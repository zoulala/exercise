#!/usr/bin/python
# -*- coding: utf8 -*-
#
# *****************************************************
#
# file:     elasticsearch_test.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2019-10-10
# brief:    
#
# cmd>e.g:  
# *****************************************************


from elasticsearch import Elasticsearch


es = Elasticsearch(hosts=['211.154.163.97',], port='9200', timeout=25)


# 删除索引(库)
result = es.indices.delete(index='actest', ignore=[400, 404])
print(result)

# 创建索引(库)
result = es.indices.create(index='actest',ignore=400)
print(result)


# 插入数据
data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm'}
result = es.create(index='actest', doc_type='politics', id=1, body=data)
# result = es.index(index='actest', doc_type='politics', body=data)  # index方法创建文档无需指定id
print(result)

# 更新数据
data = {'title': '美国留给伊拉克的是个烂摊子吗', 'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm', 'date': '2011-12-16','status':0}
result = es.update(index='actest', doc_type='politics', body={'doc':data},id=1)  # .update更新数据时body需要外包一层'doc'
# result = es.index(index='actest', doc_type='politics', body=data, id=1)
print(result)

# 删除数据
result = es.delete(index='actest', doc_type='politics', id=1)
print(result)

# 查询
result = es.search(index='actest', doc_type='politics')
print(result)

dsl = {'query':{'match':{'title':'美国'}}}
result = es.search(index='actest', doc_type='politics', body=dsl)

