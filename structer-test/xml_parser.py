#!/usr/bin/python
# -*- coding: utf8 -*-
#
# *****************************************************
#
# file:     xml_parser.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2019-10-16
# brief:    xml格式数据解析
#
# cmd>e.g:  
# *****************************************************

import os
import xmltodict

sf = open('hospital.txt','w')
n = 1
path = 'hospital/23280840'

files = os.listdir(path)
for file in files:
    filename = os.path.join(path,file)
    text = ''
    with open(filename, 'r') as f:
        line = f.read()
        dic_data = xmltodict.parse(line)

        for base_key in dic_data:

            for code_key in dic_data[base_key]:
                element_line = dic_data[base_key][code_key]
                if '@displayName' in element_line:
                    print(element_line['@displayName'])
                if '@value' in element_line and element_line['@value']:
                    key = element_line['@dataelementName'].split()[-1]
                    value = element_line['@value']
                    # print(key,' : ',value)
                    text += '<'+key +'>'+ ':' + value + '\t'
        # try:
        #     for line in f:
        #
        #         dic_data = xmltodict.parse(line)
        #
        #         for base_key in dic_data:
        #
        #             for code_key in dic_data[base_key]:
        #                 element_line = dic_data[base_key][code_key]
        #                 if '@value' in element_line and element_line['@value']:
        #                     key = element_line['@dataelementName'].split()[-1]
        #                     value = element_line['@value']
        #                     # print(key,' : ',value)
        #                     text += key+':'+value+'\t'
        # except:
        #     continue

    if text:
        n += 1
        print(text)
        sf.write(text+'\n')
sf.close()
print(n)


import xmltodict
import json

# 打开 XML 文件并读取内容
with open('input.xml', 'r') as f:
    xml_content = f.read()

# 将 XML 转换为 OrderedDict 对象
xml_dict = xmltodict.parse(xml_content)

# 将 OrderedDict 对象转换为 JSON 字符串
json_str = json.dumps(xml_dict, indent=4)

# 将 JSON 字符串写入输出文件
with open('output.json', 'w') as f:
    f.write(json_str)


## ------------------Python内置的xml和json模块来将XML文件转换为JSON格式。下面是一个简单的示例代码：-------

import xml.etree.ElementTree as ET
import json

# 读取XML文件
tree = ET.parse('example.xml')
root = tree.getroot()

# 将XML转换为JSON
json_data = {}
for child in root:
    json_data[child.tag] = child.text

# 保存JSON文件
with open('example.json', 'w') as f:
    json.dump(json_data, f)

