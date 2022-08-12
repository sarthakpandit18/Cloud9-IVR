import os
import json
import requests
from twilio.rest import Client
import boto3
from decouple import config


def quotation_rates( input_weight):
    # aws_access_key_id = config('AWS_ACCESS_KEY_ID')
    # aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY')
    # dynamodb = boto3.resource('dynamodb', 'us-east-1', aws_access_key_id=aws_access_key_id,
    #                           aws_secret_access_key=aws_secret_access_key)
    # dynamodb_client = boto3.client('dynamodb', 'us-east-1', aws_access_key_id=aws_access_key_id,
    #                           aws_secret_access_key=aws_secret_access_key)
    # rate_table = dynamodb.Table('rates').scan()
    # price = 1000
    # for i in rate_table['Items']:
    #     if (i['weight'] >= input and i['rate'] <= price):
    #         price = i['rate']

    # return price*input

   
    payload = {
        "input_weight": input_weight
    }
    data = json.dumps(payload)
    aws_access_key_id = config('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY')
    print(aws_access_key_id+","+aws_secret_access_key)
    # lambda_client = boto3.client('lambda', 'us-east-1', aws_access_key_id=aws_access_key_id,
    #                              aws_secret_access_key=aws_secret_access_key)
    # response = lambda_client.invoke(FunctionName='getWeight',
    #                                 InvocationType='RequestResponse',
    #                                 Payload=bytes(data, encoding='utf8')
    # 
                                    # )
    url='https://a2d5ovfqj7.execute-api.us-east-1.amazonaws.com/dev/quotation'
    response = requests.post(url,data=data)
    return response.text
            



# def main():
#     quotation_rates(7)

# main()