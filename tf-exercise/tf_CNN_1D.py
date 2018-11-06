"""
1、比较了tf.nn.conv1d和tf.layters.conv1d 两种方法的实现及参数。
ref:https://blog.csdn.net/john_xyz/article/details/79210088
2、用cov2d实现 cov1d   ref:https://www.cnblogs.com/HITSZ/p/8721414.html
"""

import tensorflow as tf
import numpy as np
sess = tf.InteractiveSession()


# --------------- tf.nn.conv1d  -------------------
# inputs=tf.ones((64,10,3))  # [batch, n_sqs, embedsize]
# w=tf.constant(1,tf.float32,(5,3,32))  # [w_high, embedsize, n_filers]
# conv1 = tf.nn.conv1d(inputs,w,stride=2 ,padding='SAME')  # conv1=[batch, round(n_sqs/stride), n_filers],stride是步长。
#
# tf.global_variables_initializer().run()
# out = sess.run(w)
# print(out)

# --------------- tf.nn.conv1d  &  tf.layers.conv1d  -------------------
batch_size = 32
embedding_dim = 64  # 词向量维度
seq_length = 600  # 序列长度
num_classes = 10  # 类别数
num_filters = 256  # 卷积核数目
kernel_size = 3  # 卷积核尺寸
vocab_size = 50  # 词汇表达小


input_x = tf.placeholder(tf.int32,[None,seq_length])
input_y = tf.placeholder(tf.int32,[None])
# 词向量映射
with tf.device('/cpu:0'):
    embedding = tf.get_variable('embedding', [vocab_size, embedding_dim])    # shape = (5000,64)
    embedding_inputs = tf.nn.embedding_lookup(embedding, input_x)  # shape = (?, 600,64)
    one_hot_y = tf.one_hot(input_y, num_classes)

with tf.name_scope("cnn"):
    # CNN layer
    # 只在序列维度上进行上下滑动（卷积），embedding维度全包括。
    # 比如一个句子是10个字，embedding后是[10*embedsize]的矩阵，卷积核尺寸是3，即窗口大小是3*embedsize，卷积核数量是100，滑动步长是2，
    # padding='SAME'时，输出[10/2  * 100]维的矩阵，padding='valid'时，输出[round(（10-3）/2)  * 100]维的矩阵
    # 一般卷积核尺寸选择多个，如2、3、4相当于代表2-gram 3-gram 4-gram信息，也可以选择1，代表字粒度信息
    # ref:https://www.jianshu.com/p/a8a573a0e0fa

    w = tf.Variable(initial_value=tf.truncated_normal(shape=[kernel_size, embedding_dim, num_filters], stddev=0.1))
    conv1 = tf.nn.conv1d(embedding_inputs, w, stride=2,name='conv1',padding='SAME')  # conv1=[batch, round(n_sqs/stride), n_filers],stride是步长。
    conv2 = tf.layers.conv1d(embedding_inputs, num_filters, kernel_size,strides=2, padding='valid',name='conv2')  # shape = (?, 596,256)

    # stride max pooling
    convs = tf.expand_dims(conv1,axis=-1)  # shape=[?,596,256,1]
    smp = tf.nn.max_pool(value=convs, ksize=[1, 3, num_filters, 1],strides=[1, 2, 1, 1],padding='SAME')  # shape=[?,299,256,1]
    smp = tf.squeeze(smp,-1)  #  shape=[?,299,256]
    h = tf.shape(smp)[1]
    smp = tf.reshape(smp,shape=(-1, h*256))
    # global max pooling layer
    gmp = tf.reduce_max(conv1, reduction_indices=[1], name='gmp')  # shape = (?, 256)

    # full contact layer
    fc_input = smp  # gmp
    fc_output = tf.layers.dense(fc_input, num_classes, use_bias=True)
    fc_output = tf.nn.relu(fc_output)


tf.global_variables_initializer().run()

x = np.random.randint(vocab_size, size=[batch_size,seq_length])
y = np.array([3,1,6])
out = sess.run(conv1, feed_dict={input_x:x,input_y:y})
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

