#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     extra_line.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-03-17
# brief:    
#
# cmd>e.g:  
# *****************************************************

import cv2 as cv
import numpy as np

mul_image_file = 'a.jpeg'
img = cv.imread(mul_image_file)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 灰度图片
ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 全局自适应阈值
dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 101, 20)

kernel1 = cv.getStructuringElement(cv.MORPH_RECT, (1, 30))
dilated1 = cv.dilate(dst, kernel1)
eroded1 = cv.erode(dilated1, kernel1)
thresh = cv.adaptiveThreshold(eroded1, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 5)
lines = cv.HoughLinesP(thresh, 1, np.pi / 180, 10, minLineLength=200, maxLineGap=5)

kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (30, 1))
dilated2 = cv.dilate(dst, kernel2)
eroded2 = cv.erode(dilated2, kernel2)
thresh1 = cv.adaptiveThreshold(eroded2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 5)
lines2 = cv.HoughLinesP(thresh1, 1, np.pi / 180, 10, minLineLength=200, maxLineGap=5)

print len(lines)
print len(lines2)

