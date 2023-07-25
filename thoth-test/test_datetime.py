#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     test_datetime.py
# author:   zlw2008ok@126.com
# date:     2022/9/19
# desc:     
#
# cmd>e.g.:  
# *****************************************************



import datetime


def getYesterday():

    today=datetime.date.today()
    # date = datetime.datetime.strftime(today, "%Y%m%d")
    # temp2 = today - datetime.timedelta(days=1)
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    yesterday = datetime.datetime.strftime(yesterday, "%Y%m%d")
    return yesterday

def getSomeday(n):

    today=datetime.date.today()
    somedays = [datetime.timedelta(days=i) for i in range(n,0,-1)]
    dates = [datetime.datetime.strftime(today-oneday, "%Y%m%d") for oneday in somedays]
    return dates



def getStartday(date):
    # date = '20191216'
    start_date = datetime.datetime.strptime(date, "%Y%m%d").date()
    today = datetime.date.today()
    n = (today-start_date).days
    somedays = [datetime.timedelta(days=i) for i in range(n,0,-1)]
    dates = [datetime.datetime.strftime(today-oneday, "%Y%m%d") for oneday in somedays]
    return dates


today=datetime.date.today()
gapday=datetime.timedelta(days=5000)
oneday=today-gapday
print(oneday)


gapday = today-oneday
gapday_num = gapday.days  #
print(gapday_num)
print(type(gapday_num))
