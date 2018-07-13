
# 两种post请求方式，发送json格式数据

import json,requests
from urllib import request

host='10.12.28.144'
# host="localhost"


def create(robotId):
    url = 'http://%s:9999/v1/rpc/robot-ai/create' % host

    s = {'id': robotId, 'name': '小游','sex':0,'industryId':2001,'industryName':'游戏','tenantId':100}

    # 将python对象转为json字符串，并转为bytes格式
    sj = json.dumps(s).encode(encoding='utf-8')  # python2.7则：sj = json.dumps(s)
    print(sj)

    headers = {'Content-Type': 'application/json'}  # 指明用json方式发送数据
    ggr = request.Request(url=url,headers=headers,data=sj)  # py3版本中data不能是字符串，需要转为bytes格式
    ggr = request.urlopen(ggr)
    gj = ggr.read()
    print(gj)

    # 将json格式数据转为python对象
    gs = str(gj, encoding='utf-8')
    g = json.loads(gs)
    print (g)


def realte(robotId):
    url= 'http://%s:9999/v1/rpc/robot-ai/lib/relate/'%host+str(robotId)

    s = {'SCENE': [36,37],'PUBLIC':[130]}
    sj = json.dumps(s)#.encode(encoding='utf-8')  # 可转为bytes格式，也可不转
    print(sj)

    headers = {'Content-Type': 'application/json'}  # 指明用json方式发送数据
    g = requests.post(url, data=sj, headers=headers)  # data可以是str 也可以是 bytes
    print(g.text)

def answer(robotId,ques,ask):
    url= 'http://%s:9999/v1/rpc/robot-ai/answer'%host +'?ask='+str(ask)

    s = {'robotId': robotId,'sessionId':202,'content':ques ,'first':0,'tenantId':1008}
    sj = json.dumps(s).encode(encoding='utf-8')  # 可转为bytes格式，也可不转
    print(sj)

    headers = {'Content-Type': 'application/json'}  # 指明用json方式发送数据
    g = requests.post(url, data=sj, headers=headers)  # data可以是str 也可以是 bytes

    print(g.text)  # 获得返回的数据
    ans = json.loads(g.text)  # 将返回的json数据 转为Python对象
    print(ans)

def endanswer(robotId):
    url= 'http://%s:9999/v1/rpc/robot-ai/answer/end' % host
    s = {'robotId': robotId,'sessionId':202,'tenantId':100}

    sj = json.dumps(s)  # .encode(encoding='utf-8')
    print(sj)

    headers = {'Content-Type': 'application/json'}  # 指明用json方式发送数据
    g = requests.post(url, data=sj, headers=headers)  # data可以是str 也可以是 bytes
    print(g.text)

def tag(robotId):
    url = 'http://%s:9999/v1/rpc/robot-ai/lib/question/tag' % host
    s = {'tenantId': robotId,  'question': '我是第一个问题'}
    sj = json.dumps(s)  # .encode(encoding='utf-8')
    print(sj)
    g = requests.post(url, json=sj)
    print(g.text)

def simu_ans(robotId,ques):
    url = 'http://%s:9999/v1/rpc/robot-ai/simulate_answer' % host

    s = {'robotId': robotId, 'content': ques, 'first': 0, 'tenantId': 1008}
    sj = json.dumps(s).encode(encoding='utf-8')  # 可转为bytes格式，也可不转
    print(sj)

    headers = {'Content-Type': 'application/json'}  # 指明用json方式发送数据
    g = requests.post(url, data=sj, headers=headers)  # data可以是str 也可以是 bytes

    print(g.text)  # 获得返回的数据
    ans = json.loads(g.text)  # 将返回的json数据 转为Python对象
    print(ans)

robotId = 92
# create(robotId)
# realte(robotId)
answer(robotId,'去掉',1)
# endanswer(robotId)
# tag(robotId)
# simu_ans(robotId,'游戏')

# import time
# k = 0
# while True:
#     k += 1
#     time.sleep(0.01)
#     answer(robotId,'说说说',0)
#     if k>6:
#         break
# answer(robotId, '说说说', 1)

# http='10.12.0.34:8880'
#
# # url = "http://10.12.28.223:8880/v1/rpc/robot-ms/robot/robot-data/"+"26"
# # url = "http://10.12.0.34:8880/v1/rpc/robot-ms/robot/robot-lib/"+"1001"
# url = 'http://10.12.0.34:8877/v1/rpc/uaa/tenant/list'
#
# ggr = request.Request(url=url)
# ggr = request.urlopen(ggr)
# ggr = ggr.read()
# print(ggr)
# ggr = str(ggr, encoding='utf-8')
# ggr = json.loads(ggr)
# print(ggr)
# robot_list = ggr['data']
# robotId_list = [robot['id'] for robot in robot_list]
#
# print(robotId_list)



