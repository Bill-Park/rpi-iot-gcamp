import requests
import json

serviceKey = "Z9vuWBX1vbycgKOhb8zaQ%2FFAdiYe1IiQTxPL04nRhLPoLakrbl%2F6kdqe2%2F1EpeK1qPlQkdBu2yQjLlQH%2B0ZD%2Fg%3D%3D"
sido = "서울"
url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?sidoName={sido}&searchCondition=DAILY&pageNo=1&numOfRows=10&ServiceKey={key}&_returnType=json".format(sido=sido, key=serviceKey)

headers = {'content-type' : 'application/json;charset=utf-8'}
res = requests.get(url, headers = headers)
#print(res.text)
res_json = json.loads(res.text)

for data in res_json["list"] :
    print(data["cityName"], data["pm10Value"], data["pm25Value"])

