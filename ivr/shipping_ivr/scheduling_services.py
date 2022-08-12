import os
import json
from twilio.rest import Client
import boto3
from decouple import config
from boto3.dynamodb.conditions import Key, Attr
import requests
import datetime


aws_access_key_id = config('AWS_ACCESS_KEY_ID')
aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY')
dynamodb = boto3.resource('dynamodb', 'us-east-1', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key)

def get_city():
    url = "https://a2d5ovfqj7.execute-api.us-east-1.amazonaws.com/dev/schedulingservice"
    response = requests.post(url)
    return response.text



def get_branch():
    url = "https://a2d5ovfqj7.execute-api.us-east-1.amazonaws.com/dev/getbranch"
    response = requests.get(url)
    return response.text


def get_days():
    url = "https://a2d5ovfqj7.execute-api.us-east-1.amazonaws.com/dev/get-days"
    response = requests.get(url)
    return response.text

def generateScheduledId():
    url = "https://a2d5ovfqj7.execute-api.us-east-1.amazonaws.com/dev/generatetrackingid"
    response = requests.get(url)
    return response.text


def confirmedPickup(city,branch,day,phoneNumber):
    id = generateScheduledId()
    payload = {
                "id" : id,
                "city" : city,
                "branch" : branch,
                "day" : day,
                "phoneNumber" : phoneNumber
            }
    data = json.dumps(payload)
    print("data: "+str(data))
    url = "https://a2d5ovfqj7.execute-api.us-east-1.amazonaws.com/dev/scheduledservice"
    response = requests.post(url, data = data)
    return response.text
    

