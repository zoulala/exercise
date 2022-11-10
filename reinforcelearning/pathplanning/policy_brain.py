#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     policy_brain.py
# author:   zlw2008ok@126.com
# date:     2022/10/19
# desc:     
#
# cmd>e.g.:  
# *****************************************************

import random
import numpy as np
import torch
import torch.nn as nn
from torch.nn import functional as F
from torch.distributions import Categorical

# torch.manual_seed(1)  #随机数初始化种子
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class Policy(nn.Module):

    def __init__(self, state_space, action_space):
        super(Policy, self).__init__()

        self.fc1 = nn.Linear(state_space, 128)
        self.fc2 = nn.Linear(128,64)
        self.fc3 = nn.Linear(64, action_space)
        self.dropout = nn.Dropout(0.2)

        # torch.nn.init.normal_(self.fc1.weight, mean=0, std=1)  # 表示生成的随机数用来替换weight的原始数据
        # torch.nn.init.normal_(self.fc2.weight, mean=0, std=10)  # 表示生成的随机数用来替换weight的原始数据
        # torch.nn.init.normal_(self.fc3.weight, mean=0, std=1)  # 表示生成的随机数用来替换weight的原始数据

    def forward(self, x):
        # x = F.relu(self.fc1(x))
        x = F.sigmoid(self.fc1(x))
        # x = self.dropout(x)
        x = F.sigmoid(self.fc2(x))
        x = self.fc3(x)
        return F.softmax(x, dim=1)

    def act(self, state, i_episode):
        # state = state-50
        state = torch.from_numpy(state).float().unsqueeze(0).to(device)
        probs = self.forward(state).to(device)
        m = Categorical(probs)
        action = m.sample()
        log_p = m.log_prob(action)
        ra = 1. / (1. + np.exp(-i_episode/10000))  # 0.9
        if random.random()>ra:
            action = torch.tensor(random.randint(0,5))
            log_p = m.log_prob(action)

        return action.item(), log_p

    def best_act(self, state):
        # state = state-50
        state = torch.from_numpy(state).float().unsqueeze(0).to(device)
        probs = self.forward(state).to(device)
        m = Categorical(probs)
        action= torch.argmax(probs, dim=1)
        return action.item(), m.log_prob(action)
