#coding=utf-8
"""
time    : 2017-5-12
d.s     : jieba相关操作
"""

import jieba
import jieba.posseg
import jieba.analyse


class Nlp_Jieba(object):
    """
    分词处理
    包括： 
            jieba自定义词典加载
            jieba分词方法
            jieba词性标注
            jieba关键词提取
    """
    #path = 'D:\\pycharm\\PyCharm Community Edition 2017.1.1\\workspace\\py35\\Chat-YouMi\\'
    def __init__(self,userdic="trains/model/userdicts.txt"):
        """初始化jieba 加载通用字典.
        """
        self.init_jieba(userdic)

    def init_jieba(self,  userdic):
        """jieba 加载自定义字典.
        """
        jieba.load_userdict(userdic)
        #jieba.set_dictionary(seg_dic)
        with open(userdic,'r',encoding='utf8') as input:
            for word in input:
                word = word.strip('\n')
                jieba.suggest_freq(word, True)

    def word_segment(self, sentence):
        """jieba 精简分词.
            Args: 字符串
            returns:  分词列表
        """
        cut_words = jieba.cut(sentence, HMM=False)
        words = []
        for word in cut_words:
            words.append(word)
        return words

    def word_posseg(self, sentence):
        segs = jieba.posseg.cut(sentence)
        words = []
        flags = []
        for seg in segs:
            words.append(seg.word)
            flags.append(seg.flag)
        return words,flags

    def jieba_textrank(self,speech):
        """jieba关键词提取，textrank算法
        Use textrank in jieba to extract keywords in a sentence.
        """
        return jieba.analyse.textrank(speech, withWeight=True, topK=20)

    def jieba_tf_idf(self,speech):
        """jieba关键词提取，tf/idf算法
        Use tf/idf in jieba to extract keywords in a sentence
        """
        return jieba.analyse.extract_tags(speech, topK=20, withWeight=True)

    #----------------------------------------------------------------------
    #   以下定义其他分词


if __name__ == "__main__":
    str = '我家在塔溪，我再北京工作，大理过炒年糕号码'
    wd = Nlp_Jieba(userdic="trains/modle/userdicts.txt")
    list = wd.jieba_tf_idf(str)
    list2 = wd.word_segment(str)
    # print('/'.join(list))
    for w in list2:
        print (w)

    # from chatbot import load_data
    # titles_dict = load_data.load_titles()
    # titleslist = titles_dict.values()
    # for title in titleslist:
    #     print('\n',title)
    #     list = wd.jieba_tf_idf(title)
    #     for t in list:
    #         print(t[0], end='/')
