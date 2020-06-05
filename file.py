import json
import requests

with open("conf.json", 'r') as confFile:
    conf = confFile.read()

conf = json.loads(conf)

iosJson = None

for server in conf['servers']:
    serverAddr = server['serverAddress']
    iosJsonPath = server['iosJson']
    androidJsonPath = server['androidJson']
    adsPath = server['ads'] if server['ads'] != "" else None

    iosJsonAddr = f"{serverAddr}{iosJsonPath}"
    androidJsonAddr = f"{serverAddr}{androidJsonPath}"

    try:
        iosRequest = requests.get(iosJsonAddr)
    except Exception:
        continue

    if not iosRequest or iosRequest.status_code != 200:
        # 200 is 'ok'
        continue
    else:
        iosJson = json.loads(iosRequest.text)
        break

if not iosJson:
    iosJson = "LOAD JSON FROM CACHE"

print(iosJson)
