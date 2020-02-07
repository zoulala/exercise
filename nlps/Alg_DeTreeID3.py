#!/user/bin/env python 
#-*- coding: utf-8 -*-

'''
Created on 2017��3��24��

@author: zoulingwei
'''



import math
import operator

def calcShannonEnt(dataSet):  
    '''计算给定数据shangnon数据的函数'''
    #calculate the shannon value  
    numEntries = len(dataSet)  
    labelCounts = {}  
    for featVec in dataSet:      #create the dictionary for all of the data  
        currentLabel = featVec[-1]  
        if currentLabel not in labelCounts.keys():  
            labelCounts[currentLabel] = 0  
        labelCounts[currentLabel] += 1  
    shannonEnt = 0.0  
    for key in labelCounts:  
        prob = float(labelCounts[key])/numEntries  
        shannonEnt -= prob*math.log(prob,2) #get the log value  
    return shannonEnt  



def createDataSet(): 
    '''创建数据的函数''' 
    dataSet = [[1,1,'yes'],  
               [1,1, 'yes'],  
               [1,0,'no'],  
               [0,1,'no'],  
               [0,1,'no']]  
    labels = ['no surfacing','flippers']  
    return dataSet, labels  

def splitDataSet(dataSet, axis, value): 
    '''划分数据集，按照给定的特征划分数据集''' 
    retDataSet = []  
    for featVec in dataSet:  
        if featVec[axis] == value:      #abstract the fature  
            reducedFeatVec = featVec[:axis]  
            reducedFeatVec.extend(featVec[axis+1:])  
            retDataSet.append(reducedFeatVec)  
    return retDataSet  

def chooseBestFeatureToSplit(dataSet): 
    '''选择最好的数据集划分方式''' 
    numFeatures = len(dataSet[0])-1  
    baseEntropy = calcShannonEnt(dataSet)  
    bestInfoGain = 0.0; bestFeature = -1  
    for i in range(numFeatures):  
        featList = [example[i] for example in dataSet]  
        uniqueVals = set(featList)  
        newEntropy = 0.0  
        for value in uniqueVals:  
            subDataSet = splitDataSet(dataSet, i , value)  
            prob = len(subDataSet)/float(len(dataSet))  
            newEntropy +=prob * calcShannonEnt(subDataSet)  
        infoGain = baseEntropy - newEntropy  
        if(infoGain > bestInfoGain):  
            bestInfoGain = infoGain  
            bestFeature = i  
    return bestFeature  

def majorityCnt(classList):  
    '''递归创建树'''
    classCount = {}  
    for vote in classList:  
        if vote not in classCount.keys(): classCount[vote] = 0  
        classCount[vote] += 1  
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)  
    return sortedClassCount[0][0]  

def createTree(dataSet, labels): 
    '''用于创建树的函数代码''' 
    classList = [example[-1] for example in dataSet]  
    # the type is the same, so stop classify  
    if classList.count(classList[0]) == len(classList):  
        return classList[0]  
    # traversal all the features and choose the most frequent feature  
    if (len(dataSet[0]) == 1):  
        return majorityCnt(classList)  
    bestFeat = chooseBestFeatureToSplit(dataSet)  
    bestFeatLabel = labels[bestFeat]  
    myTree = {bestFeatLabel:{}}  
    del(labels[bestFeat])  
    #get the list which attain the whole properties  
    featValues = [example[bestFeat] for example in dataSet]  
    uniqueVals = set(featValues)  
    for value in uniqueVals:  
        subLabels = labels[:]  
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)  
    return myTree  


def classify(inputTree, featLabels, testVec):
    '''实用决策树进行分类的函数'''  
    firstStr = inputTree.keys()[0]  
    secondDict = inputTree[firstStr]  
    featIndex = featLabels.index(firstStr)  
    for key in secondDict.keys():  
        if testVec[featIndex] == key:  
            if type(secondDict[key]).__name__ == 'dict':  
                classLabel = classify(secondDict[key], featLabels, testVec)  
            else: classLabel = secondDict[key]  
    return classLabel  

if __name__ == "__main__":
    myDat, labels = createDataSet()  
    myTree = createTree(myDat,labels)  
    print myTree  
    
    labels1 = ['no surfacing','flippers']     
    result = classify(myTree,labels1,[1,1]) 
    print result