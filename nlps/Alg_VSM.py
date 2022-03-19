#!/user/bin/env python 
#-*- coding: utf-8 -*-

'''
Created on 2017年3月23日

@author: zoulingwei


 vsm向量空间模型实现,计算两个文本的相似度（通过构建文档的字频向量，计算两个文档字频向量的相似度）

'''

# first: cipintongji
import math
import ast
from collections import Counter
wordsCount=0#variable for wordsfrequency
def CountKeyByWen(fileName1):#对文本进行所有词，词数统计（只对英文文章有效）
    global wordsCount
    f1=open(fileName1,'r')
    f1=open(fileName2,'r')
    table={}
    for lines in f1:
        for line in lines.split(' '):
            if line!=' ' and table.has_key(line):
                table[line]+=1
                wordsCount+=1
            elif line!=' ':
                wordsCount+=1
                table[line]=1
    dic = sorted(table.iteritems(),key= lambda asd:asd[1], reverse=True)
    # print len(dic) code for testing
    return dic
# seconde:create vocabulary
def CreateVocabulary(dic1=None, dic2=None):#创建字表
    vocabulary=[]
    for dicEle in dic1:
        if dicEle[0] not in vocabulary:
            vocabulary.append(dicEle[0])
    for dicEle in dic2:
        if dicEle[0] not in vocabulary:
            vocabulary.append(dicEle[0])
    # print len(vocabulary) code for testing
    return vocabulary
# third:compute TF-IDF output: a vector
# In this code we just use TF for computing similarity
def ComputeVector(dic1=None,vocabulary=None):#统计字频，生成字频向量
    # 3.1compute cipin global wordscount wordsCount
    # 3.2create vector
    dicVector = {}
    for elem in vocabulary:
        dicVector[elem]=0
    # dicVector = sorted(dicVector.iteritems(),key= lambda asd:asd[1], reverse=True)
    dicTemp1,dicTemp2=Counter(dicVector), Counter(dic1)
    dicTemp=dict(dicTemp1+dicTemp2)
    # dicTemp = sorted(dicTemp.iteritems(),key= lambda asd:asd[1], reverse=True)
    return  dicTemp
# fourth: compute TF-IDF
def ComputeSimlirity(dic1Vector=None,dic2Vector=None):#通过字频向量，计算两个文本的相似度
    x=0.0 #fenzi
    #fenmu
    y1=0.0
    y2=0.0
    for k in dic1Vector:# because of the element of dic1 and dic2 are the same
        temp1=(float)(float(dic1Vector[k])/float(wordsCount))
        temp2=(float)(float(dic2Vector[k])/float(wordsCount))
        x=x+ (temp1*temp2)
        y1+=pow(temp1,2)
        y2+=pow(temp2,2)
    return x/math.sqrt(y1*y2)

if __name__=='__main__':
    fileName1='C:\\Users\\zoulingwei\\Desktop\\testr.txt';
    fileName2='C:\\Users\\zoulingwei\\Desktop\\testw.txt';
    dic1 = CountKeyByWen(fileName1)
    dic2 = CountKeyByWen(fileName2)
    vocabulary = CreateVocabulary(dic1, dic2)
    dic1Vector = ComputeVector(dic1, vocabulary)
    dic2Vector = ComputeVector(dic2, vocabulary)
    for elem in dic1Vector:
        print "<"+elem[0],',',str(elem[1])+">"
    sim=ComputeSimlirity(dic1Vector,dic2Vector)
    print sim

