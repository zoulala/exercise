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