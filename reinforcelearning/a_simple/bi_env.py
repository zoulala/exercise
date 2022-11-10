#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     bi_env.py
# author:   zlw2008ok@126.com
# date:     2022/10/19
# desc:     
#
# cmd>e.g.:  
# *****************************************************

import numpy as np
class Bi(object):
    def __init__(self):
        self.state = -1

    def reset(self):
        self.state = -1
        return np.array([self.state,])

    def step(self, action):
        done = False
        reward = 0
        if action==0:
            if self.state==-1:
                self.state = -1
                done = True
                reward = -1
            elif self.state==1:
                self.state = -1
                reward = 1

        elif action==1:
            if self.state == -1:
                self.state = 1
                reward = 1
            elif self.state == 1:
                self.state = 1
                reward = -1
                done = True

        return np.array([self.state,]), reward, done

if __name__=="__main__":
    bo = Bi()

    for action in [0,0,1,0,1,1,1,0]:
        state, reward, done = bo.step(action)
        print(state, reward, done)
