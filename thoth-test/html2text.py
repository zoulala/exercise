#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     html2text.py
# author:   zlw2008ok@126.com
# date:     2023/2/16
# desc:     
#
# cmd>e.g.:  
# *****************************************************
#python去除html标签的几种方法

import re
from bs4 import BeautifulSoup
from lxml import etree

html = '<p>你好</p><br/><font>哈哈</font><b>大家好</b>'

# 方法一
pattern = re.compile(r'<[^>]+>', re.S)
result = pattern.sub('', html)
print(result)


# 方法二
soup = BeautifulSoup(html, 'html.parser')
print(soup.get_text())

# 方法三
response = etree.HTML(text=html)
# print(dir(response))
print(response.xpath('string(.)'))