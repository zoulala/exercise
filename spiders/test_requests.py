'''请求库练习：requests'''

import requests

#   -------------------requests --------------------------

url='https://httpbin.org/ip'
res = requests.get(url)
print(dir(res))
print(res.headers)
print(res.text)  # str类型
print(res.content)  # bytes类型， res.content.decode('utf8') = res.text

# get请求
url_get1 = 'https://httpbin.org/get'
data = {'param1': 'hello', 'param2': 'wrold'}
res = requests.get(url, params=data)
print(res.status_code)
print(res.reason)
print(res.headers)
print(res.text)  # str类型

# post请求
url = 'http://httpbin.org/post'
d = {'key1': 'value1', 'key2': 'value2'}
r = requests.post(url, data=d) # data可以是str 也可以是 bytes
print('post-----------')
print(r.text)



# --------------- 打开网页为大文件时（下载大json数据） --------

url = 'https://dataset-bj.cdn.bcebos.com/sked/dev_data.json'

sf = open('xxx/dev_extra.txt','w')

response = requests.get(url, stream=True)  # streamc参数按流下载，不会一次性下载。

for line in response.iter_lines():  # response.iter_content(chunk_size=512)
    if line:
        sf.write(line.decode('utf8')+'\n')
sf.close()

for chunk in response.iter_content(chunk_size=512):
    if chunk:
        print(chunk)


#
# data = response.text
# # js_data = json.loads(data)
#
# sf.write(data)
