import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    # TODO implement
    trackingid = event['trackingid']
    table = dynamodb.Table('shipment')
    print("trackingid : "+trackingid)
    response = table.get_item(Key={'tracking_id': trackingid})
    print(response['Item'])
    item = response['Item']
    return item