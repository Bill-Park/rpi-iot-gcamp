import sys
import requests
import json

client_id = "Client ID"
client_secret = "Client Secret"
lang = "Kor" # 언어 코드 ( Kor, Jpn, Eng, Chn )
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang

def main(file_name) :

    data = open(file_name, 'rb')
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
        "Content-Type": "application/octet-stream"
    }
    response = requests.post(url,  data=data, headers=headers)
    rescode = response.status_code

    if(rescode == 200):
        #print (response.text)
        return_text = json.loads(response.text)["text"]
    else:
        #print("Error : " + response.text)
        return_text = "Error: " + response.text

    return return_text

if __name__ == "__main__" :
    return_text = main("output.mp3")
    print(return_text)
