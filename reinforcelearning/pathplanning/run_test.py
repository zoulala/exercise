#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     run_test.py
# author:   zlw2008ok@126.com
# date:     2022/11/2
# desc:     
#
# cmd>e.g.:  
# *****************************************************

import numpy as np
import torch
import matplotlib.pyplot as plt
from pathway_env import PathWayEnv
from matplotlib.animation import FuncAnimation
import json

env = PathWayEnv(num_site=5,num_plane=1)


with open('models/scores_results.json', 'r') as f:
    _dic = json.load(f, )
    scores = _dic['scores'][:300]
    scores_means = _dic['scores_means'][:]
    sites_locations = _dic['sites_locations']
    sites_rates = _dic['sites_rates']

env.set_sites(sites_locations, sites_rates)

actions = []
rewards1 = []
info = ''
state = env.reset()

# env.render()
policy = torch.load('models/policyNet.pkl')
for t in range(100):
    action, log_prob = policy.best_act(state)
    state, reward, done, info = env.step(action)
    # env.render()
    actions.append(action)
    rewards1.append(1)
    if done:
        break
print(actions, info)


# plot
fig = plt.figure()
ax1 = fig.add_subplot(111)
# ax2 = fig.add_subplot(122)

ax1.plot(np.arange(1, len(scores_means) + 1), scores_means)
plt.ylabel('mean scores')
plt.xlabel('training epochs')
plt.savefig('models/mean_scores.jpg')


# plot
fig = plt.figure()
ax1 = fig.add_subplot(111)
# ax2 = fig.add_subplot(122)

x,y = zip(*sites_locations)
x = list(x)
y = list(y)
x.insert(0,0)
y.insert(0,0)

lo=ax1.scatter(0, 0, s=80,  c='red', marker='^', cmap=plt.cm.Spectral, alpha=1.0, label="原点位置")
ll=ax1.scatter(x[1:], y[1:], s=60,  c='blue', marker='o', cmap=plt.cm.Spectral, alpha=0.5, label="医疗站点")
lp = ax1.scatter(0,0, s=80, c='g', marker='*', cmap=plt.cm.Spectral, alpha=1.0, label="飞机位置")
plt.legend((ll, lo, lp), ('sites', 'home', 'plane'), scatterpoints=1, loc='upper left', ncol=3, fontsize=8)


plt.xlim((-1.5, 11))
plt.ylim((-1.5, 11))

m = len(x)
text = [str(i) for i in range(m)]
# plt.annotate('✈️', (0, 0+0.4),fontsize=20)  # 原点
for i in range(1,m):
    plt.annotate(text[i], (x[i], y[i] + 0.2),fontsize=10)


# ax2.plot(np.arange(1, len(scores_means) + 1), scores_means)
plt.ylabel('y')
plt.xlabel('x')

xx = []
yy = []
line1, = ax1.plot(xx, yy,"r--")  # 获取折线图对象，逗号不可少，如果没有逗号，得到的是元组
def update(n):  # 更新函数

    xx.append(x[n] )  # 添加X轴坐标
    yy.append(y[n])  # 添加Y轴坐标

    line1.set_xdata(xx)  # 改变线条y的坐标值
    line1.set_ydata(yy)  # 改变线条y的坐标值
    # ax.plot(xx,yy , "r--")  # 绘制折线图
    # fig.plot(xx,yy , "r--")  # 绘制折线图

    lp.set_offsets([x[n], y[n]+0.4])
    # plt.annotate('✈️', (x[n], y[n] + 0.4), fontsize=20)  # 原点
    if len(xx)>3:
        xx.pop(0)
        yy.pop(0)



ani = FuncAnimation(fig, update, frames=actions, interval=500, blit=False, repeat=False)  # 创建动画效果
plt.show()  # 显示图片 作者：手把手教你学编程 https://www.bilibili.com/read/cv13169116 出处：bilibili

ani.save("models/movie.gif",writer='pillow')
ani.save("models/movie.gif", writer="imagemagick")
# plt.show()

