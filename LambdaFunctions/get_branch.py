import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    # TODO implement
    # TODO implement
    options = dynamodb.Table('branches').scan()
    data = options['Items']
    return data
