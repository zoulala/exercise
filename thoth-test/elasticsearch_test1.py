#!/usr/bin/python
# -*- coding: utf8 -*-
#
# *****************************************************
#
# file:     elasticsearch_test1.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2019-10-10
# brief:    
#
# cmd>e.g:  
# *****************************************************

import json
from elasticsearch import Elasticsearch


es = Elasticsearch(hosts=['211.154.163.97',], port='9200', timeout=25)

# # 删除索引(库)
# result = es.indices.delete(index='actest', ignore=[400, 404])
# print(result)
#
# # 创建索引(库)
# result = es.indices.create(index='actest',ignore=400)
# print(result)
#
# mapping = {"dynamic":False,"properties":{"doc_id":{"type":"integer","index":False},"title":{"type":"text","index":False},"content":{"type":"text","index":False},"tags":{"type":"text","index":True}}}
#
# result = es.indices.put_mapping(index='actest', doc_type='personas', body=mapping)
# print(result)


# 插入数据
datas = [{'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm', 'date': '2011-12-16','status':0},
         {'title': '新中国可以', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm', 'date': '2011-12-16','status':0},
         {'title': '大师在流浪', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm', 'date': '2011-12-16','status':0},
         {'title': '小丑在天堂', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm', 'date': '2011-12-16','status':0},
         {'title': '美国和中国', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm', 'date': '2011-12-16','status':0}]

# for data in datas:
#     es.index(index='actest', doc_type='personas', body=data)

# 查询
# result = es.search(index='actest', doc_type='personas')
# print(result)

dsl = {'query':{'match':{'title':'美国'}}}
result = es.search(index='actest', doc_type='personas', body=dsl)

print(json.dumps(result, indent=2, ensure_ascii=False))

