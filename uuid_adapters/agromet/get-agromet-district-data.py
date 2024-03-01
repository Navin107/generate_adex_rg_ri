import pandas as pd
import json
from amqp import publish

exchange_to_publish = "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd"
route = "imd.gov.in/d7733b0c544dfb3137767e5efa2c1ccd3b069bf8/rs.adex.org.in/agromet-imd/.district-codes"
new_exchange_to_publish = "5d97f1bc-d548-4d02-9fd1-0e6d0f8227dd"
new_route = new_exchange_to_publish + "/.e5d6a8df-9def-4c88-897f-202a927663ef"

ri_uuid = "e5d6a8df-9def-4c88-897f-202a927663ef"
def agromet_transform(path):
    try:
        df = pd.read_excel(path)


    except Exception as e:
        print("Error while accessing the file")
        print(e)


    for row in range(0, df.shape[0]):
        agromet_dictionary = {
            "id": ri_uuid,
            "districtCode": str(df.iloc[row, 2]),
            "districtName": str(df.iloc[row, 3])
        }

        publish(exchange=new_exchange_to_publish, routing_key=new_route, message=json.dumps(agromet_dictionary))

    return None


if __name__ == "__main__":
    path = "../misc/District_tb_telangana.xlsx"
    agromet_transform(path)
