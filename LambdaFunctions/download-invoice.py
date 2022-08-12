import json
import boto3
from fpdf import FPDF
import os
import urllib3

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    pdf = FPDF()
    tracking_id = event["tracking_id"]

    pdf.add_page()
    # set style and size of font
    # that you want in the pdf
    pdf.set_font("Arial", size=15)

    options = dynamodb.Table('scheduled_services').scan()
    data = options['Items']
    for d in data:

        if d["trackingID"] == str(tracking_id):
            # create a cell
            pdf.cell(200, 10, txt=d["trackingID"],
                     ln=1, align='C')
            pdf.cell(200, 10, txt=d["branch"],
                     ln=2, align='L')
            pdf.cell(200, 10, txt=d["city"],
                     ln=3, align='L'),
            pdf.cell(200, 10, txt=d["date"],
                     ln=4, align='L')
            mobile_number = d["phoneNumber"]

    # save the pdf with name .pdf
    fileName = "/tmp/" + tracking_id + "_invoice.pdf"
    newName = tracking_id + "_invoice.pdf"
    pdf.output(fileName)
    # bucket = s3.Object('b00905274-assignment3', 'store_data.txt')
    file = pdf
    s3.upload_file(fileName, 'cloud9-invoices', newName)
    # Testing whether file is generating
    lst = os.listdir("/tmp")
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': 'cloud9-invoices',
            'Key': lst[0]
        }
    )
    payload = json.dumps({
        "mobile_number": mobile_number,
        "s3_uri": url
    })
    print(url)
    http = urllib3.PoolManager()

    # response = http.request('POST', 'https://a2d5ovfqj7.execute-api.us-east-1.amazonaws.com/dev/sendinvoice', body=payload)
    # print(response.status)
    # response = requests.post("https://a2d5ovfqj7.execute-api.us-east-1.amazonaws.com/dev/sendinvoice", data = json.dumps(payload))
    return payload

