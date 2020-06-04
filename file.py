import json
import requests

with open("conf.json", 'r') as file:
    conf = file.read()

d = json.loads(conf)

server = d['serverAddress']
ios = d['iosJson']
android = d['androidJson']

ios_json_addr = f"{server}{ios}"
android_json_addr = f"{server}{android}"

ios_req = requests.get(ios_json_addr)
android_req = requests.get(android_json_addr)

ios_json = json.loads(ios_req.text, encoding="utf-8")
android_json = json.loads(android_req.text, encoding="utf-8")

print(ios_json)
print(android_json)
