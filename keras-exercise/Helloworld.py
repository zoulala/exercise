#!/usr/bin/python
# -*- coding: utf8 -*-
#
# *****************************************************
#
# file:     Helloworld.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2019-09-02
# brief:    ref:https://keras-cn.readthedocs.io/en/latest/
#
# cmd>e.g:  
# *****************************************************

from keras.models import Sequential
from keras.layers import Dense, Activation

## 可以通过向Sequential模型传递一个layer的list来构造该模型：
# model = Sequential([
# Dense(32, units=784),
# Activation('relu'),
# Dense(10),
# Activation('softmax'),
# ])

# 也可以通过.add()方法一个个的将layer加入模型中：
model = Sequential()
model.add(Dense(units=64, input_dim=100))
model.add(Activation("relu"))
model.add(Dense(units=10))
model.add(Activation("softmax"))


# 完成模型的搭建后，我们需要使用.compile()方法来编译模型：
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 也可以自己定制损失函数。甚至修改源代码。
# from keras.optimizers import SGD
# model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True))


#完成模型编译后，我们在训练数据上按batch进行一定次数的迭代来训练网络
model.fit(x_train, y_train, epochs=5, batch_size=32)
## 当然，我们也可以手动将一个个batch的数据送入网络中训练，这时候需要使用：
# model.train_on_batch(x_batch, y_batch)

#随后，我们可以使用一行代码对我们的模型进行评估，看看模型的指标是否满足我们的要求：
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)


#或者，我们可以使用我们的模型，对新的数据进行预测：
classes = model.predict(x_test, batch_size=128)