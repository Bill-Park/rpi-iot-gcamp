import requests
from xml.etree import ElementTree

serviceKey = "Z9vuWBX1vbycgKOhb8zaQ%2FFAdiYe1IiQTxPL04nRhLPoLakrbl%2F6kdqe2%2F1EpeK1qPlQkdBu2yQjLlQH%2B0ZD%2Fg%3D%3D"
sido = "서울"
url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?sidoName={sido}&searchCondition=DAILY&pageNo=1&numOfRows=10&ServiceKey={key}".format(sido=sido, key=serviceKey)
headers = {'content-type' : 'application/json;charset=utf-8'}

res = requests.get(url, headers = headers)
tree = ElementTree.fromstring(res.text)

#print(res.text)
for child in tree.iter('item') :
    cityName = child.find('cityName').text
    pm10 = child.find('pm10Value').text
    pm25 = child.find('pm25Value').text

    print(cityName, pm10, pm25)