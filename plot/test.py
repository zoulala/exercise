#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     test.py
# author:   zlw2008ok@126.com
# date:     2022/10/14
# desc:     
#
# cmd>e.g.:  
# *****************************************************
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()