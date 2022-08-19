import requests
import json


client_id = '365d9a4861fb0444b51b'
client_secret = '132f56e78112f92668c4abc00b345659'
dicti = {}
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]
headers = {"X-Xapp-Token": token}


with open('test.txt') as file:
    line = file.read().splitlines()
    for artist in line:
        req = requests.get(f"https://api.artsy.net/api/artists/{artist}", headers=headers)
        js = json.loads(req.text)
        dicti[js['sortable_name']] = js['birthday']
    sorted_artist = sorted(dicti.items(), key=lambda x: x[1])
    for artist in dict(sorted_artist):
        print(artist)
