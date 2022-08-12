import json
import boto3


def lambda_handler(event, context):
    # TODO implement

    # # Create an SNS client
    client = boto3.client(
        "sns"
    )

    # Create the topic if it doesn't exist (this is idempotent)
    # topic = client.create_topic(Name="notifications")
    # topic_arn = "arn:aws:sns:us-east-1:404266862861:cloud9_invoice"  # get its Amazon Resource Name
    number = event['mobile_number']
    print(number)
    invoiceURL = event['s3_uri']
    # r = client.subscribe(
    #         TopicArn=topic_arn,
    #         Protocol='sms',
    #         Endpoint='+19029897588'  # <-- number who'll receive an SMS message.
    #     )
    # print("subscribe : "+str(r))

    # Publish a message.
    response = client.publish(Message=invoiceURL, PhoneNumber=str(number))

    print(response)
    return response
