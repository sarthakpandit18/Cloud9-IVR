import os
import json

import requests


def ivr_options():
    url = "https://a2d5ovfqj7.execute-api.us-east-1.amazonaws.com/dev/getoptions"
    response = requests.get(url)
    return response.text




