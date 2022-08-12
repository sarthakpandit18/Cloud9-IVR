import json
import boto3
import datetime


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


def getDayNum(day):
    if day == "Monday" or day == "monday":
        return 0
    if day == "Tuesday" or day == "tuesday":
        return 1
    if day == "Wednesday" or day == "wednesday":
        return 2
    if day == "Thursday" or day == "thursday":
        return 3
    if day == "Friday" or day == "friday":
        return 4
    if day == "Saturday" or day == "saturday":
        return 5
    if day == "Sunday" or day == "sunday":
        return 6


def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.client('dynamodb')
    daynum = getDayNum(str(event["day"]))
    d = datetime.datetime.today()
    scheduleDate = next_weekday(d, daynum)  # 0 = Monday, 1=Tuesday, 2=Wednesday...
    # print(next_monday)
    print(scheduleDate)
    item = dynamodb.put_item(TableName='scheduled_services',
                             Item={
                                 'trackingID': {'S': event["id"].replace("\"", "")},
                                 'city': {'S': event["city"]},
                                 'branch': {'S': event["branch"]},
                                 'date': {'S': str(scheduleDate)},
                                 'dateCreated': {'S': str(datetime.datetime.today())},
                                 'phoneNumber': {'S': event["phoneNumber"]}
                             })
    item2 = dynamodb.put_item(TableName='shipment',
                              Item={
                                  'tracking_id': {'S': event["id"].replace("\"", "")},
                                  'location': {'S': event["city"]},
                                  'status': {'S': str('Open')}
                              })

    return item
