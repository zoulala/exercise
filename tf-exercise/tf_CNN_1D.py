"""
1、比较了tf.nn.conv1d和tf.layters.conv1d 两种方法的实现及参数。
2、用cov2d实现 cov1d
ref:https://www.cnblogs.com/HITSZ/p/8721414.html
"""

import tensorflow as tf
import numpy as np
sess = tf.InteractiveSession()


# --------------- tf.nn.conv1d  -------------------
inputs=tf.ones((64,10,3))  # [batch, n_sqs, embedsize]
w=tf.constant(1,tf.float32,(5,3,32))  # [w_high, embedsize, n_filers]
conv1 = tf.nn.conv1d(inputs,w,stride=2 ,padding='SAME')  # conv1=[batch, round(n_sqs/stride), n_filers],stride是步长。

tf.global_variables_initializer().run()
out = sess.run(w)
print(out)

# --------------- tf.nn.conv1d  &  tf.layers.conv1d  -------------------
batch_size = 32
embedding_dim = 64  # 词向量维度
seq_length = 600  # 序列长度
num_classes = 10  # 类别数
num_filters = 256  # 卷积核数目
kernel_size = 5  # 卷积核尺寸
vocab_size = 5000  # 词汇表达小


input_x = tf.placeholder(tf.int32,[None,seq_length])

# 词向量映射
with tf.device('/cpu:0'):
    embedding = tf.get_variable('embedding', [vocab_size, embedding_dim])    # shape = (5000,64)
    embedding_inputs = tf.nn.embedding_lookup(embedding, input_x)  # shape = (?, 600,64)

with tf.name_scope("cnn"):
    # CNN layer
    w = tf.Variable(initial_value=tf.truncated_normal(shape=[kernel_size, embedding_dim, num_filters], stddev=0.1))
    conv1 = tf.nn.conv1d(embedding_inputs, w, stride=2,name='conv1',padding='SAME')  # conv1=[batch, round(n_sqs/stride), n_filers],stride是步长。
    conv2 = tf.layers.conv1d(embedding_inputs, num_filters, kernel_size, name='conv2')  # shape = (?, 596,256)
    # global max pooling layer
    gmp = tf.reduce_max(conv1, reduction_indices=[1], name='gmp')  # shape = (?, 256)


tf.global_variables_initializer().run()

x = np.random.randint(vocab_size, size=[batch_size,seq_length])
out = sess.run(conv1, feed_dict={input_x:x})
print(out)  #

# ----------------------------------cov2d to cov1d---------------------------------------------
"""
用cov2d实现 cov1d
ref:https://www.cnblogs.com/HITSZ/p/8721414.html
"""

import tensorflow as tf

sess = tf.InteractiveSession()

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1,1,1,1], padding='SAME')

def max_pool_1x2(x):
    return tf.nn.avg_pool(x, ksize=[1,1,2,1], strides=[1,1,2,1], padding='SAME')
'''
ksize = [x, pool_height, pool_width, x]
strides = [x, pool_height, pool_width, x]
'''

x = tf.Variable([[1,2,3,4]], dtype=tf.float32)
x = tf.reshape(x, [1,1,4,1])  #这一步必不可少，否则会报错说维度不一致；
'''
[batch, in_height, in_width, in_channels] = [1,1,4,1]
'''

W_conv1 = tf.Variable([1,1,1],dtype=tf.float32)  # 权重值
W_conv1 = tf.reshape(W_conv1, [1,3,1,1])  # 这一步同样必不可少
'''
[filter_height, filter_width, in_channels, out_channels]
'''

h_conv1 = conv2d(x, W_conv1)   # 结果：[4,8,12,11]

h_pool1 = max_pool_1x2(h_conv1)

tf.global_variables_initializer().run()

print(sess.run(h_conv1))  # 结果array([6,11.5])x

