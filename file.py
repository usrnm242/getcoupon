import json
import requests
import datetime


# with open("conf.json", 'r') as confFile:
#     conf = confFile.read()

start = datetime.datetime.now()
conf = requests.get("https://usrnm242.github.io/getcoupon/conf.json").text
stop = datetime.datetime.now()
measurement = stop - start

print(f"conf: {measurement.seconds}.{measurement.microseconds} seconds")

conf = json.loads(conf)

iosJson = None

server = conf['defaultServer']

serverAddr = server['serverAddress']
iosJsonPath = server['iosJson']
androidJsonPath = server['androidJson']
adsPath = server['ads'] if server['ads'] != "" else None

iosJsonAddr = f"{serverAddr}{iosJsonPath}"
androidJsonAddr = f"{serverAddr}{androidJsonPath}"

try:
    start = datetime.datetime.now()
    iosRequest = requests.get(iosJsonAddr)
    stop = datetime.datetime.now()
    measurement = stop - start
    print(f"json: {measurement.seconds}.{measurement.microseconds} seconds")
except Exception as e:
    raise(e)

if not iosRequest:
    raise AttributeError("not iosRequest")
elif iosRequest.status_code != 200:
    raise AttributeError(f"status: {iosRequest.status_code}")
else:
    iosJson = json.loads(iosRequest.text)

assert iosJson

req = requests.get(f"{serverAddr}{adsPath}")
assert req
ads = req.text
# print(ads)
# print(iosJson)
