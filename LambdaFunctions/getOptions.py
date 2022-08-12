import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb', 'us-east-1')
    options = dynamodb.Table('ivr_options').scan()
    data = options['Items']
    print(type(data))
    for i in data:
        print(i['name'])
    return data