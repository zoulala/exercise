#!/usr/bin/python
# -*- coding: utf8 -*-
#
# *****************************************************
#
# file:     lstm_0.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2019-09-02
# brief:    用于序列分类的栈式LSTM
#
# 在该模型中，我们将三个LSTM堆叠在一起，是该模型能够学习更高层次的时域特征表示。
#
# 开始的两层LSTM返回其全部输出序列，而第三层LSTM只返回其输出序列的最后一步结果，从而其时域维度降低（即将输入序列转换为单个向量）
#  ref:https://keras-cn.readthedocs.io/en/latest/images/regular_stacked_lstm.png
# cmd>e.g:  
# *****************************************************

from keras.models import Sequential
from keras.layers import LSTM, Dense
import numpy as np

data_dim = 16
timesteps = 8
num_classes = 10

# expected input data shape: (batch_size, timesteps, data_dim)
model = Sequential()
model.add(LSTM(32, return_sequences=True,
               input_shape=(timesteps, data_dim)))  # returns a sequence of vectors of dimension 32
model.add(LSTM(32, return_sequences=True))  # returns a sequence of vectors of dimension 32
model.add(LSTM(32))  # return a single vector of dimension 32
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# Generate dummy training data
x_train = np.random.random((1000, timesteps, data_dim))
y_train = np.random.random((1000, num_classes))

# Generate dummy validation data
x_val = np.random.random((100, timesteps, data_dim))
y_val = np.random.random((100, num_classes))

model.fit(x_train, y_train,
          batch_size=64, epochs=5,
          validation_data=(x_val, y_val))


