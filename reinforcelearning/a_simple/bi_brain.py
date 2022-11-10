#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     bi_brain.py
# author:   zlw2008ok@126.com
# date:     2022/10/19
# desc:     
#
# cmd>e.g.:  
# *****************************************************
import torch.nn as nn
from torch.nn import functional as F

# torch.manual_seed(1)

class Policy(nn.Module):
    def __init__(self, state_space, action_space, gamma):
        super(Policy, self).__init__()

        self.fc1 = nn.Linear(state_space, 4)
        # self.fc2 = nn.Linear(128,64)
        self.fc3 = nn.Linear(4, action_space)
        # self.dropout = nn.Dropout(0.3)

        self.gamma = gamma
        self.saved_log_probs = []
        self.rewards = []

    def forward(self, x):

        x = F.relu(self.fc1(x))
        # x = self.dropout(x)
        # x = F.relu(self.fc2(x))
        x = self.fc3(x)
        x = F.softmax(x, dim=1)

        return x
