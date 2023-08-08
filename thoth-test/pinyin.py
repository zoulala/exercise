#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     pinyin.py
# author:   zlw2008ok@126.com
# date:     2023/8/1
# desc:     拼音
#
# cmd>e.g.:  
# *****************************************************

import sys
import re
import pypinyin

word = 'abc(（）,，～|可法'
# chws = re.findall('[\u4E00-\u9FD5]',word)
# word = ''.join(chws)
wps = pypinyin.pinyin(word, style=pypinyin.NORMAL)  # heteronym=True 带声调
hh = ''.join([wp[0].upper()[0] for wp in wps])
print(wps)
print(hh)

import re
import sys
import pypinyin
while True:
    word = sys.stdin.readline()
    if not word:break
    word = word.strip()
    chws = re.findall('[\u4E00-\u9FD5]',word)
    if not chws:
        word = word[0].upper()
    else:
        word = ''.join(chws)

    wps = pypinyin.pinyin(word, style=pypinyin.NORMAL)  # heteronym=True 带声调
    hh = ''.join([wp[0].upper()[0] for wp in wps])
    sys.stdout.write(hh+'\n')




