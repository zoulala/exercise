from numpy import array,zeros, float32
from gensim import matutils
from sklearn import preprocessing
from gensim.models import word2vec



def str2split(sentence):
    '''将句子按照中文、英文分开，如：‘我 is your朋友123’--> [‘我 ','is', 'your', '朋', '友','1','2','3']'''
    sens = []
    eword = ''
    nword = []

    sentence += ' '
    for uchar in sentence:
        if (uchar >= u'\u4e00' and uchar <= u'\u9fa5'):
            if eword:
                sens.append(eword)
                eword = ''
            if nword:
                sens.append(nword)
                nword = []
            sens.append(uchar)
        elif uchar == ' ':
            if eword:
                sens.append(eword)
                eword = ''
            if nword:
                sens.append(nword)
                nword = []
        elif uchar >= u'\u0030' and uchar<=u'\u0039':
            if eword:
                sens.append(eword)
                eword = ''
            nword.append(uchar)
        else:
            if nword:
                sens.append(nword)
                nword = []
            eword += uchar.lower()
    return sens

def trange(word):
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # b = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    b = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if word in a:
        dex = a.index(word)
        return b[dex]
    else:
        return word

def get_vec_sen(sentence, models, size):
    '''获得：语义向量, 字向量求和'''

    sens = str2split(sentence)
    print(sens)
    vector = zeros((size), dtype=float32)

    for w in sens:
        if isinstance(w, list):
            ln = len(w)
            vector_n = zeros((size), dtype=float32)
            for i in range(ln,0,-1):
                wi = trange(w[ln-i])
                for model in models:
                    if wi in model:
                        vector_ten = model['ten'] if 'ten' in model else model['十']
                        vector_n += model[wi]*(2**(i-1))+vector_ten*(i-1)
                        break
            vector += preprocessing.scale(vector_n)  # 标准化
        else:
            for model in models:
                if w in model:
                    #vector += model[w]
                    vector += preprocessing.scale(model[w])  # 标准化
                    break
    # vector = preprocessing.scale(vector)
    vector = matutils.unitvec(array(vector))  # 单位圆化：模为1
    return vector

def get_vec_sen_list(sen_list, models ,size):

    vec_list = [get_vec_sen(sen, models, size) for sen in sen_list]
    return vec_list

if __name__ == "__main__":
    path1 = '../chatbotapp/service/v1/train/models/word_model_wiki'
    path2 = '../chatbotapp/service/v1/train/models/wiki_3.en.text.model'
    model_1 = word2vec.Word2Vec.load(path1)
    model_2 = word2vec.Word2Vec.load(path2)

    models = [model_1,model_2]


    str1 = '为什么要手动升级呢？'
    str2 = '为什么要手动升级呢'

    # print(model.most_similar(str))

    vec1 = get_vec_sen(str1,models,100)
    vec2 = get_vec_sen(str2, models, 100)
    print(vec1)
    print(vec2)
    import numpy as np
    score = np.dot(vec1,vec2)
    print('score:\n',score)