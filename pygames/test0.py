#!/usr/bin/env python
# -*- coding:utf-8 -*-
#ref:https://blog.csdn.net/fengf2017/article/details/79300801
import pygame
from pygame.locals import *
from sys import exit

background_image = 'image/sushiplate.jpg'
mouse_image = 'image/fugu.png'

# 初始化pygame，为使用硬件做准备
pygame.init()
# 创建了一个窗口
screen = pygame.display.set_mode((640, 480), 0, 32)
# 设置窗口标题
pygame.display.set_caption("hello world")

# 加载并转换图像
background = pygame.image.load(background_image).convert()
mouse_cursor = pygame.image.load(mouse_image).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:  # 接收到退出事件后退出程序
            exit()
    screen.blit(background, (0, 0))  # 画上背景图

    x, y = pygame.mouse.get_pos()  # 获得鼠标位置
    # 计算光标左上角位置
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2
    # 画上光标
    screen.blit(mouse_cursor, (x, y))

    # 刷新画面
    pygame.display.update()