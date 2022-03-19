#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     ts_padding.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-04-21
# brief:    处理padding对rnn的影响，https://www.jianshu.com/p/376c16b71130
#
# cmd>e.g:  
# *****************************************************


import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset,DataLoader
from torch.nn.utils.rnn import pad_sequence,pack_padded_sequence,pad_packed_sequence


def collate_fn(train_data):
    # train_data.sort(key=lambda data: len(data), reverse=True)
    data_length = [len(data) for data in train_data]
    train_data = pad_sequence(train_data, batch_first=True, padding_value=0)
    return train_data, data_length


class MyData(Dataset):
    def __init__(self, train_x):
        self.train_x = train_x
        # self.train_x = pad_sequence(train_x, batch_first=True, padding_value=0)

    def __len__(self):
        return len(self.train_x)

    def __getitem__(self, item):
        return self.train_x[item]


emb = nn.Embedding(10,8,padding_idx=0)
net = nn.LSTM(8, 5, batch_first=True)

train_x = [torch.tensor([1, 2]),
           torch.tensor([1,2, 3, 4]),
           torch.tensor([3, 4, 5, 6, 7]),
           torch.tensor([4, 5, 6, 7]),
           torch.tensor([5, 6, 7]),
           torch.tensor([6, 7]),
           torch.tensor([7])]

train_data = MyData(train_x)
# train_dataloader = DataLoader(train_data, batch_size=2)
train_dataloader = DataLoader(train_data, batch_size=2,  collate_fn=lambda x:x)
for batch_data in train_dataloader:
    lens = list(map(len, batch_data))

    batch_data = pad_sequence(batch_data,batch_first=True, padding_value=0)
    batch_data = emb(batch_data)
    # print(batch_data)
    batch_data = pack_padded_sequence(batch_data, lens, batch_first=True, enforce_sorted=False)  # 压缩去除padding，减少rnn计算和(h,c)更准确
    # print(batch_data)
    output, hidden = net(batch_data)
    print(output)
    unpacked = pad_packed_sequence(output,batch_first=True)  # 解压缩，此时output是packedsequence类型，
    print(unpacked)


    break


