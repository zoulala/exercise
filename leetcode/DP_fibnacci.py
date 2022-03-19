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
