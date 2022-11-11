import requests, json, base64
import numpy as np

class Skins:
    def __init__(self):
        self.headers = {
            'Ubi-AppId': '314d4fef-e568-454a-ae06-43e3bece12a6',
            'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3",
            'Ubi-RequestedPlatformType': 'uplay',
            'GenomeId': '85c31714-0941-4876-a18d-2c7e9dce8d40',
            'Ubi-LocaleCode': "en-US"
        }
        self.token = self.login()
        self.space_id = "5172a557-50b5-4665-b7db-e3f2e8c5041d"
        self.session = requests.Session()


    # EXTRACTING ITEM NAMES 
    # ////////////////////////////////
    def extract_item_names(self, item_names):
        items = {}
        for item_name in item_names:
            if item_name['type'] not in items:
                items[item_name['type']] = {}

            if item_name['itemId'] not in items[item_name['type']]:
                items[item_name['type']][item_name['itemId']] = item_name['nameId']
        return items


    # GETTING THE USERS INVENTORY
    # ////////////////////////////////////
    def get_inventory(self, profile_id, load):
        ids, split_list = ([], [])
        r = self.session.get(f'https://public-ubiservices.ubi.com/v1/profiles/{profile_id}/inventory?spaceId={self.space_id}', headers=self.headers)

        # // Get the item ids
        for item in r.json()['items']:
            for num in range(len(load["items"])):
                if item['itemId'] in load["items"][num].values():
                    ids.append(item['itemId'])

        # // Split the item ids into arrays of length 50
        splits = np.array_split(ids, round((len(ids)/50) + 1))
        for array in splits:
            r = self.session.get(f'https://public-ubiservices.ubi.com/v1/spaces/items?spaceId={self.space_id}&itemIds={",".join(str(i) for i in list(array))}', headers=self.headers)
            for x in r.json()['items']:
                split_list.append(x)
        return self.extract_item_names(split_list)


    # REFORMATTING THE SKINS
    # ////////////////////////////////
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


    # GRABBING AUTH KEY FROM LOGIN.TXT
    # //////////////////////////////////
    def login(self):
        self.headers["Authorization"] = "Basic " + base64.b64encode(bytes(open("data/login.txt", "r").readline(), "utf-8")).decode("utf-8")
        with requests.Session() as session:
            r = session.post("https://public-ubiservices.ubi.com/v3/profiles/sessions", json={"Content-Type":"application/json"}, headers=self.headers)
            if r.status_code == 200:
                if r.json()["ticket"]:
                    self.headers['Authorization'] = "Ubi_v1 t=" + r.json()["ticket"]
                    return True
            return False


    # MAIN FUNCTION
    # //////////////////
    def get_skins(self, username):
        r = self.session.get(f'https://public-ubiservices.ubi.com/v2/profiles?nameOnPlatform={username}&platformType=uplay', headers=self.headers)
        if "message" in r.json() and "Ticket is expired" in r.json()["message"]:
            self.login()

        # // Profiles
        profile = r.json()['profiles'][0]
        profile_name = profile['nameOnPlatform']
        profile_id = profile['profileId']

        # // Load the skin format json file
        format = json.load(open("data/format.json", 'r'))
        
        # // Results
        result = {"name": profile_name,"skins": None}
        skins = self.get_inventory(profile_id, format)
        result['skins'] = self.reformat_skins(skins, format)

        # // Return the result
        return result

# // Run the program
if __name__ == "__main__":
    name_to_check = input(" // Enter Name: ")
    print(Skins().get_skins(name_to_check))
