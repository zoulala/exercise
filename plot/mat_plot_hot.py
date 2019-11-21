#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     mat_plots.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2019-11-21
# brief:    https://blog.csdn.net/jp_zhou256/article/details/85685047
#
# cmd>e.g:
# *****************************************************
import  matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 输出所有字体名
a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
for i in a:
    print(i)

# 设置自定义字体
plt.rcParams['font.family'] = ['Heiti']
print(dir(plt.cm))


data = np.random.rand(5,6)
print(data)


def hot_pcolor(data, xticks, yticks):
    plt.pcolor(data,cmap=plt.cm.hot, # 指定填充色
               edgecolors = 'white' # 指点单元格之间的边框色
               )
    # plt.tick_params(top='on', right='on', which='both')
    # 添加x轴和y轴刻度标签(加0.5是为了让刻度标签居中显示)
    plt.xticks(np.arange(6)+0.5,xticks,rotation=20)
    plt.yticks(np.arange(5)+0.5,yticks)
    plt.show()

def hot_im(data, xticks, yticks):
    plt.imshow(data,cmap=plt.cm.Blues, # 指定填充色
               )
    plt.axis([-0.5, 5.5, - 0.5, 4.5])  # 表示要显示图形的范围
    plt.xticks(np.arange(6),xticks)
    plt.yticks(np.arange(5),yticks)
    plt.show()

def hot_mat(data, xticks, yticks):
    # fig, ax = plt.subplots()
    # ax.matshow(data,cmap=plt.cm.Blues, # 指定填充色
    #             interpolation='none', vmin=0, vmax=1,
    #
    #            )
    # ax.set_xlim(-0.5, 5.5)
    # ax.set_ylim(-0.5, 4.5)
    # ax.set_xticks(np.arange(6))
    # ax.set_yticks(np.arange(5))
    # ax.set_xticklabels(xticks)
    # ax.set_yticklabels(yticks)
    # plt.show()
    plt.matshow(data,cmap=plt.cm.Blues, # 指定填充色
                interpolation='none', vmin=0, vmax=1,
               )
    plt.axis([-0.5, 5.5,- 0.5, 4.5])  # 表示要显示图形的范围
    plt.xticks(ticks=np.arange(6),labels=xticks)
    plt.yticks(ticks=np.arange(4,-1,-1),labels=yticks)
    plt.colorbar(shrink=0.5)
    plt.show()


def hot_con(data, xticks, yticks):
    plt.contourf(data,cmap=plt.cm.Blues, # 指定填充色
               edgecolors = 'white' # 指点单元格之间的边框色
               )
    # 添加x轴和y轴刻度标签(加0.5是为了让刻度标签居中显示)
    plt.xticks(np.arange(6)+0.5,xticks)
    plt.yticks(np.arange(5)+0.5,yticks)
    plt.show()

xticks = list('一二三四五六')
yticks = list('一二三四五')
hot_con(data, xticks, yticks)
hot_pcolor(data, xticks, yticks)
hot_im(data, xticks, yticks)
hot_mat(data, xticks, yticks)