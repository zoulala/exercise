#coding=utf8

'''

测试天气api:http://www.sojson.com/open/api/weather/json.shtml?city=北京
'''


import requests


# get weather html and parse to json
city = '北京'
url = 'http://www.sojson.com/open/api/weather/json.shtml'
try:
    response = requests.get(url=url, params={'city': city})
    text = response.json()
    print(text['data'])
except:
    print('error')


