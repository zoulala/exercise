#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     run.py
# author:   zlw2008ok@126.com
# date:     2022/10/19
# desc:     
#
# cmd>e.g.:  
# *****************************************************

import random
import torch
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

from pathway_env import PathWayEnv
from policy_brain import Policy

plt.ion()

env = PathWayEnv(num_site=5,num_plane=1)
action_space = len(env.action_space)
state_space = env.env_state.shape[0]
env.render()

# eps = np.finfo(np.float32).eps.item()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

policy = Policy(state_space, action_space).to(device)
optimizer = torch.optim.Adam(policy.parameters(), lr=0.0001)

def reinforce(n_episodes=500000, max_t=100, gamma=0.9, print_every=300):
    scores_deque = deque(maxlen=100)
    scores = []
    scores_means = []
    for i_episode in range(1, n_episodes + 1):
        saved_log_probs = []
        rewards = []
        state = env.reset()
        policy.train()
        for t in range(max_t):
            action, log_prob = policy.act(state, i_episode)
            saved_log_probs.append(log_prob)
            state, reward, done, _ = env.step(action)
            rewards.append(1)
            if done:
                break
        scores_deque.append(sum(rewards))
        # scores.append(sum(rewards))

        discounts = [gamma ** i for i in range(len(rewards) + 1)]
        R = sum([a * b for a, b in zip(discounts, rewards)])

        policy_loss = []
        for log_prob in saved_log_probs:
            policy_loss.append(-log_prob * R)
        policy_loss = torch.cat(policy_loss).sum()

        optimizer.zero_grad()
        policy_loss.backward()
        optimizer.step()

        if i_episode % print_every == 0:
            # print('Episode {}\tAverage Score: {:.2f} {}'.format(i_episode, np.mean(scores_deque), actions))
            torch.save(policy, 'models/policyNet.pkl')
            actions = []
            rewards1 = []
            info = ''
            state = env.reset()
            policy.eval()
            for t in range(max_t):
                action, log_prob = policy.best_act(state)
                state, reward, done, info = env.step(action)
                actions.append(action)
                rewards1.append(1)
                if done:
                    break

            scores.append(sum(rewards1))
            scores_means.append(np.mean(scores_deque))
            print('Episode {}\tAverage Score: {:.2f} {} {}'.format(i_episode, np.mean(scores_deque), actions, info))

        if np.mean(scores_deque) >= 195.0:
            print('Environment solved in {:d} episodes!\tAverage Score: {:.2f}'.format(i_episode - 100,
                                                                                       np.mean(scores_deque)))
            break

    return scores,scores_means


if __name__ == '__main__':

    scores, scores_means = reinforce()
    # scores, scores_means = [1,2,3],[2.0,3.9]
    _dict = {'sites_locations':env.sites_locations, 'sites_rates':env.sites_rates,'scores':scores,'scores_means':scores_means}
    import json
    with open('models/scores_results.json','w') as sf:
        json.dump(_dict, sf,indent=4)


    # plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(np.arange(1, len(scores_means) + 1), scores_means)
    plt.ylabel('Score')
    plt.xlabel('Episode #')
    plt.savefig('models/mean_scores.jpg')
    plt.show()
