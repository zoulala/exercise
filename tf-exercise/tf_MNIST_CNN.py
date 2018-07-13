'''
tf 练习  ref:http://wiki.jikexueyuan.com/project/tensorflow-zh/tutorials/mnist_pros.html

MNIST手写数字sorfmax regression分类（线性回归经过sorfmax转成概率输出）

2018-02-28 zlw
'''

# 获得数据
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


# 通过InteractiveSession类来启动图
import tensorflow as tf
sess = tf.InteractiveSession()  # 这里，我们使用更加方便的InteractiveSession类。通过它，你可以更加灵活地构建你的代码。它能让你在运行图的时候，插入一些计算图，这些计算图是由某些操作(operations)构成的。这对于工作在交互式环境中的人们来说非常便利，比如使用IPython。如果你没有使用InteractiveSession，那么你需要在启动session之前构建整个计算图，然后启动该计算图。

# 构建Softmax 回归模型
x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))


sess.run(tf.initialize_all_variables())

y = tf.nn.softmax(tf.matmul(x,W) + b)
cross_entropy = -tf.reduce_sum(y_*tf.log(y))  # 注意，tf.reduce_sum把minibatch里的每张图片的交叉熵值都加起来了。我们计算的交叉熵是指整个minibatch的。

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)   # 梯度下降算法（gradient descent algorithm）以0.01的学习速率最小化交叉熵


# 训练模型
for i in range(1000):
    batch = mnist.train.next_batch(50)
    train_step.run(feed_dict={x: batch[0], y_: batch[1]})  # 可以用feed_dict来替代任何张量，并不仅限于替换占位符

# 评价模型
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))  # 这行代码会给我们一组布尔值[True, False, True, True]
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))  # cast将[True, False, True, True] 会变成 [1,0,1,1] ，reduce_mean取平均值后得到 0.75.
print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))  # 测试数据进行测试,只有91%正确率

'''以上只有91%正确率，下面用一个稍微复杂的模型：卷积神经网络来改善效果。这会达到大概99.2%的准确率。
'''
# ------------构建一个多层卷积网络----------------

# 权重和偏置初始化函数
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

# 卷积和池化
def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')  #  [batch , in_height , in_width, in_channels]，in_height , in_width,移动步长；“SAME”表示采用填充的方式，简单地理解为以0填充边缘，“VALID”表示采用不填充的方式，多余地进行丢弃

def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
strides = [1, 2, 2,
           1], padding = 'SAME')  # x:[batch, height, width, channels],ksize：表示池化窗口的大小：一个长度为4的一维列表，一般为[1, height, width, 1]，因不想在batch和channels上做池化，则将其值设为1。

# 第一层卷积，（总参数个数（5*5+1）*通道数*32）
W_conv1 = weight_variable([5, 5, 1, 32])  # 5*5大小的卷积核，1个通道（灰度图像1通道，RGB为3通道），32个卷积核
b_conv1 = bias_variable([32])  # 32个偏置

x_image = tf.reshape(x, [-1,28,28,1])  # [batch , in_height , in_width, in_channels]，结果大小【28,28,1】

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)  # 总参数个数（5*5+1）*32   。 结果大小【28,28,32】
h_pool1 = max_pool_2x2(h_conv1)  # 把x_image和权值向量进行卷积，加上偏置项，然后应用ReLU激活函数，最后进行max pooling.结果大小【14,14,32】

# 第二层卷积
W_conv2 = weight_variable([5, 5, 32, 64])  # 第一层32个卷积核产生了32个特征图，因此有32个通道，并用64个卷积核将产生64个特征图
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)  # 结果大小【14,14,64】
h_pool2 = max_pool_2x2(h_conv2)  # 结果大小【7,7,64】

# 密集连接层
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)  # 结果大小【1,1024】

# Dropout
keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 输出层
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])

y_conv=tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)  # 结果大小【1,10】

# 训练和评估模型
cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)  # ADAM优化器来做梯度最速下降
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
sess.run(tf.initialize_all_variables())


for i in range(20000):
  batch = mnist.train.next_batch(50)
  if i%100 == 0:
    train_accuracy = accuracy.eval(feed_dict={
        x:batch[0], y_: batch[1], keep_prob: 1.0})
    print("step %d, training accuracy %g"%(i, train_accuracy))

  train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print("test accuracy %g"%accuracy.eval(feed_dict={
    x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))
