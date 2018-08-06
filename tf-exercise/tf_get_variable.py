"""
@author: zlw

变量生成之tf.get_variable与tf.variable_scope  reuse参数
"""

import tensorflow as tf

v1 = tf.get_variable("v", [1])
print(v1.name)  # v:0


with tf.variable_scope("a"):  #reuse 默认False
    v2 = tf.get_variable("v", [1], initializer=tf.constant_initializer(1.0))
    print(v2.name)  # a/v:0

# with tf.variable_scope("a"):
#     v3 = tf.get_variable("v", [1])   # 报错 ValueError: Variable a/v already exists,

with tf.variable_scope("a", reuse=True):
    v4 = tf.get_variable("v", [1])
    print(v4 == v2)  # True

# with tf.variable_scope("b", reuse=True):
#     v5 = tf.get_variable("v",[1])  # 报错 ValueError: Variable b/v does not exist, or was not created with tf.get_variable().reuse=False不报错


with tf.variable_scope("a") as scope:
    with tf.variable_scope("b"):
        v6 = tf.get_variable("v", [1])
        print(v6.name)  # a/b/v:0

    scope.reuse_variables()  # 设置reuse = True
    v7 = tf.get_variable("v", [1])
    print(v7.name)  # a/v:0

# with tf.variable_scope(""):
#     v8 = tf.get_variable("v",[1])  # 会报错，因为名称为空的命名空间，等价于v1的情况，a已经存在了。而这里reuse为None，不能复用，于是报错
#     print(v8.name)


with tf.variable_scope("", reuse=True):
    v9 = tf.get_variable("a/b/v", [1])
    print(v9.name)  # a/b/v:0
    print(v2.name)  # a/v:0


    v10 = tf.get_variable("v", [1])
    print(v10.name)  # v:0


