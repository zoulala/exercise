#coding=utf-8

#练习re正则表达式
#reference:http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832260566c26442c671fa489ebc6fe85badda25cd000
#http://www.runoob.com/python/python-reg-expressions.html

import re


# 零宽断言
pattern='(?<=\d)[\u4e00-\u9fa5]+'  # 零宽断言(?<=exp)， 左边为数字的汉字
content = "56咳嗽a可3"
print(re.findall(pattern,content))

pattern='(?<!\d)[\u4e00-\u9fa5]+'  # 零宽断言(?<!exp)，左边不为数字的汉字
content = "56咳嗽a可3"
print(re.findall(pattern,content))

pattern='[\u4e00-\u9fa5]+(?=\d)'  # 零宽断言(?=exp)，右边为数字的汉字
content = "56咳嗽a可3"
print(re.findall(pattern,content))

pattern='[\u4e00-\u9fa5]+(?!\d)'  # 零宽断言(?!exp)，右边不为数字的汉字
content = "56咳嗽a可3"
print(re.findall(pattern,content))



# 循环匹配
pattren= "(?:(?!死|亡|原因)[\u4e00-\u9fa5])+"   # 匹配汉字，但不匹配特定汉字:死|亡|原因
content = "ajr死啊啊人原因来人啊qer咳嗽"
print(re.findall(pattren,content))

# 左侧最近的字符匹配
pattren = "b[^b]*aa"  # 实现匹配关键词"aa"左侧最近的字符"b"
aa = '{"a": "bc","b":"abc"de"fg", "f":"fallll"}'
output_str = re.sub(r'(?<=[^, :}{])"(?=[^, :}{])', '', aa)  # 删除非json格式双引号

# 实现关键词"aa"前面8个字符内未出现关键词"bb"
pattern = r'^(?!.*bb.{0,7}aa).*aa'
text1 = 'aaccddbbddaa'  # 匹配失败，因为前面8个字符内有bb
text2 = 'aaccddaa'  # 匹配成功，因为前面8个字符内没有bb
match1 = re.match(pattern, text1)
match2 = re.match(pattern, text2)
print(match1)  # None
print(match2)  # <re.Match object; span=(0, 8), match='aaccddaa'>
'''
解释一下正则表达式：
^ 表示匹配字符串的开头。
(?!.*bb.{0,7}aa) 使用零宽度负预测先行断言，表示后面不能匹配任意数量的任意字符、"bb"以及0到7个任意字符，然后再匹配"aa"。
.*aa 匹配任意数量的任意字符，直到最后一个"aa"。
因此，这个正则表达式会匹配前面8个字符内没有"bb"的字符串，并且最后一个"aa"是整个字符串的最后一个"aa"。
'''

# sub高级替换
pattren= "^(.*?):(.*)$"
content = """
code:34
id:305
text:科室下进行观察
"""
for line in content.splitlines():
    print(re.sub(pattren,'\"\\1\":\"\\2\"',line))  # 批量增加引号

a = re.sub('([^\d]1\d{6})\d{4}([^\d])',r'\1****\2','b18501371234a')  # 变量
b = re.sub('([^\d]1\d{6})\d{4}([^\d])','\\1****\\2','b18501371234a')  # 变量
c = re.sub('(?<=[^\d]1\d{6})\d{4}(?=[^\d])','****','b18501371234a')  # 零宽断言
print(a)
print(b)
print(c)
exit()
