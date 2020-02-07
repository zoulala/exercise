#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     LDA.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-02-07
# brief:    
#
# cmd>e.g:  
# *****************************************************

from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel

# Create a corpus from a list of texts
common_dictionary = Dictionary(common_texts)
common_corpus = [common_dictionary.doc2bow(text) for text in common_texts]

# Train the model on the corpus.
lda = LdaModel(common_corpus, num_topics=10)

for sample in common_corpus:
    print(lda[sample])

