#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     bi_run.py
# author:   zlw2008ok@126.com
# date:     2022/10/19
# desc:     
#
# cmd>e.g.:  
# *****************************************************


import random
import torch
import torch.nn as nn
import numpy as np
from itertools import count
import matplotlib.pyplot as plt
from torch.distributions import Categorical
from torch.autograd import Variable
from bi_env import Bi
from bi_brain import Policy

# torch.manual_seed(1)
plt.ion()

env = Bi()
action_space = 2
state_space = 1

learning_rate = 0.01
gamma = 0.98
max_steps = 1000

eps = np.finfo(np.float32).eps.item()

policy = Policy(state_space, action_space, gamma)
optimizer = torch.optim.Adam(policy.parameters(), lr=learning_rate)
# criterion = nn.BCELoss()  # F.binary_cross_entropy, 概率0～1之间
# criterion = nn.MSELoss()  # 均方根误差
criterion = nn.CrossEntropyLoss()

def selct_action(state):
    state = torch.from_numpy(state).float().unsqueeze(0)
    probs = policy(state)
    c = Categorical(probs)
    action = c.sample()

    policy.saved_log_probs.append(c.log_prob(action))
    action = action.item()

    return action

def main():

    episode_durations = []
    #Batch_history
    state_pool = []
    action_pool = []
    reward_pool = []
    label_pool = []
    steps = 0

    for episode in range(60000):
        state = env.reset()

        for t in count():
            action = selct_action(state)
            state_pool.append(state)
            state, reward ,done = env.step(action)
            reward = -1 if done else reward
            # env.render()

            # state_pool.append(state)
            action_pool.append(float(action))
            if reward <0:
                if action==0:
                    label_pool.append(1)
                else:
                    label_pool.append(0)
            else:
                if action==0:
                    label_pool.append(0)
                else:
                    label_pool.append(1)
            steps += 1

            if done:
                episode_durations.append(t + 1)
                print("Episode {}, live time = {}".format(episode, t))
                # print(action_pool)

                # plot(rewards)
                break
        if episode >0 and episode % 50 == 0:
            # gradiend desent

            ## optimizer.zero_grad()
            ## ----------- 单步调优方式 ----------
            for i in range(steps): # 单步调优
                state = state_pool[i]
                state = torch.from_numpy(state).float().unsqueeze(0)
                # action = Variable(torch.FloatTensor([action_pool[i]]))
                # reward = reward_pool[i]

                probs = policy(state)
                action_label = torch.tensor([label_pool[i],],)
                # c = Categorical(probs)
                loss = criterion(probs, action_label)
                # print(loss)

                # loss = -c.log_prob(action) * reward
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()  # 单步调优

            ## ----------- batch调优方式 ----------
            # batch_state = torch.tensor(state_pool, dtype=torch.float32)
            # probs = policy(batch_state)
            # batch_label = torch.tensor(label_pool)
            # loss = criterion(probs, batch_label)
            # # print(loss)
            # optimizer.zero_grad()
            # loss.backward()
            # optimizer.step()



            state_pool = []
            action_pool = []
            label_pool = []
            steps = 0

if __name__ == '__main__':
    main()
