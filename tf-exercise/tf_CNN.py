"""
ref:https://blog.csdn.net/cxmscb/article/details/71023576
"""


import tensorflow as tf
from sklearn.datasets import load_digits
import numpy as np

digits = load_digits()
X_data = digits.data.astype(np.float32)
Y_data = digits.target.astype(np.float32).reshape(-1,1)
print (X_data.shape)
print (Y_data.shape)

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
scaler = MinMaxScaler()
X_data = scaler.fit_transform(X_data)
Y = OneHotEncoder().fit_transform(Y_data).todense() #one-hot编码

# 转换为图片的格式 （batch，height，width，channels）
X = X_data.reshape(-1,8,8,1)
batch_size = 8 # 使用MBGD算法，设定batch_size为8

def generatebatch(X,Y,n_examples, batch_size):
    for batch_i in range(n_examples // batch_size):
        start = batch_i*batch_size
        end = start + batch_size
        batch_xs = X[start:end]
        batch_ys = Y[start:end]
        yield batch_xs, batch_ys # 生成每一个batch


tf.reset_default_graph()
# 输入层
tf_X = tf.placeholder(tf.float32,[None,8,8,1])
tf_Y = tf.placeholder(tf.float32,[None,10])

# 卷积层+激活层
conv_filter_w1 = tf.Variable(tf.random_normal([3, 3, 1, 10]))
conv_filter_b1 =  tf.Variable(tf.random_normal([10]))
relu_feature_maps1 = tf.nn.relu(\
                tf.nn.conv2d(tf_X, conv_filter_w1,strides=[1, 1, 1, 1], padding='SAME') + conv_filter_b1)

# 池化层
max_pool1 = tf.nn.max_pool(relu_feature_maps1,ksize=[1,3,3,1],strides=[1,2,2,1],padding='SAME')

# 卷积层
conv_filter_w2 = tf.Variable(tf.random_normal([3, 3, 10, 5]))
conv_filter_b2 =  tf.Variable(tf.random_normal([5]))
conv_out2 = tf.nn.conv2d(relu_feature_maps1, conv_filter_w2,strides=[1, 2, 2, 1], padding='SAME') + conv_filter_b2
print (conv_out2)

# BN归一化层+激活层
batch_mean, batch_var = tf.nn.moments(conv_out2, [0, 1, 2], keep_dims=True)
shift = tf.Variable(tf.zeros([5]))
scale = tf.Variable(tf.ones([5]))
epsilon = 1e-3
BN_out = tf.nn.batch_normalization(conv_out2, batch_mean, batch_var, shift, scale, epsilon)
print (BN_out)
relu_BN_maps2 = tf.nn.relu(BN_out)

# 池化层
max_pool2 = tf.nn.max_pool(relu_BN_maps2,ksize=[1,3,3,1],strides=[1,2,2,1],padding='SAME')

# 将特征图进行展开
max_pool2_flat = tf.reshape(max_pool2, [-1, 2*2*5])

# 全连接层
fc_w1 = tf.Variable(tf.random_normal([2*2*5,50]))
fc_b1 =  tf.Variable(tf.random_normal([50]))
fc_out1 = tf.nn.relu(tf.matmul(max_pool2_flat, fc_w1) + fc_b1)

# 输出层
out_w1 = tf.Variable(tf.random_normal([50,10]))
out_b1 = tf.Variable(tf.random_normal([10]))
pred = tf.nn.softmax(tf.matmul(fc_out1,out_w1)+out_b1)

loss = -tf.reduce_mean(tf_Y*tf.log(tf.clip_by_value(pred,1e-11,1.0)))

train_step = tf.train.AdamOptimizer(1e-3).minimize(loss)

y_pred = tf.arg_max(pred,1)
bool_pred = tf.equal(tf.arg_max(tf_Y,1),y_pred)

accuracy = tf.reduce_mean(tf.cast(bool_pred,tf.float32)) # 准确率

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(1000): # 迭代1000个周期
        for batch_xs,batch_ys in generatebatch(X,Y,Y.shape[0],batch_size): # 每个周期进行MBGD算法
            sess.run(train_step,feed_dict={tf_X:batch_xs,tf_Y:batch_ys})
        if(epoch%100==0):
            res = sess.run(accuracy,feed_dict={tf_X:X,tf_Y:Y})
            print (epoch,res)
    res_ypred = y_pred.eval(feed_dict={tf_X:X,tf_Y:Y}).flatten() # 只能预测一批样本，不能预测一个样本
    print (res_ypred)
    '''在第100次个batch size 迭代时，准确率就快速接近收敛了，这得归功于Batch Normalization 的作用！需要注意的是，这个模型还不能用来预测单个样本，因为在进行BN层计算时，单个样本的均值和方差都为0，会得到相反的预测效果，解决方法详见归一化层。'''

from sklearn.metrics import  accuracy_score
print (accuracy_score(Y_data,res_ypred.reshape(-1,1)))
