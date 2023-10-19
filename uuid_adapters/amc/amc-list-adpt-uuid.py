import requests
import json
import time
from datetime import datetime
from collections import OrderedDict
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz
import dateutil.parser
import xmltodict
from amqp import publish


IST = pytz.timezone("Asia/Kolkata")
exchange_to_publish = "3f01f800-92d7-4ffa-afe3-7cb4fb8aa3ee"
route = "3f01f800-92d7-4ffa-afe3-7cb4fb8aa3ee/.537b3f73-c543-4b69-bc4e-5790ef54b6c3"
uuid = "537b3f73-c543-4b69-bc4e-5790ef54b6c3"

time_formatter = "%Y-%m-%dT%H:%M:%S+05:30"

# APScheduler==3.7.0
# pytz==2019.3
# requests==2.22.0

ignore_list = [""," ",'NULL',None,"-"," -","-"]

class amc_list(object):
   
    def getData(self):
        """
        :API is used for fetching the AMC List information of Telangana.
        :GET method
        :return: None
        """
        try:
            url = "http://tsmarketing.in/WebService.asmx/AmcList"
            payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\n  <soap:Body>\n    <AmcList xmlns=\"http://tsmarketing.in/\" />\n  </soap:Body>\n</soap:Envelope>"
            headers = {
            'Content-Type': 'application/xml'
            }
            amc_response = requests.request("POST", url, headers=headers, data=payload)
            response_data = xmltodict.parse(amc_response.content)
            if amc_response.status_code != 200:
                time.sleep(300)
                amc_response = self.getData()
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
        :param amc list response:
        :return: None
        """
        try:
            amc_list = []
            for amc_list_params in amc_response:
                if amc_list_params.get('AmcCode') not in dupl_list:
                    amc_dict = OrderedDict()
                    amc_dict["id"] = uuid
                    amc_dict["districtCode"] = None if amc_list_params.get('dno') is None else str(amc_list_params.get('dno'))
                    amc_dict["districtName"] = None if amc_list_params.get('dname') is None else str(amc_list_params.get('dname'))
                    amc_dict["address"] = None if amc_list_params.get('address') is None else amc_list_params.get('address')
                    amc_dict["amcCode"] = None if amc_list_params.get('AmcCode') is None else amc_list_params.get('AmcCode')
                    amc_dict["amcName"] = None if amc_list_params.get('AmcName') is None else amc_list_params.get('AmcName')
                    amc_dict["amcGrade"] = None if amc_list_params.get('AmcGrade') is None else amc_list_params.get('AmcGrade')
                    amc_dict["telephone"] = None if amc_list_params.get('tel') is None else amc_list_params.get('tel')
                    amc_dict['observationDateTime'] =  dateutil.parser.parse(str(datetime.now())).strftime(time_formatter)
                    amc_list.append(amc_dict)
                    dupl_list.append(amc_dict["amcCode"])
                
            if amc_list:
                #print(json.dumps(amc_list, indent=4))
                publish(exchange=exchange_to_publish, routing_key=route, message=json.dumps(amc_list))

        except KeyError as e:
            print("key doesn't exists", e)

if __name__ == '__main__':
    sched = BlockingScheduler()
    smb = amc_list()
    dupl_list = []
    sched.add_job(smb.getData,'cron',month = "*",day = "1", hour="5", minute="30")
    sched.start()



