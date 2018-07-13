'''
tf 练习  ref:https://blog.csdn.net/sinat_33761963/article/details/62433234

tensorboard 练习
（py35环境下，运行程序后，在命令行输入：tensorboard --logdir=D:\pycharm\PyCharm Community Edition 2017.1.1\workspace\py35\exercise\tf-exercise\board_log）
打开浏览器localhost：6006

2018-04-25zlw
'''



import tensorflow as tf


max_step = 1000  # 最大迭代次数
learning_rate = 0.001   # 学习率
dropout = 0.9   # dropout时随机保留神经元的比例

data_dir = 'MNIST_data/'   # 样本数据存储的路径
log_dir = 'board_log/'    # 输出日志保存的路径


# 获得数据
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets(data_dir, one_hot=True)

# 创建session
sess = tf.InteractiveSession()

# 创建输入数据占位符
with tf.name_scope('input'):
    x = tf.placeholder(tf.float32, [None, 784], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, 10], name='y-input')

# 使用tf.summary.image保存图像信息
with tf.name_scope('input_reshape'):
    image_shaped_input = tf.reshape(x, [-1, 28, 28, 1])  # 将图像数据1*784的向量转变成28 * 28 * 1的原始像素，为了在tensorboard上还原出输入的特征数据对应的图片
    tf.summary.image('input', image_shaped_input, 10)  # tf.summary.image（）中传入的第一个参数是命名，第二个是图片数据，第三个是最多展示的张数，此处为10张

# 权重和偏置初始化函数
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)  # 标准差为0.1,正态分布的随机数
  return tf.Variable(initial)

def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

# 收录每次的参数信息
def variable_summaries(var):
    """Attach a lot of summaries to a Tensor (for TensorBoard visualization)."""
    with tf.name_scope('summaries'):
      # 计算参数的均值，并使用tf.summary.scaler记录
      mean = tf.reduce_mean(var)
      tf.summary.scalar('mean', mean)

      # 计算参数的标准差
      with tf.name_scope('stddev'):
        stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
      # 使用tf.summary.scaler记录记录下标准差，最大值，最小值
      tf.summary.scalar('stddev', stddev)
      tf.summary.scalar('max', tf.reduce_max(var))
      tf.summary.scalar('min', tf.reduce_min(var))
      # 用直方图记录参数的分布
      tf.summary.histogram('histogram', var)

# 构建神经网络层
def nn_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
    """Reusable code for making a simple neural net layer.
    It does a matrix multiply, bias add, and then uses relu to nonlinearize.
    It also sets up name scoping so that the resultant graph is easy to read,
    and adds a number of summary ops.
    input_tensor：特征数据 
    input_dim：输入数据的维度大小 
    output_dim：输出数据的维度大小(=隐层神经元个数） 
    layer_name：命名空间 
    act=tf.nn.relu：激活函数（默认是relu)
    """
    # 设置命名空间
    with tf.name_scope(layer_name):
      # 调用之前的方法初始化权重w，并且调用参数信息的记录方法，记录w的信息
      with tf.name_scope('weights'):
        weights = weight_variable([input_dim, output_dim])
        variable_summaries(weights)
      # 调用之前的方法初始化权重b，并且调用参数信息的记录方法，记录b的信息
      with tf.name_scope('biases'):
        biases = bias_variable([output_dim])
        variable_summaries(biases)
      # 执行wx+b的线性计算，并且用直方图记录下来
      with tf.name_scope('linear_compute'):
        preactivate = tf.matmul(input_tensor, weights) + biases
        tf.summary.histogram('linear', preactivate)
      # 将线性输出经过激励函数，并将输出也用直方图记录下来
      activations = act(preactivate, name='activation')
      tf.summary.histogram('activations', activations)

      # 返回激励层的最终输出
      return activations


#  创建隐藏层
hidden1 = nn_layer(x, 784, 500, 'layer1')

# 创建一个dropout层，,随机关闭掉hidden1的一些神经元，并记录keep_prob
with tf.name_scope('dropout'):
    keep_prob = tf.placeholder(tf.float32)
    tf.summary.scalar('dropout_keep_probability', keep_prob)
    dropped = tf.nn.dropout(hidden1, keep_prob)

# 创建一个输出层
y = nn_layer(dropped, 500, 10, 'layer2', act=tf.identity)  # 输入的维度是上一层的输出:500,输出的维度是分类的类别种类：10，激活函数设置为全等映射identity.（暂且先别使用softmax,会放在之后的损失函数中一起计算）

# 创建损失函数
with tf.name_scope('loss'):
    # 计算交叉熵损失（每个样本都会有一个损失）
    diff = tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y)
    with tf.name_scope('total'):
      # 计算所有样本交叉熵损失的均值
      cross_entropy = tf.reduce_mean(diff)

tf.summary.scalar('loss', cross_entropy)

# 训练，并计算准确率
with tf.name_scope('train'):
    train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)  # 使用AdamOptimizer优化器训练模型，最小化交叉熵损失

# 计算准确率,并用tf.summary.scalar记录准确率
with tf.name_scope('accuracy'):
    with tf.name_scope('correct_prediction'):
      # 分别将预测和真实的标签中取出最大值的索引，弱相同则返回1(true),不同则返回0(false)
      correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    with tf.name_scope('accuracy'):
      # 求均值即为准确率
      accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
tf.summary.scalar('accuracy', accuracy)

# 合并summary operation,
merged = tf.summary.merge_all()  # summaries合并
# 写到指定的磁盘路径中
train_writer = tf.summary.FileWriter(log_dir + '/train', sess.graph)
test_writer = tf.summary.FileWriter(log_dir + '/test')

# 运行初始化所有变量
tf.global_variables_initializer().run()

# 喂人的数据
def feed_dict(train):
    """Make a TensorFlow feed_dict: maps data onto Tensor placeholders."""
    if train:
      xs, ys = mnist.train.next_batch(100)
      k = dropout
    else:
      xs, ys = mnist.test.images, mnist.test.labels
      k = 1.0
    return {x: xs, y_: ys, keep_prob: k}

# 开始训练模型
for i in range(max_step):
    if i % 10 == 0:  # 记录测试集的summary与accuracy
      summary, acc = sess.run([merged, accuracy], feed_dict=feed_dict(False))
      test_writer.add_summary(summary, i)
      print('Accuracy at step %s: %s' % (i, acc))
    else:  # 记录训练集的summary
      if i % 100 == 99:  # Record execution stats
        run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
        run_metadata = tf.RunMetadata()
        summary, _ = sess.run([merged, train_step],
                              feed_dict=feed_dict(True),
                              options=run_options,
                              run_metadata=run_metadata)
        train_writer.add_run_metadata(run_metadata, 'step%03d' % i)
        train_writer.add_summary(summary, i)
        print('Adding run metadata for', i)
      else:  # Record a summary
        summary, _ = sess.run([merged, train_step], feed_dict=feed_dict(True))
        train_writer.add_summary(summary, i)
train_writer.close()
test_writer.close()

