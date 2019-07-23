import os
import sys
import requests
import json

client_id = "Client ID"
client_secret = "Client Secret"

url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"

def main(tts_text, file_name = "input.mp3") :

    datas = {
        "speaker" : "mijin",
        "speed" : "0",
        "text" : tts_text
    }

    headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_secret,
            "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=datas, headers=headers)

    with open(file_name, 'wb') as f:
        f.write(response.content)

    return file_name

if __name__ == "__main__" :
    file_name = main("안녕하세요 Gcamp")
    os.system("mpg123 {}".format(file_name))
