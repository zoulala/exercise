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


# sub高级替换
pattren= "^(.*?):(.*)$"
content = """
code:34
id:305
text:科室下进行观察
"""
for line in content.splitlines():
    print(re.sub(pattren,'\"\\1\":\"\\2\"',line))  # 批量增加引号
