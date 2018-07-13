'''
tf 练习1  ref:http://wiki.jikexueyuan.com/project/tensorflow-zh/get_started/introduction.html

一个基本的运行示例

2018-02-28 zlw
'''

'''这段很短的 Python 程序生成了一些三维数据, 然后用一个平面拟合它'''

import tensorflow as tf
import numpy as np

# 使用 NumPy 生成假数据(phony data), 总共 100 个点.
x_data = np.float32(np.random.rand(2, 100)) # 随机输入
y_data = np.dot([0.100, 0.200], x_data) + 0.300

# 构造一个线性模型
b = tf.Variable(tf.zeros([1]),name='b')
# b = tf.get_variable(name='b',initializer=tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b




# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化变量
init = tf.initialize_all_variables()

# 启动图 (graph)
sess = tf.Session()
sess.run(init)

# 拟合平面
for step in range(0, 201):
    sess.run(train)
    if step % 5 == 0:
        # print (step, sess.run(W), sess.run(b))
        print(step, sess.run([W,b]))  # 以列表的形式打印出w,b，，需要获取的多个 tensor 值，在 op 的一次运行中一起获得（而不是逐个去获取 tensor）
sess.close()
# 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]


