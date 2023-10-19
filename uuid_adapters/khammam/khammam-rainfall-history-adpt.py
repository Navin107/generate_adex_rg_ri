import pandas as pd
import json
from datetime import datetime
from collections import OrderedDict
import dateutil.parser
from amqp import publish

exchange_to_publish = "f5d4d767-dfdd-48b0-8afc-aa49da4c9776"
route = "f5d4d767-dfdd-48b0-8afc-aa49da4c9776/.0dc68957-c82c-4b1c-9c8a-c53c165cd705"
uuid = "0dc68957-c82c-4b1c-9c8a-c53c165cd705"

time_formatter = "%Y-%m-%dT%H:%M:%S+05:30"

def khammam_subdistricts_transform(path):
   
    try:
        df = pd.read_csv(path)
        
    except Exception as e:
        print("Error while accessing the file")
        print(e)
        
    khammam_list = []
    for row in range(0, df.shape[0]):
        khammam_dictionary = OrderedDict()
        khammam_dictionary["id"] =   uuid
        khammam_dictionary['districtCode'] = str(df.iloc[row,0])
        khammam_dictionary["subDistrictCode"] = str(df.iloc[row,1])
        khammam_dictionary["subDistrictName"] = str(df.iloc[row,4])
        khammam_dictionary["precipitation"] = float(df.iloc[row,6])
        khammam_dictionary['observationDateTime'] =  dateutil.parser.parse(str(df.iloc[row,5])).strftime(time_formatter)
        khammam_list.append(khammam_dictionary)
    
    #print(json.dumps(khammam_list,indent=4))
    publish(exchange=exchange_to_publish, routing_key=route, message=json.dumps(khammam_list))

    return None

if __name__ == "__main__":
    path = "../weather/misc/khammam-rainfall-history.csv"
    khammam_subdistricts_transform(path)
    


