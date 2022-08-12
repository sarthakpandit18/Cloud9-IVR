import json
import boto3
from datetime import datetime


# Generates tracking id by incrementing the latest id
def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    schedule = dynamodb.Table('scheduled_services').scan()
    data = schedule['Items']
    sort = sorted(data, key=lambda i: i['dateCreated'])
    latestId = sort[len(sort) - 1].get('trackingID')
    print("latest id: " + str(latestId))
    latestdate_from_db = datetime.strptime(latestId[:-3], '%Y%m%d')
    latest_id_from_db = latestId[-3:]
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d")
    latestdate_from_db = str(latestdate_from_db).split(" ")[0]

    # increment the id by 1 from the latest id if it is on the same day as latest id else create a new id for the day
    # Example
    # Latest id from db - 20220627005 and the new tracking id is created on the same day --> generated tarcking id will be 20220627006
    # Latest id from db - 20220627005 and the new tracking id is created on the next day as a first id --> generated tarcking id will be 20220628001
    if current_date == latestdate_from_db:
        tempId = '%03d' % (int(latest_id_from_db) + 1)
        generatedID = str(latestdate_from_db.replace("-", "")) + str(tempId)
        print(generatedID)
    else:
        generatedID = str(current_date.replace("-", "")) + str("001")
        print(generatedID)

    return generatedID


