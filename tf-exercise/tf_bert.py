#!/usr/bin/python
# -*- coding: utf8 -*-
#
# *****************************************************
#
# file:     tf_bert.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2019-09-24
# brief:    
#
# cmd>e.g:  
# *****************************************************


import numpy as np
import create_input
import tensorflow as tf
from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file
from tensorflow.python import pywrap_tensorflow
from bert import modeling
from bert import tokenization

tf.logging.set_verbosity(tf.logging.INFO)

# 这里是下载下来的bert配置文件
bert_config = modeling.BertConfig.from_json_file("chinese_L-12_H-768_A-12/bert_config.json")
vocab_file="chinese_L-12_H-768_A-12/vocab.txt"
batch_size=20
num_labels=2  # 类别数量，我的例子是个二分类
is_training=True
max_seq_length=128
iter_num=1000
lr=0.00005


# ----------------------------------- model搭建 ---------------------------------
#  创建bert的输入
input_ids = tf.placeholder(shape=[batch_size, max_seq_length], dtype=tf.int32, name="input_ids")
input_mask = tf.placeholder(shape=[batch_size, max_seq_length], dtype=tf.int32, name="input_mask")
segment_ids = tf.placeholder(shape=[batch_size, max_seq_length], dtype=tf.int32, name="segment_ids")
###
input_labels=tf.placeholder (shape=batch_size,dtype=tf.int32,name="input_ids")
# 创建bert模型
model = modeling.BertModel(
    config=bert_config,
    is_training=True,
    input_ids=input_ids,
    input_mask=input_mask,
    token_type_ids=segment_ids,
    use_one_hot_embeddings=False  # 这里如果使用TPU 设置为True，速度会快些。使用CPU 或GPU 设置为False ，速度会快些。
)

output_layer = model.get_sequence_output()  # 这个获取每个token的output 输入数据[batch_size, seq_length, embedding_size] 如果做seq2seq 或者ner 用这个
output_layer = model.get_pooled_output()  # 这个获取句子的output
hidden_size = output_layer.shape[-1].value #获取输出的维度


# 后面增加一个全连接
with tf.variable_scope('Last_Full'):
    logits = tf.layers.dense(output_layer, 2)
    loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=input_labels, name="soft_loss")
    loss = tf.reduce_mean(loss, name="loss")
    predict = tf.argmax(tf.nn.softmax(logits), axis=1, name="predictions")
    acc = tf.reduce_mean(tf.cast(tf.equal(input_labels, tf.cast(predict, dtype=tf.int32)), "float"), name="accuracy")

update_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope='Last_Full')  # 搜集Last_Full下的变量
train_op = tf.train.AdamOptimizer(lr).minimize(loss, var_list=update_vars)  # var_list:指定需要更新参数的变量


# ---------------------------------- 初始化模型 ----------------------------------
# bert模型参数初始化的地方
init_checkpoint = "chinese_L-12_H-768_A-12/bert_model.ckpt"
use_tpu = False
# 获取模型中所有的训练参数。
tvars = tf.trainable_variables()
# 加载BERT模型
(assignment_map, initialized_variable_names) = modeling.get_assignment_map_from_checkpoint(tvars,
                                                                                           init_checkpoint)
tf.train.init_from_checkpoint(init_checkpoint, assignment_map)

tf.logging.info("**** Trainable Variables ****")
# 打印加载模型的参数
reader = pywrap_tensorflow.NewCheckpointReader(init_checkpoint)
var_to_shape_map = reader.get_variable_to_shape_map()
print(reader.get_tensor('cls/seq_relationship/output_bias'))
# for key in var_to_shape_map:
#     print(key)
#     print(reader.get_tensor(key))

for var in tvars:
    init_string = ""
    if var.name in initialized_variable_names:
        init_string = ", *INIT_FROM_CKPT*"
    tf.logging.info("  name = %s, shape = %s%s", var.name, var.shape,
                    init_string)

    # print_tensors_in_checkpoint_file("chinese_L-12_H-768_A-12/bert_model.ckpt", tensor_name=var.name, all_tensors=True)
    # print(reader.get_tensor(var.name))
    #
# # 输出所有参数
# print_tensors_in_checkpoint_file("chinese_L-12_H-768_A-12/bert_model.ckpt", None,True)






# ---------------------------------- 产生训练样本 ----------------------------------
# 加载数据集合
with open("data/text.txt","r",encoding="utf-8") as f:
    data=f.read().splitlines()
texts=[]
labels=[]
for line in data:
    line=line.split("\t")
    if len(line) ==2 and int(line[1])<2:# 这里演示一个二分类问题，但训练样本并没有认真处理过，所以去掉label大于1的。
        texts.append(line[0])
        labels.append(line[1])

tokenizer = tokenization.FullTokenizer(vocab_file=vocab_file) # token 处理器，主要作用就是 分字，将字转换成ID。vocab_file 字典文件路径
input_idsList=[]
input_masksList=[]
segment_idsList=[]
for t in texts:
    single_input_id, single_input_mask, single_segment_id=create_input.convert_single_example(max_seq_length,tokenizer,t)
    input_idsList.append(single_input_id)
    input_masksList.append(single_input_mask)
    segment_idsList.append(single_segment_id)



input_idsList=np.asarray(input_idsList,dtype=np.int32)
input_masksList=np.asarray(input_masksList,dtype=np.int32)
segment_idsList=np.asarray(segment_idsList,dtype=np.int32)
labels=np.asarray(labels,dtype=np.int32)

# ---------------------------------- 训练过程 ----------------------------------
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())  # 这里初始化并不会将上面已经初始化的bert变量覆盖
    print(reader.get_tensor('cls/seq_relationship/output_bias'))
    for i in range(iter_num):
        shuffIndex = np.random.permutation(np.arange(len(texts)))[:batch_size]
        batch_labels = labels[shuffIndex]
        batch_input_idsList=input_idsList[shuffIndex]
        batch_input_masksList=input_masksList[shuffIndex]
        batch_segment_idsList=segment_idsList[shuffIndex]
        l,a,_=sess.run([loss,acc,train_op],feed_dict={
            input_ids:batch_input_idsList,input_mask:batch_input_masksList,
            segment_ids:batch_segment_idsList,input_labels:batch_labels
        })
        print("准确率:{},损失函数:{}".format(a,l))

