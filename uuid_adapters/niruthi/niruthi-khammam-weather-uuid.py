from datetime import datetime, date, timedelta, time
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import json
import pytz
from amqp import publish
exchange_to_publish = "e4917519-c5fc-4bd9-9f89-0dd22aa54eec"
exchange_to_publish_bck = "niruthi.com/16327cbbfce71b6df9af71036acfd7d2a40453ae/rs.adex.org.in/niruthi-weather"
route = "e4917519-c5fc-4bd9-9f89-0dd22aa54eec/.d60e022f-e32a-4d66-8178-0e7d91361c95"
route_bck = "niruthi.com/16327cbbfce71b6df9af71036acfd7d2a40453ae/rs.adex.org.in/niruthi-weather/.khammam-weather-info"
IST=pytz.timezone("Asia/Kolkata")
ri_uuid = "d60e022f-e32a-4d66-8178-0e7d91361c95"

class NiruthiWeather(object):
    def __init__(self, headers, base_url):
        self.headers = headers
        self.base_url = base_url

    def getData(self):
        try:
            start_date = "2023-07-18"
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = "2023-08-30"
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            while start_date <= end_date:
                query_date = start_date
                payload = json.dumps({
                    "state": "Telangana",
                    "district": "Khammam",
                    "q_date": str(query_date)
                })
                response = requests.request("POST", self.base_url, headers=headers, data=payload)
                res = response.json()["iudx_filterapi"]
                self.transformData(res, query_date)
                start_date += timedelta(days=1)


        except IndexError as ie:
            print("No data observed for " + str(query_date))
        except requests.Timeout as err:
            print("Connection Timeout error.")
        except requests.exceptions.ConnectionError:
            print("Connection refused.")
        except Exception as e:
            print("Exception has Occurred ", e)


    def transformData(self, response, query_date):
        """
        :API is used to transform data according to our data model.
        :param sewage_data:
        :return: transformed all response data according to data model.
        """
        transformedOutput = []
        for data in response:
            final_data = dict()
            final_data["id"] = ri_uuid

            final_data["subdistrictName"] = data["subdistrict"]
            final_data["villageName"] = data["village"]
            final_data["gramPanchayatName"] = data["gp"]
            final_data["windSpeed"] = {"avgOverTime": data["avgwind"][0]["value"],
                                       "maxOverTime": data["maxwind"][0]["value"]}
            final_data["precipitation"] = data["prcp"][0]["value"]
            final_data["relativeHumidity"] = {"avgOverTime": data["rhavg"][0]["value"],
                                              "maxOverTime": data["rhmax"][0]["value"],
                                              "minOverTime": data["rhmin"][0]["value"]}
            final_data["solarRadiation"] = data["srad"][0]["value"]
            final_data["dewPoint"] = data["tdew"][0]["value"]
            final_data["airTemperature"] = {"maxOverTime": data["tmax"][0]["value"],
                                            "minOverTime": data["tmin"][0]["value"]}
            final_data["dayLength"] = data["daylength"][0]["value"]
            final_data["location"] = {
                            "type": "Point",
                            "coordinates": [float(data["longitude"]), float(data["latitude"])]
            }
            datetime_obj = datetime.strptime(str(query_date) + " " + str(time(0, 0, 0)), "%Y-%m-%d %H:%M:%S")
            iudx_date_format = datetime_obj.astimezone(IST).isoformat()

            final_data["observationDateTime"] = iudx_date_format
            transformedOutput.append(final_data)

        # print(json.dumps(transformedOutput, indent=3))
        publish(exchange=exchange_to_publish, routing_key=route, message=json.dumps(transformedOutput))

if __name__ == "__main__":
    sched = BlockingScheduler()
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer icbfPwGoTaH4vU4NteCLWusHI6A20GOIdhBqDDfb7z3jIBe47eMI1Bg6e9SCE1UzjyBNZaSPxaYq7fiY2QZmt8DFcR4JxT4sWY98wFlwVWLf4tcsba1MhzaPH05sVtYC"
    }
    base_url = "https://iudxapiserver.apps.niruthi.com/getparamdata"
    obj = NiruthiWeather(headers, base_url)
    obj.getData()
