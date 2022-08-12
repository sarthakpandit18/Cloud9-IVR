from twilio.rest import Client
from pyngrok import ngrok
import os
from decouple import config


def update_ngrok_url():
    url = ngrok.connect(8000).public_url
    print(' * Tunnel URL:', url)
    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    incoming_phone_numbers = client.incoming_phone_numbers.list(limit=20)

    for record in incoming_phone_numbers:
        print(record.friendly_name)
        if record.friendly_name == '(825) 251-9025':
            client.incoming_phone_numbers(record.sid).update(voice_url=url + '/shipping_ivr/welcome')


if __name__ == '__main__':
    update_ngrok_url()
