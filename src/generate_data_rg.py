import json
import requests
from collections import OrderedDict
import uuid

class IUDXDataProcessor:
    
    def __init__(self):
    
        self.resource_group_data = self.load_json_file('../raw/resourceGroup.json')
        self.resources_data = self.load_json_file('../raw/resources.json')
        self.provider_data = self.load_json_file('../raw/provider.json')
        self.user_data = self.load_json_file('../raw/sha-keycloak.json')
        self.resource_server_data = self.load_json_file("../raw/resource-server.json")

    def load_json_file(self, file_path):
        with open(file_path) as file:
            return json.load(file)

    def process_provider(self, json_data):
        provider_id = json_data["id"]

        json_data["id_bck"] = provider_id
        json_data["id"] = self.provider_data.get(provider_id)
        json_data["resourceServer"] = "ab311420-7d84-4a0a-9fdb-c811be588589"
        json_data["resourceServer_bck"] = "datakaveri.org/27e503da0bdda6efae3a52b3ef423c1f9005657a/rs.iudx.org.in"
        json_data["ownerUserId"] = self.user_data.get(provider_id)

        desired_keys = [
            "@context","id", "id_bck",  "type", "name", "description", "resourceServer", "resourceServer_bck", "providerOrg"
        ]
        return self.extract_desired_keys(desired_keys, json_data)

    def process_resource_group(self, json_data):
        rg_id = json_data["id"]
        provider_id = json_data["provider"]

        json_data["id_bck"] = rg_id
        json_data["id"] = self.resource_group_data.get(rg_id) 
        json_data["provider"] = self.provider_data.get(provider_id)
        json_data["provider_bck"] = provider_id
        json_data["ownerUserId"] = self.user_data.get(provider_id)
        json_data["cos"] =  "49f96c4c-e595-4fee-984c-43dededfba48"

        desired_keys = ["@context", "id", "id_bck", "type", "name", "label", "description", "tags", "provider", "provider_bck", "itemStatus", "location", "instance", "ownerUserId", "cos", "itemCreatedAt"]
        return self.extract_desired_keys(desired_keys, json_data)
    
    def fetch_url_data(self, url):
        response = requests.get(url)
        dict_data = response.json()
        json_array = dict_data.get("results", [])
        return json_array

    def extract_desired_keys(self, desired_keys, json_data):
        return {key: json_data[key] for key in desired_keys if json_data.get(key)}

    def generate(self):

        url = "https://api.dataexplorer.adex.org.in/adex/cat/v1/search?property=[type]&value=[[iudx:ResourceGroup]]"
        json_array = self.fetch_url_data(url)

        json_changed_dict = []

        for json_data in json_array:

            json_data = OrderedDict(json_data)
            json_changed_dict.append(self.process_resource_group(json_data))

        return json_changed_dict

data_processor = IUDXDataProcessor()
uuid_data = data_processor.generate()

with open("../generated_data/generate-resource-group.jsonld", "w") as f:
    json.dump(uuid_data,f,indent=5)

print("done")