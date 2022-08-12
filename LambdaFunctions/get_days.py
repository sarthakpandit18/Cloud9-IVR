import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    # TODO implement
    options = dynamodb.Table('days').scan()
    data = options['Items']
    return data
