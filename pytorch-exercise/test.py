#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     test.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-02-10
# brief:    
#
# cmd>e.g:  
# *****************************************************

import torch
from torch.autograd import Variable
import matplotlib.pyplot as plt
import torch.nn.functional as fu

tensor = torch.FloatTensor([[1,2],[3,4]])
variable = Variable(tensor, requires_grad=True)

t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)

print(tensor*tensor)
print(torch.mean(tensor*tensor))
v_out.backward()
print(variable)
print(variable.grad)
print(variable.data)
print(variable.data.numpy())


# 激励函数及画图
x = torch.linspace(-5,5,200)
x = Variable(x)
x_np = x.data.numpy()

y_relu = fu.relu(x).data.numpy()
y_sigmoid = fu.sigmoid(x).data.numpy()
y_tanh = fu.tanh(x).data.numpy()
y_softplus = fu.softplus(x).data.numpy()
# y_softmax = fu.softmax(x)

plt.figure(1, figsize=(8,6))
plt.subplot(221)
plt.plot(x_np,y_relu,c='red',label='relu')
plt.ylim(-1,5)
plt.legend(loc='best')


plt.subplot(222)
plt.plot(x_np,y_sigmoid,c='red',label='sigmoid')
plt.ylim(-0.2,1.2)
plt.legend(loc='best')

plt.subplot(223)
plt.plot(x_np,y_tanh,c='red',label='tanh')
plt.ylim(-1.2,1.2)
plt.legend(loc='best')

plt.subplot(224)
plt.plot(x_np,y_softplus,c='red',label='softplus')
plt.ylim(-0.2,6)
plt.legend(loc='best')

# plt.show()


# 回归曲线
x = torch.unsqueeze(torch.linspace(-1,1,100),dim=1)
y = x.pow(2)+0.2*torch.rand(x.size())
x,y = Variable(x),Variable(y)

# plt.scatter(x.data.numpy(), y.data.numpy())
# plt.show()
class Net(torch.nn.Module):
    def __init__(self,n_features,n_hidden,n_output):
        super(Net,self).__init__()
        self.hidden = torch.nn.Linear(n_features, n_hidden)
        self.predict = torch.nn.Linear(n_hidden,n_output)

    def forward(self,x):
        x = fu.relu(self.hidden(x))
        x = self.predict(x)
        return x

net = Net(1, 10, 1)
print(net)

# plt.ion()
# plt.show()

opt = torch.optim.SGD(net.parameters(),lr=0.2)
loss_func = torch.nn.MSELoss()
for t in range(100):
    prediction = net(x)
    loss = loss_func(prediction,y)

    opt.zero_grad()
    loss.backward()
    opt.step()
    print(loss.data)

#     if t%5 ==0:
#         plt.cla()
#         plt.scatter(x.data.numpy(),y.data.numpy())
#         plt.plot(x.data.numpy(),prediction.data.numpy(),'r-',lw=5)
#         plt.text(0.5,0,'Loss=%.4f' % float(loss.data.numpy()),fontdict={'size':20,'color':'red'})
#         plt.pause(0.1)
# plt.ioff()
# plt.show()




