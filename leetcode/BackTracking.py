#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     BackTracking.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2021-09-22
# brief:    回溯法
#
# cmd>e.g:  
# *****************************************************

'''
回溯法是一种选优搜索法，按选优条件向前搜索，以达到目标。但当探索到某一步时，发现原先选择并不优或达不到目标，
就退回一步重新选择，这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为 “回溯点”。许多复杂的，
规模较大的问题都可以使用回溯法，有“通用解题方法”的美称。回溯法有“通用的解题法”之称，也叫试探法，它是一种系统的搜索问题的解的方法。
简单来说，回溯法采用试错的方法解决问题，一旦发现当前步骤失败，回溯方法就返回上一个步骤，选择另一种方案继续试错。
'''

# 回溯法：排列组合
def permute(array, res):

    if not array:  # 无元素可加，输出结果
        print(res)

    n = len(array)
    for i in range(n):
        # res.append(array[i])
        newres = res + [array[i]]  # 加入元素

        # 子串排列组合
        sub_array = array[:i] + array[i + 1:]  # 子串
        permute(sub_array, newres)

permute([1,2,3,4],[])



# n 皇后
#ref https://blog.csdn.net/qq_43235359/article/details/90605468

def check(board, row, col):
    for i in range(row):
        if abs(board[i] - col) == 0 or abs(board[i] - col) == abs(i - row):
            return False
    return True


def eightqueen(board, row):
    '''board =1*n,每个元素值代表每行中皇后的位置'''
    border = len(board)
    if row >= border:
        for i, col in enumerate(board):
            print('□ ' * col + '■ ' + '□ ' * (len(board) - 1 - col))
        print("")

    for col in range(border):
        if check(board, row, col):  # 判断该位置是否 与 前面皇后位置冲突
            board[row] = col
            eightqueen(board, row + 1)

board = [0 for i in range(8)]
eightqueen(board, 0)

# board = [0 for i in range(4)]
# eightqueen(board, 0)


