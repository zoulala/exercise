#coding=utf-8

#练习re正则表达式
#reference:http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832260566c26442c671fa489ebc6fe85badda25cd000
#http://www.runoob.com/python/python-reg-expressions.html

import re



#match()使用------------------------------------------------------------------------------
'''match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。'''
print (u'\n\n\nmatch使用----------------')
if re.match(r'^\d{3}\-\d{3,8}$','010-12345'):
    print ('one')
if re.match(r'^\d{3}\s\d{3,8}$','010 12345'):
    print ('two')

test = u'用户输入的字符串'
if re.match(r'用户', test):
    print (u'起始开始yes')
if re.match(r'输入', test):
    print (u'中间开始no')

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print( m.groups(),m.group(0),m.group(1),m.group(2))


email = 'some.one@126.com'
mm = re.match(r'^([a-zA-z_-]+[a-zA-Z0-9_-]+\.?[0-9a-zA-z]+)@([0-9a-zA-Z]+)\.([a-zA-Z]{3})$', email)
m = re.match(r'^\w+\.?\w+\@\w+\.\w{3}', email)
if mm:
    print( u'邮箱书写正确')

line = "Cats are smarter than dogs"
ma = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
print (ma.groups())
	
#search()使用----------------------------------------------------------------------------------
'''re.search 扫描整个字符串并返回第一个成功的匹配。'''
print (u'\n\n\nsearch()使用--------------')
print (re.search('www','www.runoob.com').span())
print (re.search('com','www.runoob.com.com').span())
m = re.search('com','www.runoob.Com.cOm',re.I)# re.I 不分大小写
print (bool(m))

#检索和替换sub()使用---------------------------------------------------------------------------------
'''用于替换字符串中的匹配项
re.sub(pattern, repl, string, count=0, flags=0);repl可以是函数，count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配'''
print (u'\n\n\nsub()使用--------------')
phone = "2004-959-559 # 这是一个国外电话号码"
 
num = re.sub(r'#.*$', "", phone)# 删除字符串中的 Python注释 
print (u"电话号码是: ", num)
num = re.sub(r'\D', "", phone,0)# 删除非数字(-)的字符串 
print (u"电话号码是 : ", num)

def double(matched):# 将匹配的数字乘于 2
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))


#切分字符串---------------------------------------------------------------------------------
print (u'\n\n\n切分字符串--------------')
print ('a b   c'.split(' '))
print (re.split(r'\s+','a b   c'))
print (re.split(r'[\s|,\;]+','a,b c   d;m;;k , ;l'))

#编译-----------------------------------------------------------------------------------------
print (u'\n\n\n编译--------------')
re_t = re.compile(r'^(\d{3})-(\d{3,8})$')
m = re_t.match('010-12345')
print (m.groups())

# findall()--------------------------------------------------------------------------------
print ('\n\n\nfindall()用法')
s = 'aaa112bbb, 222ABaa, cccc333'
mk = re.findall(r'[a-z]+(\d+)[a-z]+', s)
print (mk)
print (re.findall(r'Ab',s,re.I))
print(re.findall(r'[a-z\d]+',s))
ss = '共 8 页,共 9 页'
ms = re.findall(r'共(.*?)页', ss)  # 最短匹配
print (ms)

# finditer()------------------------
offsets = []
results = re.finditer('共(.*?)页',ss)
for res in results:
    offsets.append(res.span())


datas = re.finditer('(\d+)(\w+)','afb123ga26')
# datas = re.finditer('(afb)','afb123ga26')
for d in datas:
    print(d.span())
    print(d.start(),d.end())
    print(d.group())
    print(d.groups())
    a = d.group()
    b = d.groups()
    bspan = d.regs[1]
    print(b)
    print(bspan)
    # groups() 为元组，代表多少个括号内容
    for i in range(len(d.groups())):
        a_group = d.groups()[i]
        a_span = d.regs[i+1]
        print(a_group,a_span)






