from twilio.rest import Client
import boto3
from decouple import config
import json
import requests
from twilio.rest import Client


aws_access_key_id = config('AWS_ACCESS_KEY_ID')
aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY')
dynamodb = boto3.resource('dynamodb', 'us-east-1', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key)


def get_shipment_details(tracking_id):
    payload = {
                "tracking_id" : tracking_id
            }
    data = json.dumps(payload)
    url = "https://a2d5ovfqj7.execute-api.us-east-1.amazonaws.com/dev/download-invoice"
    response = requests.get(url, data = data)
    jsonResponse = json.loads(response.text)
    lambda_response = json.loads(jsonResponse)
    s3_uri = lambda_response['s3_uri']
    client = Client('AC9c97bcd2de84f7993a7a0f55780674a4', 'a0d8e0562c48f4ed884f82100fbcb8c7')

    message = client.messages \
        .create(
        body=s3_uri,
        from_='+18252519025',
        to='+19029894402'
    )
    return response.text
