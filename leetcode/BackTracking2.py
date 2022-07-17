#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     BackTracking2.py
# author:   zlw2008ok@126.com
# date:     2022/4/22
# description:    递归实现多级for循环
#
# cmd>e.g.:  
# *****************************************************
"""
写一个方法实现多个列表之间元素所有组合情况，按列表前后顺序组合。
如 输入data = [[1,2,3],[4,5],[6,7,8,9]]，
输出  [[1,4,6],[1,4,7],[1,4,8],[1,4,9],[1,5,6],[1,5,7], ...[3,5,9]]

"""

def for0(data, res):
    '''多级for循环
    存在问题：n为变量情况无法实现；书写复杂
    '''
    n = len(data)
    temp = []
    for a in data[0]:
        temp.append(a)
        for b in data[1]:
            temp.append(b)
            for c in data[2]:
                temp.append(c)
                for d in data[3]:
                    temp.append(d)
                    res.append(temp)
                    temp.pop()
                temp.pop()
            temp.pop()
        temp.pop()


#  递归实现
def recur(data, res,i, n):

    if i==n:
        print(res)
        return
    alist = data[i]
    for a in alist:
        res.append(a)
        i += 1
        recur(data, res, i, n)
        res.pop()
        i -=1


data = [[1,2,3],[5,6,7],[8,9,0]]
res = []
recur(data, res, 0, 3)

# 第三方库

import itertools

data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
a = list(itertools.product(*data))
print(a)
