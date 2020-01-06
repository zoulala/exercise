#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     url_encode_decode.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-01-05
# brief:    url 编码解码：
#
# cmd>e.g:  
# *****************************************************

from urllib import parse
import json

print(parse.quote("http://192.168.10.105:8080/media/activities/上海/ad/1515043837.jpg"))

print(parse.unquote('http://192.168.10.105:8080/media/activities/%E4%B8%8A%E6%B5%B7/ad/1515043837.jpg'))



aaa = '{"time":1577671457285,"alias":"zsys","scene":1017,"platform":"wxsp","client":"wx_zsys","xfr":"pages/home/index","unionid":"o7w1PuOKcLTIiub71Qpk_G4d3VRc","openid":"oqHf50KTQUVAesHogLgVEotmo0-M","session_key":"lwp8hX/KWWeh/Y4ZOZUkdA==","username":"张杰","storage_id":323537,"user_id":"657eb88a7d6cea06501f5e0f85448698","sor_mark_id":"o7w1PuOKcLTIiub71Qpk_G4d3VRc","is_new":0,"phone":"13581560096","auth_code":"GsfbgoMtMzDRdcmqMxpNyBaOIXhFnLHJ","userid":323537,"page":"pages/commonWebview/index","name":"commonWebview","title":"左手医生","web_h5_url":"https%3A%2F%2Fweb.zuoshouyisheng.com%2Frecommend%3Fid%3D808083e9512d9ee8aa717eed396e45a4%26user_id%3D323537%26xfr%3D%25E5%25B7%25A6%25E6%2589%258B%25E5%258C%25BB%25E7%2594%259F%25E5%25B0%258F%25E7%25A8%258B%25E5%25BA%258F%25E9%25A6%2596%25E9%25A1%25B5%26user_id%3D323537%26auth_code%3DGsfbgoMtMzDRdcmqMxpNyBaOIXhFnLHJ%26logParams%3D%7B%22tr-action-source%22%3A%22go-guess-like-button%22%7D"}'

bbb = json.loads(aaa)
ccc = bbb.get('web_h5_url')
print(ccc)
print(parse.unquote(ccc))

ddd = parse.unquote(ccc)
print(parse.unquote(ddd))


import requests
filename = 'http://211.154.163.104/hb2-vpc-92/info.log.20191228'
r = requests.get(filename, stream=True)
data = r.iter_lines(chunk_size=10, delimiter=b"\n")
for line in data:
    print(line)