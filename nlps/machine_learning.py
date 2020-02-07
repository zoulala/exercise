#coding=utf-8
"""
d.s     :传统机器学习算法
"""
import operator
from numpy import *


class ML(object):
    """
    机器学习算法
    包括:   K_NN()，K近邻算法
            K_means()，K均值聚类算法
            SVM()，支持向量机
            Decision_tree，决策树ID3
            boosting，增强学习算法
            Naive Bayes， 朴素贝叶斯
    """
    def __init__(self):
        pass

    def K_NN(self, inX, dataSet, labels, k):
        ''' K近邻算法
            Args:
                 inX: 需要分类的向量
                 dataSet: 已知类别的数据集array
                 labels: 数据集对应的标签
                 k:                 
            returns: inX对应的label
        '''
        dataSetSize = dataSet.shape[0]
        diffMat = tile(inX, (dataSetSize, 1)) - dataSet
        sqDiffMat = diffMat ** 2
        sqDistances = sqDiffMat.sum(axis=1)
        distances = sqDistances ** 0.5
        sortedDistances = distances.argsort()
        classCount = {}
        for i in range(k):
            numOflabel = labels[sortedDistances[i]]
            classCount[numOflabel] = classCount.get(numOflabel, 0) + 1
        sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]

    def K_means(self, dataSet, k):
        ''' K均值算法
            Args:
                 dataSet: 数据集array
                 k:     聚成k类            
            returns: k个中心向量,样本类列表[类别  与中心的欧式距离]
        '''
        # calculate Euclidean distance
        def euclDistance(vector1, vector2):
            return sqrt(sum(power(vector2 - vector1, 2)))

        # init centroids with random samples
        def initCentroids(dataSet, k):
            numSamples, dim = dataSet.shape
            centroids = zeros((k, dim))
            for i in range(k):
                index = int(random.uniform(0, numSamples))
                centroids[i, :] = dataSet[index, :]
            return centroids

        numSamples = dataSet.shape[0]
        # first column stores which cluster this sample belongs to,
        # second column stores the error between this sample and its centroid
        clusterAssment = mat(zeros((numSamples, 2)))
        clusterChanged = True

        ## step 1: init centroids
        centroids = initCentroids(dataSet, k)
        l=0
        while clusterChanged:
            l+=1
            print (l)
            clusterChanged = False
            ## for each sample
            for i in range(numSamples):
                minDist = 100000.0
                minIndex = 0
                ## for each centroid
                ## step 2: find the centroid who is closest
                for j in range(k):
                    distance = euclDistance(centroids[j, :], dataSet[i, :])
                    if distance < minDist:
                        minDist = distance
                        minIndex = j

                ## step 3: update its cluster
                if clusterAssment[i, 0] != minIndex:
                    clusterChanged = True
                    clusterAssment[i, :] = minIndex, minDist

            ## step 4: update centroids
            for j in range(k):
                pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
                centroids[j, :] = mean(pointsInCluster, axis=0)

        print('Congratulations, cluster complete!')
        return centroids, clusterAssment

if __name__ == "__main__":
    dataSet = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1],[5,0.1],[3,0.1],[2,0.1],[8,0.1],
                     [0,8],[0,9.1], [0, 4.1],[0,0.6],[0.5,0.1],[0,3.1],[4,1.1],[3,0.9]])

    MLbot = ML()
    cent,clus = MLbot.K_means(dataSet,3)
    print(cent, '\n\n',clus)