# -*- coding: utf-8 -*-
"""
pyltp 是 [语言技术平台（Language Technology Platform, LTP）](https://github.com/HIT-SCIR/ltp)的 Python 封装。
在使用 pyltp 之前，您需要简要了解 [语言技术平台（LTP）](http://ltp.readthedocs.org/zh_CN/latest/) 能否帮助您解决问题。
"""

from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import NamedEntityRecognizer
from pyltp import Parser

import os
LTP_DATA_DIR = '../trains\\model\\ltp_data'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
user_dict_path = os.path.join(LTP_DATA_DIR, 'userdict1.txt' )  # 自定义分词词典路径，名称为``

pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名体识别模型路径，模型名称为`ner.model`

par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`

class Nlp_Ltp(object):
    """
    哈工大语言处理工具pyLTP
    """
    def __init__(self):
        pass
    #分句
    '''
    此函数参数输入的格式必须为str格式，所以直接获取的list里的参数值需要 
    通过encode('utf-8')，从Unicode转换为str 
    '''
    def sentence_splitter(self,sentence):
        sents = SentenceSplitter.split(sentence)
        print ('\n'.join(sents)  )
        sents_list = list(sents)
        return sents_list

    # 分词
    def segmentor(self, sentence):
        segmentor = Segmentor()
        #segmentor.load(cws_model_path)  # 加载模型
        segmentor.load_with_lexicon(cws_model_path, user_dict_path)  # 加载模型，第二个参数是您的外部词典文件路径
        words = segmentor.segment(sentence)  # 分词
        # 默认可以这样输出
        #print ('\t'.join(words))
        # 可以转化成List输出
        word_list = list(words)
        segmentor.release()  # 释放模型
        return word_list


    # 词性标注
    def posttagger(self, words):
        postagger = Postagger()
        postagger.load(pos_model_path)
        posttags = postagger.postag(words)  # 词性标注
        postags = list(posttags)
        postagger.release()  # 释放模型
        # print type(postags)
        return postags


    # 命名实体识别
    def ner(self, words, postags):
        # print ('命名实体开始！')
        recognizer = NamedEntityRecognizer()
        recognizer.load(ner_model_path)  # 加载模型
        netags = recognizer.recognize(words, postags)  # 命名实体识别
        # for word, ntag in zip(words, netags):
        #     print(word + '/' + ntag)
        recognizer.release()  # 释放模型
        nerttags = list(netags)
        return nerttags

    # 依存句法分析
    def parse(self, words, postags):
        parser = Parser() # 初始化实例
        parser.load(par_model_path)  # 加载模型
        arcs = parser.parse(words, postags)  # 句法分析
        #print ("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
        parser.release()  # 释放模型
        return arcs

if __name__ == "__main__":
    ltp = Nlp_Ltp()
    str = '　　大侠，小精灵倾力为您服务！<br />　　黄龙洞是一个允许宣战，加杀气的场景；<br />　　此场景中可能会发生玩家之间的PK行为，主动杀死其他玩家会受到杀气惩罚，请您注意安全哦~<br />　　当您切换场景时，游戏上方会提示您该场景是否存在宣战、加杀气的信息。<br />　　小精灵提示您：您如果对杀气值概念模糊，也可向小精灵咨询如&ldquo;杀气值是什么'

    words = ltp.segmentor(str)
    postags = ltp.posttagger(words)
    nerttags = ltp.ner(words, postags)
    arcs = ltp.parse(words, postags)
    print(words)
    print(postags)
    print(nerttags)
    print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))