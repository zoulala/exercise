#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     ddparser_evaluate.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-01-24
# brief:    百度基于深度学习的依存句法分析，https://github.com/baidu/DDParser
#
# cmd>e.g:  
# *****************************************************

import xlwt
from ddparser import DDParser


'''
Label','关系类型','说明','示例
SBV','主谓关系','主语与谓词间的关系','他送了一本书(他<--送)
VOB','动宾关系','宾语与谓词间的关系','他送了一本书(送-->书)
POB','介宾关系','介词与宾语间的关系','我把书卖了（把-->书）
ADV','状中关系','状语与中心词间的关系','我昨天买书了（昨天<--买）
CMP','动补关系','补语与中心词间的关系','我都吃完了（吃-->完）
ATT','定中关系','定语与中心词间的关系','他送了一本书(一本<--书)
F','方位关系','方位词与中心词的关系','在公园里玩耍(公园-->里)
COO','并列关系','同类型词语间关系','叔叔阿姨(叔叔-->阿姨)
DBL','兼语结构','主谓短语做宾语的结构','他请我吃饭(请-->我，请-->吃饭)
DOB','双宾语结构','谓语后出现两个宾语','他送我一本书(送-->我，送-->书)
VV','连谓结构','同主语的多个谓词间关系','他外出吃饭(外出-->吃饭)
IC','子句结构','两个结构独立或关联的单句','你好，书店怎么走？(你好<--走)
MT','虚词成分','虚词与中心词间的关系','他送了一本书(送-->了)
HED','核心关系','指整个句子的核心','
'''

ddp = DDParser()
# rst = ddp.parse("孩子发热不降，精神很好，舌苔有点重。")
# print(rst)
#
# rst = ddp.parse(["百度是一家高科技公司", "他送了一本书"])
# print(rst)
# exit()



def ddparser_val():

    workbook2 = xlwt.Workbook()
    sheet2 = workbook2.add_sheet("sheet2")

    row_idx = 0
    n = 500
    
    relates = ['SBV','VOB','POB','ADV','CMP','ATT','F','COO','DBL','DOB','VV','IC','MT','HED']
    relates_map = {k:v for v,k in enumerate(relates)}
    sheet2.write(row_idx, 0, 'line')
    sheet2.write(row_idx, 1, 'words')
    for i in range(len(relates)):
        ii = i+2
        sheet2.write(row_idx, ii, relates[i])

    with open('zhusu.txt','r') as f:
        for line in f:
            print(row_idx)
            if row_idx > n:
                break
            line = line.strip()
            if not line:continue
            line2 = line.replace('患者:','')
            rst = ddp.parse(line2)[0]

            words = rst['word']
            heads = rst['head']
            deprels = rst['deprel']
            row_idx += 1
            sheet2.write(row_idx, 0, line)
            sheet2.write(row_idx, 1, '/'.join(words))

            _dic = {}

            for j in range(len(words)):
                word = words[j]
                head = heads[j]
                deprel = deprels[j]
                subject = words[head]
                _str = '__'.join([word, deprel, subject])

                if deprel not in _dic:
                    _dic[deprel] = []
                _dic[deprel].append(_str)

            for deprel in _dic:

                jj = relates_map[deprel]+2


                _sstrs = '; '.join(_dic[deprel])
                print(_sstrs)
                sheet2.write(row_idx, jj, _sstrs)

    workbook2.save("ddparser_eval.xls")

ddparser_val()