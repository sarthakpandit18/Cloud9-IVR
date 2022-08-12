import json
import os


def get_ngrok_link():
    os.system("ngrok http 8000 &>/dev/null &")
    os.system("curl  http://44.197.101.54:4040/api/tunnels > tunnels.json")

    with open('tunnels.json') as data_file:
        datajson = json.load(data_file)

    msg = ""
    # print(datajson['tunnels'])
    for i in datajson['tunnels']:
        # print (i)
        msg = i['public_url']
    print(msg)
    return msg


# print (msg+"1")

if __name__ == "__main__":
    get_ngrok_link()
