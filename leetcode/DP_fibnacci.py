#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     DP_fibnacci.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-09-20
# brief:    
#
# cmd>e.g:  
# *****************************************************

""""
计算斐波那契数列：Fn = Fn-1+Fn-2  (n=1,2  fib(1)=fib(2)=1)

"""
import numpy as np
# 递归方法
def fibnacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibnacci(n-1)+fibnacci(n-2)


# 动态规划方法
def dp_fibnacci(n):
    if n<=0:
        return 0

    dp = np.zeros(n+1)

    dp[0]=0
    dp[1]=1
    dp[2]=1
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]

    return dp[n]


# dp状态压缩
#我们发现每次状态转移只需要 DP table 中的一部分，那么可以尝试用状态压缩来缩小 DP table 的大小，只记录必要的数据，上述例子就相当于把DP table 的大小从 n 缩小到 2。

def dp_fibnacci_com(n):
    if n<=0:
        return 0
    if n==1 or n==2:
        return 1

    d1=1
    d2=1
    _sum = 0
    for i in range(3,n+1):
        _sum = d1+d2
        d1 = d2
        d2 = _sum
    return _sum

res= fibnacci(10)
print(res)
res= dp_fibnacci(10)
print(res)
res= dp_fibnacci_com(10)
print(res)
