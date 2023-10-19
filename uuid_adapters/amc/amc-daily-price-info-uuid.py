import requests
import json
import time
import datetime
from collections import OrderedDict
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz
import dateutil.parser
import xmltodict
from amqp import publish


IST = pytz.timezone("Asia/Kolkata")
exchange_to_publish = "3f01f800-92d7-4ffa-afe3-7cb4fb8aa3eeo"
route = "3f01f800-92d7-4ffa-afe3-7cb4fb8aa3ee/.4aef701f-bf08-4f66-b38b-594a9c8c15cf"
uuid = "4aef701f-bf08-4f66-b38b-594a9c8c15cf"

time_formatter = "%Y-%m-%dT%H:%M:%S+05:30"

# APScheduler==3.7.0
# pytz==2019.3
# requests==2.22.0

ignore_list = [""," ",'NULL',None,"-"," -","-"]

class amc_price(object):
   
    def getData(self):
        """
        :API is used for fetching the AMC daily price information in Telangana.
        :GET method
        :return: None
        """
        try:
            today = datetime.date.today()
            url = f"http://tsmarketing.in/WebService.asmx/DayPrices?dt1={today}"
            headers = {
            'Content-Type': 'text/xml'
            }
            response = requests.request("GET", url, headers=headers)
            response_data = xmltodict.parse(response.content)

            if response.status_code != 200:
                time.sleep(300)
                response = self.getData()
            self.publishData(response_data['DataSet']['diffgr:diffgram']['NewDataSet']['Table'])
        except requests.exceptions.HTTPError as errh:
            print("An Http Error occurred:", errh)

        except requests.exceptions.ConnectionError as errc:
            print("An Error Connecting to the API occurred:", errc)

        except requests.exceptions.Timeout as errt:
            print("A Timeout Error occurred:", errt)

        except requests.exceptions.RequestException as err:
            print("An Unknown Error occurred", err)

        except KeyError as e:
            print("key doesn't exists", e)

    def publishData(self,amc_response):
        """
        :param amc daily price info response:
        :return: None
        """
        try:
            amc_list = []
            for amc_params in amc_response:
                amc_dict = OrderedDict()
                amc_dict["id"] = uuid
                amc_dict["amcName"] = None if amc_params.get('AmcName') is None else str(amc_params.get('AmcName'))
                amc_dict["amcCode"] = None if amc_params.get('AmcCode') is None else str(amc_params.get('AmcCode'))
                amc_dict["marketName"] = None if amc_params.get('YardName') is None else str(amc_params.get('YardName'))
                amc_dict["marketID"] = None if amc_params.get('YardCode') is None else str(amc_params.get('YardCode'))
                amc_dict["commodityVarietyName"] = None if amc_params.get('CommName') is None else str(amc_params.get('CommName'))
                amc_dict["commodityVarietyCode"] = None if amc_params.get('CommCode') is None else str(amc_params.get('CommCode'))
                amc_dict["seedVarietyName"] = None if amc_params.get('VarityName') is None else str(amc_params.get('VarityName'))
                amc_dict["seedVarietyCode"] = None if amc_params.get('VarityCode') is None else str(amc_params.get('VarityCode'))
                amc_dict["arrivalQuantity"] = None if amc_params.get('Arrivals') is None else float(amc_params.get('Arrivals'))
                amc_dict["minimumPrice"] = None if amc_params.get('Minimum') is None else float(amc_params.get('Minimum'))
                amc_dict["maximumPrice"] = None if amc_params.get('Maximum') is None else float(amc_params.get('Maximum'))
                amc_dict["modalPrice"] = None if amc_params.get('Model') is None else float(amc_params.get('Model'))
                amc_dict["marketFee"] = None if amc_params.get('MarketFee') is None else float(amc_params.get('MarketFee'))
                amc_dict["agencyName"] = None if amc_params.get('ProAgencyName') is None else str(amc_params.get('ProAgencyName'))
                amc_dict["marketValuation"] = None if amc_params.get('Valuation') is None else float(amc_params.get('Valuation'))
                amc_dict['observationDateTime'] =  None if amc_params.get('DDate') is None else amc_params.get('DDate')
                amc_list.append(amc_dict)

                
            if amc_list:
                #print(json.dumps(amc_list, indent=4))
                publish(exchange=exchange_to_publish, routing_key=route, message=json.dumps(amc_list))

        except KeyError as e:
            print("key doesn't exists", e)

if __name__ == '__main__':
    sched = BlockingScheduler()
    smb = amc_price()
    sched.add_job(smb.getData,'cron',month="*", hour="23", minute="30")
    sched.start()