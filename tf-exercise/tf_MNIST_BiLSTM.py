

import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

learning_rate = 0.01
max_samples = 400000
batch_size = 128
display_step = 10

n_input = 28
n_steps = 28
n_hidden = 256
n_classes = 10

x = tf.placeholder(tf.float32, [None, n_steps, n_input])
y = tf.placeholder(tf.float32, [None, n_classes])

weights = tf.Variable(tf.random_normal([2 * n_hidden, n_classes]))
biases = tf.Variable(tf.random_normal([n_classes]))


def BiRNN(x, weights, biases):
    x = tf.transpose(x, [1, 0, 2])
    x = tf.reshape(x, [-1, n_input])
    x = tf.split(x, n_steps)

    lstm_fw_cell = tf.contrib.rnn.BasicLSTMCell(n_hidden, forget_bias=1.0)
    lstm_bw_cell = tf.contrib.rnn.BasicLSTMCell(n_hidden, forget_bias=1.0)

    outputs, _, _ = tf.contrib.rnn.static_bidirectional_rnn(
    lstm_fw_cell,
    lstm_bw_cell,
    x,
    dtype=tf.float32
    )
    return tf.matmul(outputs[-1], weights) + biases

pred = BiRNN(x, weights, biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred,
labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    step = 1
    while step * batch_size < max_samples:
        batch_x, batch_y = mnist.train.next_batch(batch_size)
        batch_x = batch_x.reshape((batch_size, n_steps, n_input))
        sess.run(optimizer, feed_dict={x: batch_x, y: batch_y})
        if step % display_step == 0:
            acc = sess.run(accuracy, feed_dict={x: batch_x, y: batch_y})
            loss = sess.run(cost, feed_dict={x: batch_x, y: batch_y})
            print ("Iter" + str(step * batch_size) + ", Minibatch Loss=" + \
            "{:.6f}".format(loss) + ", Training Accuracy= " + \
            "{:.5f}".format(acc))
        step += 1
    print ("Optimization Finishes!")

    test_len = 50000
    test_data = mnist.test.images[:test_len].reshape((-1, n_steps, n_input))
    test_label = mnist.test.labels[:test_len]
    print ("Testing accuracy:",
    sess.run(accuracy, feed_dict={x: test_data, y: test_label}))


'''
这里选择了400000个sample进行训练，图像按行读入像素序列(总共n_step=28行)，每128个样本看成一个batch做一次BPTT，每10个batch打印一次training loss。

Iter396800, Minibatch Loss=0.038339, Training Accuracy= 0.98438
Iter398080, Minibatch Loss=0.007602, Training Accuracy= 1.00000
Iter399360, Minibatch Loss=0.024104, Training Accuracy= 0.99219
Optimization Finishes!
取50000个样本作为测试集，准确率为：

('Testing accuracy:', 0.98680007)
可以发现，双向LSTM做图像分类虽然也有不错的性能，但是还是比CNN略微逊色。主要原因应该还是因为图像数据属于层次性比较高的数据，CNN能够逐层抽取图像的层次特征，从而达到比较高的精度。
但是可以想象，对于时序性比较强的无空间结构数据，RNN会有更加出色的表现。

===================

CNN是做图像识别的，对彩票一点用都没有。彩票预测分为两种，一直是M选N型，比如双色球，大乐透，另外一种是M选1型，比如福彩3d在各位上选一个。

M选1型 的可以用非线性回归算法进行预测。KNN这个是典型的非线下回归算法，测试效果并不理想。贝叶斯，随机森林，SVM, GBDT可以测试看看。

'''