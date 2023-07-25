#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     json_test2.py
# author:   zlw2008ok@126.com
# date:     2023/7/17
# desc:     读取json大文件，防止内存不足问题
#
# cmd>e.g.:  
# *****************************************************

import json
def read_large_json(filename):
    with open(filename) as file:
        line = file.readline()
        line = file.readline()
        json_decoder = json.JSONDecoder()
        buffer = ''
        for line in file:
            buffer += line.strip()
            try:
                while buffer:
                    result, index = json_decoder.raw_decode(buffer)
                    yield result
                    buffer = buffer[index:].lstrip().lstrip(',')
            except ValueError:
                # 如果当前缓冲区不是一个完整的JSON对象，则继续读取下一行。
                pass

datas = read_large_json('/Users/zlw/Documents/5-词表知识/术语词表集/各中心/京煤/t_dwd_emr_doc_t.json')

for data in datas:
    print(data)