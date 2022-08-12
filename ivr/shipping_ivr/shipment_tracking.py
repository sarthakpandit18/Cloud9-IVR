import json
import requests


def shipment_tracking(trackingid):
    payload = {
        "trackingid": trackingid
    }
    data = json.dumps(payload)
    url = "https://a2d5ovfqj7.execute-api.us-east-1.amazonaws.com/dev/shipmentstatus";
    response = requests.post(url, data=data)
    return response.text
