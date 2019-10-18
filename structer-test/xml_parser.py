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

sf = open('partment.txt','w')
n = 1
path = '门诊病历导出数据'

files = os.listdir(path)
for file in files:
    filename = os.path.join(path,file)
    text = ''
    with open(filename, 'r') as f:
        try:
            for line in f:

                dic_data = xmltodict.parse(line)

                for base_key in dic_data:

                    for code_key in dic_data[base_key]:
                        element_line = dic_data[base_key][code_key]
                        if '@value' in element_line and element_line['@value']:
                            key = element_line['@dataelementName'].split()[-1]
                            value = element_line['@value']
                            # print(key,' : ',value)
                            text += key+':'+value+'\t'
        except:
            continue

    if text:
        n += 1
        print(text)
        sf.write(text+'\n')
sf.close()
print(n)




