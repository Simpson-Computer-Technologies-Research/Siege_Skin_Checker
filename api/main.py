from fastapi import FastAPI, Header
import requests, json
import numpy as np
app = FastAPI()

# ENDPOINTS
# ////////////////////////
@app.get("/skins/{name}")
def skins(name: str, auth: str = Header(None)):
    headers = {
        'Ubi-AppId': 'c5393f10-7ac7-4b4f-90fa-21f8f3451a04', 
        'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3",
        'Ubi-RequestedPlatformType': 'uplay',
        'GenomeId': '85c31714-0941-4876-a18d-2c7e9dce8d40',
        'Ubi-LocaleCode': "en-US",
        "Authorization": auth
    }
    return Functions().get_skins(name, headers)


# MAIN FUNCTIONS
# ////////////////////////
class Functions():
    def __init__(self):
        self.space_id = "5172a557-50b5-4665-b7db-e3f2e8c5041d"
        self.session = requests.Session()
        self.format = json.load(open("data/format.json", 'r'))

    # // Extract the type of skins
    def extract_item_names(self, item_names):
        items = {}
        for item_name in item_names:
            if item_name['type'] not in items:
                items[item_name['type']] = {}

            if item_name['itemId'] not in items[item_name['type']]:
                items[item_name['type']][item_name['itemId']] = item_name['nameId']
        return items

    # // Reformat the skins into map
    def reformat_skins(self, skins, format_list):
        formatted = {}
        for skin_type in skins:
            for skin_id in skins[skin_type]:
                for format_items in format_list["items"]:
                    if skin_id == format_items["id"]:
                        if format_items["category"] not in formatted:
                            formatted.update({format_items["category"]: []})
                        formatted[format_items["category"]].append(format_items["name"])
        return formatted

    # // Get the inventory of the ubisoft profile
    def get_inventory(self, profile_id, load, headers):
        temp_ids, split_list = ([], [])
        r = self.session.get(f'https://public-ubiservices.ubi.com/v1/profiles/{profile_id}/inventory?spaceId={self.space_id}', headers=headers)

        # // Get the item ids
        for item in r.json()['items']:
            for num in range(len(load["items"])):
                if item['itemId'] in load["items"][num].values():
                    temp_ids.append(item['itemId'])

        # // Split the item ids into arrays of length 50
        splits = np.array_split(temp_ids, round((len(temp_ids)/50) + 1))
        for array in splits:
            r = self.session.get(f'https://public-ubiservices.ubi.com/v1/spaces/items?spaceId={self.space_id}&itemIds={",".join(str(i) for i in list(array))}', headers=headers)
            for x in r.json()['items']:
                split_list.append(x)
        return self.extract_item_names(split_list)

    # // Primary function to get the skins of the user
    def get_skins(self, username, headers):
        # // Send http request to ubisoft api
        r = self.session.get(f'https://public-ubiservices.ubi.com/v2/profiles?nameOnPlatform={username}&platformType=uplay', headers=headers)
        try:
            # // Profile Variables
            profile = r.json()['profiles'][0]
            profile_name = profile['nameOnPlatform']
            profile_id = profile['profileId']

            # // Results
            result = {"name": profile_name,"skins": None}
            skins = self.get_inventory(profile_id, self.format, headers)
            result['skins'] = self.reformat_skins(skins, self.format)

            # // Return result
            return result
        except:
            return r.json()
