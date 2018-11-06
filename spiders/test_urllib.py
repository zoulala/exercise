'''请求库练习：urllib'''

# python3
from urllib import request,parse
# 简单测试
url = 'https://httpbin.org/ip'
html = request.urlopen(url=url,data=None,timeout=None,cafile=None,capath=None,cadefault=False,context=None)  # data:post提交数据，caxxx是身份验证参数
print(type(html))  # 查看返回的对象类型
print(dir(html))  # 查看对象包含的属性
print(html.code)  # 状态码
print(html.getcode())  # 获取状态码
print(html.headers)
print(html.geturl())
print(html.read())  # 结果bytes类型：b'{\n  "origin": "211.159.181.217"\n}\n'


# get请求
url = 'https://httpbin.org/get'
data = parse.urlencode({'param1': 'hello', 'param2': 'wrold'})
print(type(data))  # ‘param2=wrold&param1=hello’
new_url = '?'.join([url, '%s']) % data
new_url = request.Request(new_url)  # 不带data参数为get请求，该行可以忽略
res = request.urlopen(new_url)
print(res.info())  # =headers
print(res.read())  # bytes类型

# post请求
url = 'http://httpbin.org/post'
data = {'key1': 'value1', 'key2': 'value2'}
data = parse.urlencode(data).encode('utf-8')  # b'key1=value1&key2=value2'
req = request.Request(url, data=data)  #POST方法
r = request.urlopen(req)
print(dir(r))
print(r.read())  # bytes类型

