import requests
import json
from os.path import exists
from datetime import datetime, timedelta
from amqp import publish
from apscheduler.schedulers.blocking import BlockingScheduler
from dateutil import parser
import re

exchange_to_publish = "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd"
route = "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd/.advisory-subdistrict-data"
id = "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd/advisory-subdistrict-data"
new_exchange_to_publish = "5d97f1bc-d548-4d02-9fd1-0e6d0f8227dd"
new_route = new_exchange_to_publish + "/.68593b2b-00e4-4a90-a74f-ddf6840d32d8"

ri_uuid = "68593b2b-00e4-4a90-a74f-ddf6840d32d8" 

class agrometData:

    def __init__(self, base_url):
        self.base_url = base_url

    def subdistrict_data(self):

        url = self.base_url

        try:
            now = datetime.now() + timedelta(days=-1)
            date = now.strftime("%Y-%m-%d")
            base_url = url + date + "/541"
            response = requests.request("GET", base_url)
            response_data = response.text.split("Total Number of Record=")

            if "[" in response_data[1]:
                response_data = response_data[1].split("[")
                json_array = json.loads("[" + response_data[1])

            elif "{" in response_data[1]:
                response_data = response_data[1].split("{")
                json_array = json.loads("{" + response_data[1])

            self.transform_publish(json_array)


        except requests.exceptions.HTTPError as errh:
            print("An Http Error occurred:", errh)

        except requests.exceptions.ConnectionError as errc:
            print("An Error Connecting to the API occurred:", errc)

        except requests.exceptions.Timeout as errt:
            print("A Timeout Error occurred:", errt)

        except requests.exceptions.RequestException as err:
            print("A Request Exception Error occurred", err)

        except Exception as oe:
            print("An unknown error occurred", oe)

    def transform_publish(self, json_array):
        """
        Transforms the data as per IUDX vocab and publishes them
        :param list_of_packets: list of packets containing aqm locations
        :type list_of_packets:list

        """
        if type(json_array) == dict:
            if json_array.get("message"):
                print("No subdistrict advisory were found")
                return

        transformed_records = []
        for packet in json_array:
            v = packet["custom_date"]
            transformed_record = {
                "id": ri_uuid,
                "observationDateTime": f"{parser.parse(v).isoformat()}+05:30",
                "agriculturalCategory": packet["category_name"],
                "stateCode": packet["state_id"],
                "stateName": packet["state_name"],
                "districtCode": packet["district_id"],
                "districtName": packet["district_name"],
                "subdistrictCode": packet["asd_id"],
                "subdistrictName": packet["asd_name"],
                "commodityCode": packet["type_id"],
                "commodityName": packet["crop_name"],
                "regionalLangID": packet["reg_lang_id"],
                "regionalLangName": packet["reg_lang_name"],
                "generalAdvisory": packet["general_advisory_eng"],
                "generalAdvisoryRegional": packet["general_advisory_reg"],
                "smsAdvisory": packet["sms_eng"],
                "smsAdvisoryRegional": packet["sms_reg"],
                "technicalAdvisory": packet["advisory_eng"],
                "technicalAdvisoryRegional": packet["advisory_reg"],
                "weatherSummary": packet["weather_summary_eng"],
                "weatherSummaryRegional": packet["weather_summary_reg"]
            }

            transformed_records.append(transformed_record)

        self.deduplication(transformed_records)

    def deduplication(self, current_list_of_packets):

        """
        Removes duplicates from current_list of packets for each cycle &
        Stores list of packets seen in each cycle as json dump.
        :param current_list_of_packets: contains packets obtained at each cycle
        :type current_list_of_packets: List
        """

        if not (exists('../misc/agromet-subdistrict-level.json')):

            with open('../misc/agromet-subdistrict-level.json', 'w', encoding='utf-8') as fp:
                json.dump(current_list_of_packets, fp, indent=6, ensure_ascii=False)
                self.publish_data(current_list_of_packets)


        else:
            with open('../misc/agromet-subdistrict-level.json', 'r+', encoding='utf-8') as fp:
                json_str = fp.read()

                if json_str != "":
                    cache_list = json.loads(json_str)
                    fp.seek(0)
                    fp.truncate(0)
                    diff_list = [packet for packet in current_list_of_packets if packet not in cache_list]
                    json.dump(cache_list + diff_list, fp, indent=6, ensure_ascii=False)
                    self.publish_data(diff_list)

                else:

                    with open('../misc/agromet-subdistrict-level.json', 'w') as fp:
                        json.dump(current_list_of_packets, fp, indent=6, ensure_ascii=False)
                        self.publish_data(current_list_of_packets)

    def strip_whitespace(self, json_array):

        for json_data in json_array:
            for key, value in json_data.items():
                pattern = r"[\r\n\t•]"
                json_data[key] = re.sub(pattern, "", value)

        return json_array

    def publish_data(self, json_transformed_packet):

        json_data = json.dumps(json_transformed_packet, ensure_ascii=False)
        json_array = self.strip_whitespace(json.loads(json_data))

        for packet in json_array:
            # print(json.dumps(packet, indent=5, ensure_ascii=False))
            publish(exchange=new_exchange_to_publish, routing_key=new_route, message=json.dumps(packet, ensure_ascii=False))


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    BASE_URL = "https://agromet.imd.gov.in/index.php/api/Advisory_service/teln_asd_advisory/"
    agromet_subdistrict_data = agrometData(BASE_URL)
    agromet_subdistrict_data.subdistrict_data()
    scheduler.add_job(agromet_subdistrict_data.subdistrict_data, "cron", hour=1, minute=00, second=00)
    scheduler.start()


