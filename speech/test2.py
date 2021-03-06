#!/usr/bin/env python3
# coding: utf-8

import urllib.request
import urllib
import json
import base64
import  os

#设置应用信息
baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
grant_type = "client_credentials"
client_id = "SrhYKqzl3SE1URnAEuZ0FKdT"
client_secret = "hGqeCkaMPb0ELMqtRGc2VjWdmjo7T89d"

#合成请求token的URL
url = baidu_server+"grant_type="+grant_type+"&client_id="+client_id+"&client_secret="+client_secret

#获取token
res = urllib.request.urlopen(url).read().decode()
data = json.loads(res)
token = data["access_token"]
print (token)

#设置音频属性，根据百度的要求，采样率必须为8000，压缩格式支持pcm（不压缩）、wav、opus、speex、amr
VOICE_RATE = 16000
WAVE_FILE = "23.wav" #音频文件的路径
USER_ID = "hail_hydra" #用于标识的ID，可以随意设置
WAVE_TYPE = "wav"

#打开音频文件，并进行编码
f = open(WAVE_FILE, "rb")
fr = f.read()
speech = base64.b64encode(fr).decode()
size = os.path.getsize(WAVE_FILE)
update = json.dumps({"format":WAVE_TYPE, "rate":VOICE_RATE, 'channel':1,'cuid':USER_ID,'token':token,'speech':speech,'len':size})
update = update.encode(encoding="utf-8")#string to bytes
headers = { 'Content-Type' : 'application/json' }
url = "http://vop.baidu.com/server_api"
req = urllib.request.Request(url, update, headers)

r = urllib.request.urlopen(req)


t = r.read().decode()# bytes to string
result = json.loads(t)
print (result)
if result['err_msg']=='success.':
    word = result['result'][0].encode('utf-8')
    if word!='':
        if word[len(word)-3:len(word)]=='，':
            print (word[0:len(word)-3])
        else:
            print (word)
    else:
        print ("音频文件不存在或格式错误")
else:
    print ("错误")