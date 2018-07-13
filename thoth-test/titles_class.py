
import numpy as np
import collections
from lib import similar_str2str

def titles_Kmeans(titleslist, k):
    '''实现标题列表的k均值分类'''

    def str2words(titleslist):
        '''titleslist:['在何方','法分天法',...]，words:['法','在','何',...]'''
        all_words = []
        for title in titleslist:
            all_words += [word for word in title]
        counter = collections.Counter(all_words)
        count_pairs = sorted(counter.items(), key=lambda x: -x[1])
        words, _ = zip(*count_pairs)
        return words  # 不重复的字，并按字频排好序

    def str2vector(str, words):
        '''构建标题向量'''
        vec_len = len(words)
        vector = np.zeros(vec_len)
        for word in str:
            if word in words:
                vector[words.index(word)] = 1
        return vector

    titleslist = list(titleslist)
    words = str2words(titleslist)
    vec1 = str2vector(titleslist[0], words)
    aaa = [str2vector(title, words) for title in titleslist]
    aaa = np.array(aaa)
    from lib import machine_learning
    mlbot = machine_learning.ML()
    cent, clus = mlbot.K_means(aaa, k)
    # for j in range(k):
    #     print("------------------------------------", j)
    #     mi = [i for i in range(len(clus)) if clus[i, 0] == j]
    #     for ii in mi:
    #         print(titleslist[ii])

def title_Knn(titleslist, k):
    '''对titleslist列表，计算出每个title对应的5个最相似的titles,返回索引号字典'''
    titleslist = list(titleslist)
    similar = similar_str2str.arithmetic()
    dict_knn = {}
    for i in range(len(titleslist)):
        coses = []
        for str2 in titleslist:
            levd = similar.levenshtein(titleslist[i], str2)
            val1, val2 = similar.creat_val(titleslist[i], str2)
            cos = similar.cosxy(val1, val2)
            coses.append(cos)

        sov_n = np.argsort(coses)  # 相似度低到高排序序号
        sov_n = list(sov_n)
        sov_n.reverse()
        dict_knn[i] = sov_n[1:k]
    return dict_knn