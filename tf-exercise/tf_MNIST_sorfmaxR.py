'''
tf 练习  ref:http://wiki.jikexueyuan.com/project/tensorflow-zh/tutorials/mnist_beginners.html

MNIST手写数字sorfmax regression分类（线性回归经过sorfmax转成概率输出，即逻辑回归）

2018-02-28 zlw
'''

'''MNIST是一个入门级的计算机视觉数据集，它包含各种手写数字图片,28*28的灰度像素数据输入，10维输出标签用one-hot向量表示[0 1 0 0 0 0 0 0 0 0]'''

# 获得数据
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# 构建tf模型计算图
import tensorflow as tf
x = tf.placeholder(tf.float32, [None, 784])  # 定义输入变量占位符，样本数量不限
W = tf.Variable(tf.zeros([784,10]))  # 定义权重变量
b = tf.Variable(tf.zeros([10]))  # 定义偏移变量
y = tf.nn.softmax(tf.matmul(x,W) + b)  # x*W + b经过softmax转换成概率   softmax函数定义：softmax(x) = exp(xi)/sum(exp(x1),exp(x2)...exp(xi))

y_ = tf.placeholder("float", [None,10])  # y_是真实分类标签
cross_entropy = -tf.reduce_sum(y_*tf.log(y))  # 用交叉熵来作为损失函数loss,计算交叉熵

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)  # 梯度下降算法（gradient descent algorithm）以0.01的学习速率最小化交叉熵

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)  # 初始化session

# 训练模型
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)  # 在训练数据中随机100个样本进行训练
    _,ys = sess.run([train_step,y], feed_dict={x: batch_xs, y_: batch_ys})
    # print(sum(ys[0]))


# 评价模型
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))  # 这行代码会给我们一组布尔值[True, False, True, True]
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))  # cast将[True, False, True, True] 会变成 [1,0,1,1] ，reduce_mean取平均值后得到 0.75.
print (sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))  # 测试数据进行测试