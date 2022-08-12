import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    schedule = dynamodb.Table('scheduled_services').scan()
    data = schedule['Items']
    length = len(data)
    allShipments = []
    for d in data:
        print(type(d))
        id = d.get('trackingID')
        branch = d.get('branch')
        city = d.get('city')
        date = d.get('date')
        print("scheduled_id : " + str(id))
        shipmentTable = dynamodb.Table('shipment').scan()
        shipmentTableData = shipmentTable['Items']

        for d1 in shipmentTableData:
            shipment_id = d1.get('tracking_id')
            location = d1.get('location')
            status = d1.get('status')
            if shipment_id == id:
                shipment = {
                    "trackingID": shipment_id,
                    "pickupCity": city,
                    "pickupBranch": branch,
                    "date": date,
                    "currentLocation": location,
                    "status": status
                }
                allShipments.append(shipment)
                print(" id : " + str(shipment_id) + ", status= " + str(d1.get('location')))
    print(allShipments)
    return allShipments




