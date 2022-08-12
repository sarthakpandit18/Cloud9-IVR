import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    # TODO implement
    rate_table = dynamodb.Table('rates').scan()
    price = 1000
    input = event['input_weight']
    print (input)
    for i in rate_table['Items']:
        if (i['weight'] >= input and i['rate'] <= price):
            price = i['rate']
    print(price)
    return price*input