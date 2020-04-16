#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     a_stock_simulate.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-04-16
# brief:    看了一个操盘策略，用公式进行模拟。https://www.toutiao.com/i6815418938378158606
#
# cmd>e.g:  
# *****************************************************

import random

money = 100000.  # 总价
p_num = 5.
loss_k = 0.1  # 止损率
add_k = 0.2  # 止赢率
prob = 0.5  # 股票上涨概率(止赢概率)  该参数完全体现个人水平，影响最终结果走势

profit = 0.  # 每一步利润
inps = 20000.  # 初始入金
a_part = money/p_num  # 每操作单元


def make_a_deal(inps,money,max_step=10):
    '''进行一笔交易
    inps:入仓额
    money:手上总额
    max_step:最大交易次数
    '''
    print(max_step,inps, money)

    money -= inps  # 入仓
    outs = 0

    # 交易终止条件
    if money<0:
        return outs
    if max_step<1:
        return outs

    # 开始交易
    max_step -= 1  # 交易次数减少一次
    rd = random.random()  # 0～1随机数
    if rd < prob:
        profit = add_k*inps  # 止赢
    else:
        profit = -loss_k*inps  # 止损
    outs = inps+profit  # 出仓
    money += outs

    if outs > inps:
        inps += a_part  # 止赢就加大一码入仓
        if inps>money:  # 入仓额度>总价，则不加码
            inps -= a_part
        outs = make_a_deal(inps, money,max_step)  # 继续交易
    else:
        inps -= a_part  # 止损就加减一码入仓
        if inps<a_part:  # 入仓额度最少为一码
            inps = a_part
        outs = make_a_deal(inps, money,max_step)  # 继续交易

    return outs


def make_a_deal2(inps,money,target=200000,step=0):
    '''进行一笔交易
    inps:入仓额
    money:手上总额
    target:目标额
    step:交易次数
    '''
    print('交易%s次，入仓%s，总额%s'%(step,inps, money))

    # 交易终止条件
    if money<0 or money>target:
        return 0

    # 开始交易
    money -= inps  # 入仓
    step += 1  # 交易次数减少一次
    rd = random.random()  # 0～1随机数
    if rd < prob:
        profit = add_k*inps  # 止赢
    else:
        profit = -loss_k*inps  # 止损
    outs = inps+profit  # 出仓
    money += outs

    if outs > inps:
        inps += a_part  # 止赢就加大一码入仓
        if inps>money:  # 入仓额度>总价，则不加码
            inps -= a_part
        outs = make_a_deal2(inps, money,target,step=step)  # 继续交易
    else:
        inps -= a_part  # 止损就加减一码入仓
        if inps<a_part:  # 入仓额度最少为一码
            inps = a_part
        outs = make_a_deal2(inps, money,target,step=step)  # 继续交易

    return outs


# make_a_deal(inps,money,max_step=100)
make_a_deal2(inps,money,200000,0)








