import requests
import json
import dateutil.parser as dp
from amqp import publish
from apscheduler.schedulers.blocking import BlockingScheduler
import os
from dateutil import parser

exchange_to_publish = "e59365a9-7808-450d-8a42-3269dfcd7e8b"
exchange_to_publish_bck = "krishitantra.com/dd9561b09f5d63b59160388f96085a55d24e7795/gateway.adex.org.in/krishitantra-data"

route = "e59365a9-7808-450d-8a42-3269dfcd7e8b/.938f7c21-5a53-4d5e-988b-60d8f2e0c963"
route_bck = "krishitantra.com/dd9561b09f5d63b59160388f96085a55d24e7795/gateway.adex.org.in/krishitantra-data/.soil-tests-data"

ri_uuid = "938f7c21-5a53-4d5e-988b-60d8f2e0c963"
# id_bck = "krishitantra.com/dd9561b09f5d63b59160388f96085a55d24e7795/gateway.adex.org.in/krishitantra-data/soil-tests-data"

class agrometData:
    
    def __init__(self, base_url):
        self.base_url = base_url

    def getToken(self):
                
        try:
            
            payload = """{
                "query":"mutation GenerateAccessToken($refreshToken: String!, $clientId: String!, $clientSecret: String!) {generateAccessToken(refreshToken: $refreshToken, client_id: $clientId, client_secret: $clientSecret)}",
                "variables":{"refreshToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlblR5cGUiOiJSZWZyZXNoVG9rZW4iLCJvcmdhbml6YXRpb24iOiI2Mjk2ZmI4MTJiY2EzZjAwMTNhMzFjYWYiLCJ0eXBlIjoiVXNlciIsInN1YiI6IjYzZTllYzNlZTBjOGY1MDAxOTA5N2FjYSIsImlhdCI6MTY4NDIzODg2NSwiZXhwIjoxOTk5ODE0ODY1LCJhdWQiOiJLcmlzaGl0YW50cmEuY29tIiwiaXNzIjoiS3Jpc2hpdGFudHJhLmNvbSIsImp0aSI6IjcxMzk0NmY0LWQ3ZjgtNDE2OC05ZDhkLWU5NzlmYjE1NmQxOSJ9.aCNaBQc66nVtNiQphsBxfQHMmPvHPd8Z9SP_K1cFXgo\",\"clientId\":\"6463720eb77653001be002f1\",\"clientSecret\":\"fc*uL$wCRe5gkmT&u2S&tN4TJTv6#ZD6"}
                }"""
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", self.base_url, headers=headers, data=payload)
            
            token = response.json()["data"]["generateAccessToken"]["token"]
                        
            self.getData(token)


        except requests.exceptions.HTTPError as errh:
            print("An Http Error occurred:", errh)

        except requests.exceptions.ConnectionError as errc:
            print("An Error Connecting to the API occurred:", errc)

        except requests.exceptions.Timeout as errt:
            print("A Timeout Error occurred:", errt)

        except requests.exceptions.RequestException as err:
            print("An Unknown Error occurred", err)

        except Exception as oe:
            print("An Unknown Error occurred", oe)

    def getData(self, token):

        """
        Fetching from seeding api
        :params end_point: end point which consists of attribute or temporal query
        :return None:
        """


        try:
            
            payload = "{\"query\":\"query GetTestByOrg($computedId: String, $testCentre: String, $from: String, $to: String) {\\n  getTestByOrg(computedID: $computedId, testCentre: $testCentre, from: $from, to: $to) {\\n     computedID\\n    id\\n    location\\n    crop\\n    previousCrop\\n    previousYield\\n    previousYieldPrice\\n    targetYield\\n    previousManure\\n    previousfertilizerQuantity\\n     results\\n    testCentre {\\n      id\\n      name\\n      createdAt\\n      updatedAt\\n      testCentreCode\\n    }\\n    plot {\\n        surveyNo\\n    }\\n    createdAt\\n    updatedAt\\n    startedAt\\n    endedAt\\n    sampleDate\\n    testCompletedAt\\n  }\\n}\",\"variables\":{\"testCentre\":\"digitalgreen00001\"}}"
            
            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(token)
            }

            response = requests.request("POST", self.base_url, headers=headers, data=payload)
            
            resp = response.json()
            
            json_array = resp["data"]["getTestByOrg"]
                        
            
            self.transform_publish(json_array)
                        
                 
        except requests.exceptions.HTTPError as errh:
            print("An Http Error occurred:", errh)

        except requests.exceptions.ConnectionError as errc:
            print("An Error Connecting to the API occurred:", errc)

        except requests.exceptions.Timeout as errt:
            print("A Timeout Error occurred:", errt)

        except requests.exceptions.RequestException as err:
            print("An Unknown Error occurred", err)

        except Exception as oe:
            print("An Unknown Error occurred", oe)
                
            
    def transform_publish(self, list_of_packets):
        """
        Transforms the data as per IUDX vocab and publishes them
        :param list_of_packets: list of packets containing aqm locations
        :type list_of_packets:list
        
        """
        time_formatter = "%Y-%m-%dT%H:%M:%S+05:30"

        transformed_records = []
        
        for packet in list_of_packets:
            observation_date = packet["sampleDate"]
            testCompletedDate = packet["testCompletedAt"]
            
            transformed_record={
                "id": ri_uuid,
                "sampleID":packet["id"],
                "location":packet["location"],
                "cropNameCommon":packet["crop"],
                "previousCropName":packet["previousCrop"],
                "previousYield":packet["previousYield"],
                "targetYield":packet["targetYield"],
                "surveyNumber":packet["plot"]["surveyNo"],
                "boron":packet["results"].get("B",None),
                "cu":packet["results"].get("Cu",None),
                "electricalConductivity":packet["results"].get("EC",None),
                "fe":packet["results"].get("Fe",None),
                "organicCarbon":packet["results"].get("OC",None),
                "sulphur":packet["results"].get("S",None),
                "zn":packet["results"].get("Zn",None),
                "potassium":packet["results"].get("k",None),
                "nitrogen":packet["results"].get("v",None),
                "phosphorus":packet["results"].get("p",None),
                "pH":packet["results"].get("pH",None),
                "testCentreID":packet["testCentre"]["id"],
                "testCentreName":packet["testCentre"]["name"],
                "testCentreCode":packet["testCentre"]["testCentreCode"],
                "testDateTime":parser.parse(testCompletedDate).strftime(time_formatter) if testCompletedDate else None,
                "observationDateTime": parser.parse(observation_date).strftime(time_formatter) if observation_date else None

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

        cache_file = '../misc/krishi-data.json'

        if not os.path.exists(cache_file):
            with open(cache_file, 'w') as fp:
                self.write_json_file(current_list_of_packets, fp)
        
        else:
            with open(cache_file, 'r+') as fp:
                json_str = fp.read()

                if json_str != "":
                    self.deduplication_checker(json_str, fp, current_list_of_packets)
                else:
                    with open(cache_file, 'w') as fp:
                        self.write_json_file(current_list_of_packets, fp)                       
    
    def deduplication_checker(self, json_str, fp, current_list_of_packets):
        cache_list = json.loads(json_str)
        fp.seek(0)
        fp.truncate(0)
        diff_cache_packet = {}
        diff_packet = []
        
        for packet in current_list_of_packets:
            
            if packet["sampleID"] not in cache_list.keys():
                diff_cache_packet[packet["sampleID"]] = packet
                diff_packet.append(packet) 

            elif str(packet["sampleID"]) in cache_list.keys() and dp.parse(packet["observationDateTime"]) > dp.parse(cache_list[str(packet["sampleID"])]["observationDateTime"]):
                cache_list[packet["sampleID"]] = packet
                diff_packet.append(packet) 

        json.dump({**cache_list, **diff_cache_packet}, fp, indent=7)
        self.publish_data(diff_packet)

    def write_json_file(self, current_list_of_packets, fp):
        
        self.publish_data(current_list_of_packets)
        cache_packet = {packet["sampleID"] : packet for packet in current_list_of_packets}
        json.dump(cache_packet, fp, indent=6)
        
    def publish_data(self, json_transformed_packet):

        for packet in json_transformed_packet:
            
            # print(packet)
                        
            publish(exchange=exchange_to_publish, routing_key=route, message=json.dumps(packet, ensure_ascii=False))

    
if __name__ == "__main__":
    scheduler = BlockingScheduler()
    BASE_URL =  "https://soilv3-api-prod.krishitantra.com/"    
    krishi_tantra_data = agrometData(BASE_URL)
    krishi_tantra_data.getToken()
    scheduler.add_job(krishi_tantra_data.getToken, "interval", days=30)
    scheduler.start()

