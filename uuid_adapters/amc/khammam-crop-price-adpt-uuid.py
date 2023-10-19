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
exchange_to_publish = "3f01f800-92d7-4ffa-afe3-7cb4fb8aa3ee"
route = "3f01f800-92d7-4ffa-afe3-7cb4fb8aa3ee/.9c24f067-9552-45c2-9137-512263651b79"
uuid  = "9c24f067-9552-45c2-9137-512263651b79"

time_formatter = "%Y-%m-%dT%H:%M:%S+05:30"

# APScheduler==3.7.0
# pytz==2019.3
# requests==2.22.0

ignore_list = [""," ",'NULL',None,"-"," -","-"]

class khammam_price(object):
   
    def getData(self):
        """
        :API is used for fetching the Khammam AMC price information of Telangana.
        :GET method
        :return: None
        """
        try:
            today = datetime.date.today()
            url = "http://tsmarketing.in/WebService.asmx?op=khammamPrices"
            payload = f"<soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\n  <soap:Body>\n    <khammamPrices xmlns=\"http://tsmarketing.in/\">\n      <dt1>{today}</dt1>\n      <dt2>{today}</dt2>\n    </khammamPrices>\n  </soap:Body>\n</soap:Envelope>"
            headers = {
            'Content-Type': 'text/xml'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            response_data = xmltodict.parse(response.content)

            if response.status_code != 200:
                time.sleep(300)
                response = self.getData()
            self.publishData(response_data['soap:Envelope']['soap:Body']['khammamPricesResponse']['khammamPricesResult']['diffgr:diffgram']['NewDataSet']['Table'])
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

    def publishData(self,khammam_response):
        """
        :param khammam amc info response:
        :return: None
        """
        try:
            khammam_list = []
            for khammam_params in khammam_response:
                khammam_dict = OrderedDict()
                khammam_dict["id"] = uuid
                khammam_dict["amcName"] = None if khammam_params.get('AmcName') is None else str(khammam_params.get('AmcName'))
                khammam_dict["commodityVarietyName"] = None if khammam_params.get('VarityName') is None else str(khammam_params.get('VarityName'))
                khammam_dict["arrivalQuantity"] = None if khammam_params.get('Arrivals') is None else float(khammam_params.get('Arrivals'))
                khammam_dict["minimumPrice"] = None if khammam_params.get('Minimum') is None else float(khammam_params.get('Minimum'))
                khammam_dict["maximumPrice"] = None if khammam_params.get('Maximum') is None else float(khammam_params.get('Maximum'))
                khammam_dict["modalPrice"] = None if khammam_params.get('Model') is None else float(khammam_params.get('Model'))
                khammam_dict["agencyName"] = None if khammam_params.get('ProAgencyName') is None else str(khammam_params.get('ProAgencyName'))
                khammam_dict['observationDateTime'] =  None if khammam_params.get('DDate') is None else khammam_params.get('DDate')
                khammam_list.append(khammam_dict)

                
            if khammam_list:
                #print(json.dumps(khammam_list, indent=4))
                publish(exchange=exchange_to_publish, routing_key=route, message=json.dumps(khammam_list))

        except KeyError as e:
            print("key doesn't exists", e)

if __name__ == '__main__':
    sched = BlockingScheduler()
    smb = khammam_price()
    sched.add_job(smb.getData,'cron',month="*", hour="23", minute="30")
    sched.start()
