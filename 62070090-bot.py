import json
import requests
import time
requests.packages.urllib3.disable_warnings()

api_url = "https://10.0.15.104/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback62070090"

headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json"
}
basicauth = ("admin", "cisco")

accesstoken = 'ODEyY2NkNmYtZTI3NC00M2Q1LWEwZTctMjdjNDQ5OGNjMjcxMmQ2NjY0YjgtYmM5_P0A1_4a252141-f787-4173-a4c9-bde69c553a24'
roomid = 'Y2lzY29zcGFyazovL3VzL1JPT00vNjUwODkzMjAtY2QxOS0xMWVjLWE1NGUtNGQ2MmNhMWM4YmVl'
url = 'https://webexapis.com/v1/messages'
webexbot_headers = {
    'Authorization': 'Bearer {}'.format(accesstoken),
    'Content-Type': 'application/json'
}
def getStatusLo():
    response = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
    if response.status_code == 404:
        return "Loopback62070090 - Operational status is down"
    else:
        response_json = response.json()
        return "Loopback62070090 - Operational status is " + response_json["ietf-interfaces:interface"]["oper-status"]

def bot():
    getParams = {
            "roomId": roomid,
            "max": 1
        }

    while True:
        message = requests.get(url, headers=webexbot_headers, params=getParams).json()
        print("Received message: " + message["items"][0]["text"])
        if message["items"][0]["text"] == "62070090":
            postParams = {
                "roomId": roomid,
                "markdown": getStatusLo()
            }
            response = requests.post(url, headers=webexbot_headers, json=postParams)
        time.sleep(1)

bot()