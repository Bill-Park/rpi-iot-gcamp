import requests
import json
api_key = "dd40631e0b2c53fdc84e1dffd1da95f6"
url = "http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={key}".format(key=api_key)

def main() :
    res = requests.get(url)
    res_json = json.loads(res.text)
    temperature = round(res_json["main"]["temp"] - 273, 1)
    humidity = round(res_json["main"]["humidity"])
    return temperature, humidity


if __name__ == "__main__" :
    temp, humi = main()
    print(temp)
    print(humi)
