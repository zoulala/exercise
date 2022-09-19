#!/usr/bin/python
# -*- coding: utf8 -*-
#
# *****************************************************
#
# file:     base_test_01.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2019-10-28
# brief:    https://www.pypandas.cn/docs/getting_started/10min.html#合并-merge
#
# cmd>e.g:  
# *****************************************************

import numpy as np
import pandas as pd

filename = '北京-省控线.csv'

data = pd.read_csv(filename, encoding='gbk')

# data = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
#                           'foo', 'bar', 'foo', 'foo'],
#                     'B': ['one', 'one', 'two', 'three',
#                           'two', 'two', 'one', 'three'],
#                     'C': np.random.randn(8),
#                     'D': np.random.randn(8)})



'''基本信息'''
print(data)  # 所有数据
print(data.head(3))  # 头几行
print(data.tail(2))  # 尾部几行
print(data.dtypes)  # 字段类型
print(data.index)  # 索引
print(data.columns)  # 列
print(data.to_numpy())  # numpy
print(data.describe())  # 对数值类型统计信息
print(data.T)  # 转置

'''排序'''
print(data.sort_index(axis=1, ascending=False))  # 按轴排序
print(data.sort_values(by='省控分数线'))  # 按轴排序

'''选择'''
print(data.省控分数线)  # data['省控分数线']  # 选择一个列
print(data[0:3])  # 切片
print(data.loc[1])  # 通过标签获取数据
print(data.loc[1:5, ['省控分数线','考生类别名称']])  # 通过标签在多个轴上选择数据
print(data.iloc[0:5, 0:2])  # 通过整数获取数据，类似于numpy
print(data.iloc[[1, 2, 4], [0, 2]])  # 通过整数的列表按位置切片
print(data.at[1,'省控分数线'])  # 快速访问标量
print(data.iat[1,1])  # 快速访问标量
print(data[data.省控分数线 > 500])  # 使用单个列的值来选择数据
# print(data[data>0]) # 从满足布尔条件的DataFrame中选择值, 数值型可用
print(data[data['考生类别名称'].isin(['理科', '文科'])])  #使用 isin() 方法过滤
print(data[(data.考生类别名称=='理科') & (data.录取批次名称.isin(['本科一批','本科二批','本科三批']))])  # 组合过滤

'''遍历'''
for a,b in zip(data["省控分数线"],data["考生类别名称"]):  #
    pass
for row in data.itertuples():  # 按照行, 通过 row[name] 对元素进行访问
    print(getattr(row, '省控分数线'), getattr(row, '考生类别名称'))
for index,row in data.iterrows():  # 按照行, 通过 row[name] 对元素进行访问
    print(row['省控分数线'], row['考生类别名称'])
for _idx,col in data.items():  # 按照列进行, 通过 row[index] 对元素进行访问
    print(_idx,col)
for index, row in data.iteritems():   # 按照列进行, 通过 row[index] 对元素进行访问
    print(index,row[0],row[1],row[2],row[3]) # index为列名