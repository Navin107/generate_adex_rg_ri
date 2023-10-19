import requests
import json
import time
from datetime import datetime
from collections import OrderedDict
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz
import dateutil.parser
from amqp import publish


IST = pytz.timezone("Asia/Kolkata")
exchange_to_publish = "f5d4d767-dfdd-48b0-8afc-aa49da4c9776"
route = "f5d4d767-dfdd-48b0-8afc-aa49da4c9776/.b72a23b8-5767-48a1-8fc8-6abafe23e69a"
uuid = "b72a23b8-5767-48a1-8fc8-6abafe23e69a"

time_formatter = "%Y-%m-%dT%H:%M:%S+05:30"

# APScheduler==3.7.0
# pytz==2019.3
# requests==2.22.0

ignore_list = [""," ",'NULL',None,"-"," -","-"]

sub = {"1":"Singareni","2":"Kamepalle","3":"Raghunadhapalem","4":"Khammam_Rural","5":"Thirumalayapalem","6":"Kusumanchi",
           "7":"Nelakondapalle","8":"Mudigonda","9":"Chinthakani","10":"Khammam_Urban","11":"Konijerla","12":"Enkuru",
           "13":"Kalluru","14":"Penuballi","15":"Sathupalle","16":"Vemsoor","17":"Thallada","18":"Wyra","19":"Bonakal",
           "20":"Madhira","21":"Yerrupalem"}

class weather(object):
   
    def getData(self):
        """
        :API is used for fetching the weather information of Khammam.
        :GET method
        :return: None
        """
        try:
            url = "https://tsdps.telangana.gov.in/rest/Khammamadredfdfdfdtsdpsidsdreddkfdereizllkdfhjmxjfieurhjkdfdhalskdfkxhjiehdjfdklfkdjhf"     
            weather_response = requests.get(url)
            if weather_response.status_code != 200:
                time.sleep(300)
                weather_response = self.getData()
            self.publishData(weather_response.json())
        except requests.exceptions.HTTPError as errh:
            print("An Http Error occurred:", errh)

        except requests.exceptions.ConnectionError as errc:
            print("An Error Connecting to the API occurred:", errc)

        except requests.exceptions.Timeout as errt:
            print("A Timeout Error occurred:", errt)

        except requests.exceptions.RequestException as err:
            print("An Unknown Error occurred", err)
        
    def publishData(self,weather_response):
        """
        :param weather response:
        :return: None
        """
        try:
            weather_list = []
            for weather_params in weather_response:
                
                today_date = datetime.now().date()
                api_date = datetime.strptime(weather_params.get('datetime'), "%m/%d/%Y").date()
                
                if today_date == api_date:

                    weather_dict = OrderedDict()
                    weather_dict["id"] = uuid
                    weather_dict["districtCode"] = None if weather_params.get('dcode') is None else str(weather_params.get('dcode'))
                    weather_dict["subDistrictCode"] = None if weather_params.get('dmcode') is None else str(weather_params.get('dmcode'))
                    weather_dict["subDistrictName"] = None if weather_params.get('dmcode') is None else sub[str(weather_params.get('dmcode'))]
                    weather_dict["precipitation"] = None if weather_params.get('rain') is None else weather_params.get('rain')
                    weather_dict["airTemperature"] = {"maxOverTime" : None if weather_params.get('temp_max') is None else weather_params.get('temp_max'),
                                                    "minOverTime" : None if weather_params.get('temp_min') is None else weather_params.get('temp_min')
                                                    }
                    weather_dict["relativeHumidity"] = {"maxOverTime" : None if weather_params.get('humidity_max') is None else weather_params.get('humidity_max'),
                                                    "minOverTime" : None if weather_params.get('humidity_min') is None else weather_params.get('humidity_min')
                                                    }
                    weather_dict['observationDateTime'] =  dateutil.parser.parse(str(datetime.now())).strftime(time_formatter)


                    weather_list.append(weather_dict)

                
            if weather_list:
                #print(json.dumps(weather_list, indent=4))
                publish(exchange=exchange_to_publish, routing_key=route, message=json.dumps(weather_list))

        except KeyError as e:
            print("key doesn't exists", e)

if __name__ == '__main__':
    sched = BlockingScheduler()
    smb = weather()
    sched.add_job(smb.getData,'cron',day="*", hour="11", minute="30")
    sched.start()



    

