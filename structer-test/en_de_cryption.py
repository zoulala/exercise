#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     tst.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-01-02
# brief:    加密解密
#
# cmd>e.g:  
# *****************************************************

import re
import base64
import random



# maps = {'a':'M'}
#
# chars1 = []
# chars2 = []
#
# with open('tst.txt','r') as f:
#     for line in f:
#         line = line.strip()
#         if not line:continue
#         if line in chars1:
#             print('error')
#         chars1.append(line)
#         chars2.append(line)
# random.shuffle(chars2)
#
# print(chars1)
# print(chars2)
# print(dict(list(zip(chars1,chars2))))
# print(dict(list(zip(chars2,chars1))))
# map1 = dict(list(zip(chars1,chars2)))
# map2 = dict(list(zip(chars2,chars1)))
#

def encryption(content):
    # content = 'num days: 103'
    s1 = base64.encodebytes(content.encode('utf8'))
    s1 = s1.decode('utf8')
    s2 = ''
    for c in s1:
        s2 += map1.get(c,c)
    return s2

def decryption(content):
    s3 = ''
    for c in content:
        s3 += map2.get(c,c)
    s3 = base64.decodebytes(s3.encode('utf8'))
    out = s3.decode('utf8')
    return out


def encryption2(content):
    # content = 'num days: 103'
    s1 = base64.encodestring(content)
    # s1 = s1.decode('utf8')
    print s1
    s2 = ''
    for c in s1:
        s2 += map1.get(c,c)
    return s2

def decryption2(content):
    s3 = ''
    for c in content:
        s3 += map2.get(c,c)
    s3 = base64.decodestring(s3)
    return s3



map1 = {'+': 'G', '.': 'm', '1': 'p', '0': 'v', '3': 'B', '2': 'l', '5': '.', '4': 'E', '7': ':', '6': '5', '9': '<', '8': '1', ':': 'u', '=': '?', '<': 'A', '?': '8', '>': 'k', 'A': 'w', 'C': 'Z', 'B': 'r', 'E': 'e', 'D': 'c', 'G': 'R', 'F': 'W', 'I': 'a', 'H': 't', 'K': 'V', 'J': 'Y', 'M': 'y', 'L': 'o', 'O': 'j', 'N': 'h', 'Q': 'q', 'P': 'T', 'S': 'P', 'R': '9', 'U': 'D', 'T': 'C', 'W': 's', 'V': 'g', 'Y': 'N', 'X': 'O', 'Z': 'n', 'a': '2', 'c': 'S', 'b': 'Q', 'e': '6', 'd': '4', 'g': 'f', 'f': 'K', 'i': 'H', 'h': 'b', 'k': 'J', 'j': 'L', 'm': '0', 'l': 'x', 'o': 'd', 'n': 'z', 'q': 'I', 'p': 'M', 's': 'F', 'r': '7', 'u': '3', 't': '=', 'w': 'U', 'v': 'X', 'y': 'i', 'x': '+', 'z': '>'}
map2 = {'+': 'x', '.': '5', '1': '8', '0': 'm', '3': 'u', '2': 'a', '5': '6', '4': 'd', '7': 'r', '6': 'e', '9': 'R', '8': '?', ':': '7', '=': 't', '<': '9', '?': '=', '>': 'z', 'A': '<', 'C': 'T', 'B': '3', 'E': '4', 'D': 'U', 'G': '+', 'F': 's', 'I': 'q', 'H': 'i', 'K': 'f', 'J': 'k', 'M': 'p', 'L': 'j', 'O': 'X', 'N': 'Y', 'Q': 'b', 'P': 'S', 'S': 'c', 'R': 'G', 'U': 'w', 'T': 'P', 'W': 'F', 'V': 'K', 'Y': 'J', 'X': 'v', 'Z': 'C', 'a': 'I', 'c': 'D', 'b': 'h', 'e': 'E', 'd': 'o', 'g': 'V', 'f': 'g', 'i': 'y', 'h': 'N', 'k': '>', 'j': 'O', 'm': '.', 'l': '2', 'o': 'L', 'n': 'Z', 'q': 'Q', 'p': '1', 's': 'W', 'r': 'B', 'u': ':', 't': 'H', 'w': 'A', 'v': '0', 'y': 'M', 'x': 'l', 'z': 'n'}

content = '4C4C4544-004A-3610-8056-C3C04F594332\t1577905443.95\t1577932703.95\t57\t1'
enc = encryption2(content)
print(enc)

dec = decryption2(enc)
print(dec)

import os
import time


def is_expired2(filename,pro_uuid, max_t=365*86400):
    if not os.path.exists(filename):return False

    new_str = ''
    f = open(filename,'r')
    line = f.read()
    if not line:return False

    decrt = decryption2(line)  # 解码
    # print(decrt)
    data = decrt.split('\t')
    if len(data)!=5:return False

    uuid= data[0]  # 设备id
    if uuid != pro_uuid:
        f.close()
        new_str += pro_uuid + '\t'
        new_str += str(time.time()) + '\t'
        new_str += str(time.time()) + '\t'
        new_str += '0.0' + '\t'
        new_str += '0'
        encrt = encryption2(new_str)
        with open(filename, 'w') as f:
            f.write(encrt)
        return True

    first_t = float(data[1])  # 首次时间
    last_t = float(data[2])  # 最近时间
    used_t = float(data[3])  # 已用时间
    change_n = int(data[4])  # 修改次数

    if used_t>max_t:return False
    if last_t>time.time():return False
    if first_t>last_t:return False
    if (time.time()-first_t)>max_t:return False
    if change_n>(max_t/86400):return False
    gap = time.time()-last_t

    if gap>86400:  # 超过1天时间则更新一次
        new_str += uuid +'\t'
        new_str += data[1]+'\t'
        new_str += str(time.time())+'\t'
        new_str += str(used_t+gap) +'\t'
        new_str += str(change_n+1)

    if new_str:
        encrt = encryption2(new_str)
        with open(filename,'w') as f:
            f.write(encrt)
    return True

uid = '4C4C4544-0034-3610-804D-CAC04F4E4B32'
print is_expired2('tst.txt',uid)

start_stamp = time.strptime("2018-09-08","%Y-%m-%d")
print time.mktime(start_stamp)



'''
双重验证 1、系统uuid和项目中uuid是否统一；2、系统时间是否在项目配置文件时间内。uuid授权后一直不变，系统时间只要保证在授权时间内就可以一直使用。

问题定位：规则太弱
解决方法：
增加一个动态文件，文件内容为：uuid+第一次使用时间float+最近一次使用时间float+使用累计时间float+修改次数int，5个内容组成。文件字符串内容是经过base64转码后，再由代码中静态字符map映射后的字符串存储。如：4C4C4544-004A-3610-8056-C3C04F594332\t1577905443.95\t1577932703.95\t57\t1
经过base64转码后：NEM0QzQ1NDQtMDA0QS0zNjEwLTgwNTYtQzNDMDRGNTk0MzMyCTE1Nzc5MDU0NDMuOTUJMTU3Nzkz MjcwMy45NQk1Nwkx
在经过map({‘+’: ‘G’, ‘.’: ‘m’, ‘1’: ‘p’,…})映射后：
heyvq>qphcq=ycwvqPv>hLeUoCfUhCN=q>hcyc9RhCJvy>yiZCeph>S.ycDvhcy3jCDYyCDBh>J> yLSUyiE.hqJphUJ+
每次调用读取该文件：
1、文件必须存在，否则过期处理
2、新授权机器上使用时，根据uuid变化进行初始化文件内容
3、累计时间>最大授权时间，过期处理
4、系统时间<上一次使用时间，过期处理
5、上一次使用时间< 第一次使用时间 ,过期处理
6、(当前时间-第一次使用时间) > 最大授权时间, 过期处理
7、(当前时间-上一次使用时间) > 1天，更新累计时间，加密更新文件


'''