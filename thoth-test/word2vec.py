#!/user/bin/env python
#-*- coding: utf-8 -*-

'''
Created on 2017��5��4��
对中文进行分词，word2vec训练中文
@author: zoulingwei
'''


import numpy as np
from gensim.models import word2vec
import os
import re
from lib import similar_str2str

import logging

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):#构造yield的生成器，避免一次性读入内存
        for line in open(self.dirname):
            #line = line.decode(defaultcode)#解码为unicode
            yield line.split()



class MySentences_all(object):
    def __init__(self, path):
        self.path = path
        self.hanzi_re = re.compile(u"[\u4E00-\u9FD5]+", re.U)

    def __iter__(self):#构造yield的生成器，避免一次性读入内存

        for filename in os.listdir(path):
            pathname = path + filename
            print(pathname)
            for line in open(pathname,'r',encoding='utf8'):
                #line = line.decode(defaultcode)#解码为unicode
                hanzi_list = self.extract_hanzi(line)
                for hanzi_line in hanzi_list:
                    fenci_line = self.cut_sentence(hanzi_line)
                    yield fenci_line.split()

    def extract_hanzi(self,sentence):
        """提取汉字"""
        return self.hanzi_re.findall(sentence)

    def cut_sentence(self,sentence):
        """分词"""
        return ' '.join(sentence)



if __name__ == "__main__":
    # path = 'C:/Users/zoulingwei/Desktop/data//'
    # model_name = 'model1'

    path = 'C:/Users/zoulingwei/Desktop/wiki//'
    model_name = 'model/word_model_wiki'
    #sentences = MySentences_all(path) # a memory-friendly iterator

    #model = word2vec.Word2Vec(sentences)
    #model.save(model_name)

    model = word2vec.Word2Vec.load(model_name)
    # print(len(model['爱']))
    # print(model.most_similar('爱'))
    # print(model.similarity('我','你'))
    #print(model.similar_by_vector(vec))

    str1 = '我冯'
    str2 = '的冯'
    # 没标准化：如何/怎么=0.453    什么意思啊 & 说的啥 =0.46    你在干啥呢/做什么哦=0.6  ；；；；'我/的=-0.1'，‘我熵/的熵=0.1’,'我熵/我冯=0.8', 说明常用字向量方差大
    # 标准化：如何/怎么=0.455    什么意思啊 & 说的啥=0.57     你在干啥呢/做什么哦=0.74  ；；；；'我/的=-0.09'，‘我熵/的熵=0.49’,'我熵/我冯=0.46', 说明改善


    from gensim import matutils
    from sklearn import preprocessing

    str = '新皇朝御礼'
    for w in str:
        v1 = model[w]
        print(np.var(v1))


    vector1 = np.zeros((100),dtype=np.float32)
    for w in str1:
        if w in model:
            #vector1 += model[w]
            vector1 += preprocessing.scale(model[w])

    vector1_un = matutils.unitvec(vector1)
    vector1_zc = preprocessing.scale(vector1)

    vector2 = np.zeros((100), dtype=np.float32)
    for w in str2:
        if w in model:
            #vector2 += model[w]
            vector2 += preprocessing.scale(model[w])

    vector2_un = matutils.unitvec(vector2)
    vector2_zc = preprocessing.scale(vector2)

    vector2_zc_un = matutils.unitvec(vector2_zc)

    sm = similar_str2str.arithmetic()
    print(model.similar_by_vector(vector2_zc))

    print('un_dot:',np.dot(vector1_un,vector2_un))
    print('zc_dot:',np.dot(vector1_zc,vector2_zc)/100)

    #result = sm.cosxy(vector1,vector2)
    #print('cos:',result)
    


    '''
    
    a = [4,0,5,1,7,2,1]
    b = [5.2,1.2,6.2,2.2,8.2,3.2,2.2]
    #b = [3,4,2,3,1,5,2]
    a=[1,1.1,1.2,1.3]
    b=[-7,3,6,-4]
    c=[3,1,8,2]


    print(np.var(a),np.var(b))
    print(np.std(a),np.std(b))

    def mo(a):  # 向量莫
        aa = [i*i for i in a]
        mos = pow(sum(aa), 0.5)
        return mos

    def un(a):  # 单位化
        list = [i/mo(a) for i in a]
        return list

    def zc(a):   # 标准化
        mea = np.mean(a)
        zcroe_a = [(i-mea)/np.std(a) for i in a]
        return zcroe_a
    def add(a,b):
        list = [a[i]+b[i] for i in range(len(a))]
        return list

    def r(a,b):
        cov = np.cov(a,b)

    a_un = un(a)
    b_un = un(b)
    a_zc = zc(a)
    b_zc = zc(b)




    a_zc_un = zc(a_un)
    b_zc_un = zc(b_un)
    a_un_zc = un(a_zc)
    b_un_zc = un(b_zc)
    print(a_zc)
    print(b_zc)

    a_un_mo = mo(a_un)
    b_un_mo = mo(b_un)
    a_zc_mo = mo(a_zc)
    b_zc_mo = mo(b_zc)


    c_un = un(c)
    c_zc = zc(c)

    ab_un = add(a_un,b_un)
    aab_un = add(ab_un,a_un)
    abc_un = add(ab_un,c_un)
    abc_un_un = un(abc_un)
    ab_un_un = un(ab_un)
    aab_un_un = un(aab_un)
    print(np.dot(b_un,abc_un_un))

    ab_zc = add(a_zc,b_zc)
    abc_zc = add(ab_zc,c_zc)

    aab_zc = add(ab_zc,a_zc)
    abb_zc = add(b_zc,ab_zc)

    print(np.corrcoef(c_zc,abc_zc))


    print('a_un:', a_un)
    print('b_un:', b_un)
    print('a_zc:',a_zc)
    print('b_zc:',b_zc)

    print('a_mo',mo(a))
    print('b_mo',mo(b))
    print('a_un_mo:',a_un_mo)
    print('b_un_mo:',b_un_mo)
    print('a_zc_mo:',a_zc_mo)
    print('b_zc_mo:',b_zc_mo)

    print(np.var(a_un))

    print(np.cov(a,b))
    print(np.cov(a_zc,b_zc))

    print(np.corrcoef(a, b))
    print(np.corrcoef(a_un_zc,b_un_zc))

    print('ab_dot:',np.dot(a,b)/(mo(a)*mo(b)))
    print('ab_un_dot:',np.dot(a_un,b_un))
    print('ab_zc_dot:',np.dot(a_zc,b_zc))
    print('ab_un_zc_dot:',np.dot(a_un_zc,b_un_zc))
    '''
