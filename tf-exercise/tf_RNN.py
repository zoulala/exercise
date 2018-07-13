"""
ref:https://zhuanlan.zhihu.com/p/28196873
"""
import tensorflow as tf
import numpy as np

# 单步RNN：RNNCell
"""
我是中国人
你在做什么
是吗<eco><eco><eco>

假设隐藏层LSTM神经元数量为k，一次处理3句话，每句话序列长度为5(即时间维度)，字向量是n维则(即n个输入节点)：[batch ,n_steps ,word_embeding]=[3,5,n]
过程：（其中步骤1叫单步执行，相当于call方法，步骤1到3是多步执行，dynamic_rnn函数来实现）
    1、分别将batch的一个字输入网络(我、你、是),根据网络权重w0/b0(n*k个)计算 和 初始状态（h01、h02、h03），分别产生状态h11、h12、h13；
    2、分别将batch的第二个字输入网络（是、在、吗），根据网络权重w0/b0(n*k个)计算 和 状态（h11、h12、h13），分别产生状态h21、h22、h23；
    .
    .
    .
    3、计算完最后一个字后，将batch个样本产生的结果总和来进行权重w0/b0调整为-->w1/b1,一个batch结束
    4、进行下一个batch样本集计算，循环步骤1
    注意：batch中3句话分别进行计算相互不干扰，但共享权重。（也可以理解为分别单独计算第一句话进入网络，计算第二句话也进入网络，计算第三句话进入网络，只是用矩阵形式方便一起计算。
    且进行计算完3句话后，用总的误差来梯度调整权重，而不是分别每句话计算完就调整权重。这是batch用处所在）

"""
# cell = tf.nn.rnn_cell.BasicRNNCell(num_units=128) # state_size = 128
# print(cell.state_size) # 128
#
# inputs = tf.placeholder(np.float32, shape=(32, 100)) # 32 是 batch_size
# h0 = cell.zero_state(32, np.float32) # 通过zero_state得到一个全0的初始状态，形状为(batch_size, state_size)
# output, h1 = cell.__call__(inputs, h0) #调用call函数
#
# print(h1.shape) # (32, 128)

lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(num_units=128)
inputs = tf.placeholder(np.float32, shape=(32, 100)) # 32 是 batch_size
h0 = lstm_cell.zero_state(32, np.float32) # 通过zero_state得到一个全0的初始状态
output, h1 = lstm_cell.__call__(inputs, h0)  # call方法inputs必须是[batch_size,输入节点数]（即单步执行）

print(h1.h)  # shape=(32, 128)
print(h1.c)  # shape=(32, 128)


# 执行多步：tf.nn.dynamic_rnn
inputs2 = tf.placeholder(np.float32, shape=(32, 20, 100)) # 32 是 batch_size 20是序列长度，100是输入节点维数。shape = (batch_size, time_steps, input_size)
# initial_state: shape = (batch_size, cell.state_size)。初始状态。一般可以取零矩阵
initial_state = lstm_cell.zero_state(32, np.float32) # 通过zero_state得到一个全0的初始状态
outputs, state = tf.nn.dynamic_rnn(lstm_cell, inputs2, initial_state=initial_state)  # outputs，state为最后一步的输出和状态
print(state.h)  # shape=(32, 128)



# 堆叠RNNCell：MultiRNNCell
'''
很多时候，单层RNN的能力有限，我们需要多层的RNN。将x输入第一层RNN的后得到隐层状态h，这个隐层状态就相当于第二层RNN的输入，第二层RNN的隐层状态又相当于第三层RNN的输入，
以此类推。在TensorFlow中，可以使用tf.nn.rnn_cell.MultiRNNCell函数对RNNCell进行堆叠
'''
def get_a_cell():
    return tf.nn.rnn_cell.BasicRNNCell(num_units=128)  # 每调用一次这个函数就返回一个BasicRNNCell

cell = tf.nn.rnn_cell.MultiRNNCell([get_a_cell() for _ in range(3)])  # 用tf.nn.rnn_cell MultiRNNCell创建3层RNN
# 得到的cell实际也是RNNCell的子类
# 它的state_size是(128, 128, 128)
# (128, 128, 128)并不是128x128x128的意思
# 而是表示共有3个隐层状态，每个隐层状态的大小为128
print(cell.state_size) # (128, 128, 128)
# 使用对应的call函数
inputs = tf.placeholder(np.float32, shape=(32, 100)) # 32 是 batch_size
h0 = cell.zero_state(32, np.float32) # 通过zero_state得到一个全0的初始状态
output1, h1 = cell.call(inputs, h0)
print(h1) # tuple中含有3个32x128的向量
# 通过MultiRNNCell得到的cell并不是什么新鲜事物，它实际也是RNNCell的子类，因此也有call方法、state_size和output_size属性。同样可以通过tf.nn.dynamic_rnn来一次运行多步。


# 注意坑1：Output说明
'''
BasicRNNCell对照来看。h就对应了BasicRNNCell的state。那么，y是不是就对应了BasicRNNCell的output呢？答案是否定的
def call(self, inputs, state):
    """Most basic RNN: output = new_state = act(W * input + U * state + B)."""
    output = self._activation(_linear([inputs, state], self._num_units, True))
    return output, output   # call 源码，output和state是一样的。因此，我们还需要额外对输出定义新的变换，才能得到图中真正的输出y
    
再来看一下BasicLSTMCell的call函数定义（函数的最后几行）：
new_c = (
    c * sigmoid(f + self._forget_bias) + sigmoid(i) * self._activation(j))
new_h = self._activation(new_c) * sigmoid(o)

if self._state_is_tuple:
  new_state = LSTMStateTuple(new_c, new_h)
else:
  new_state = array_ops.concat([new_c, new_h], 1)
return new_h, new_state
只需要关注self._state_is_tuple == True的情况，因为self._state_is_tuple == False的情况将在未来被弃用。返回的隐状态是new_c和new_h的组合，而output就是单独的new_h。如果我们处理的是分类问题，那么我们还需要对new_h添加单独的Softmax层才能得到最后的分类概率输出。
'''



