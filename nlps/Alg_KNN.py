#!/user/bin/env python 
#-*- coding: utf-8 -*-

'''
Created on 2017年3月24日

@author: zoulingwei


k-近邻算法及测试
'''



from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels



def classify(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistances = distances.argsort()
    classCount = {}
    for i in range(k):
        numOflabel = labels[sortedDistances[i]]
        classCount[numOflabel] = classCount.get(numOflabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]



if __name__ == "__main__":
    group, labels = createDataSet()  
    result = classify([0,5], group, labels, 3)
    print result
