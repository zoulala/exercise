#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     pymupdf.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-10-25
# brief:    
#
# cmd>e.g:  
# *****************************************************

import fitz

'''
# 将PDF转化为图片
pdfPath pdf文件的路径
imgPath 图像要保存的文件夹
zoom_x x方向的缩放系数
zoom_y y方向的缩放系数
rotation_angle 旋转角度
'''


def pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle):
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    # 逐页读取PDF
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]

        # 设置缩放和旋转系数

        # # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # # 此处若是不做设置，默认图片大小为：792X612, dpi=72
        # zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        # zoom_y = 1.33333333

        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.writePNG(imgPath + str(pg) + ".png")
        print(pg)
    pdf.close()



def pyMuPDF2_fitz(pdfPath, imagePath):
    '''选择自定义区域进行转换'''
    pdfDoc = fitz.open(pdfPath) # open document
    for pg in range(pdfDoc.pageCount): # iterate through the pages
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像
        # 此处若是不做设置，默认图片大小为：792X612, dpi=72
        zoom_x = 1.33333333 #(1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate) # 缩放系数1.3在每个维度  .preRotate(rotate)是执行一个旋转
        rect = page.rect                         # 页面大小
        mp = rect.tl + (rect.bl - (0,75/zoom_x)) # 矩形区域    56=75/1.3333
        clip = fitz.Rect(mp, rect.br)            # 想要截取的区域
        pix = page.getPixmap(matrix=mat, alpha=False, clip=clip) # 将页面转换为图像
        # 开始写图像
        pix.writePNG(imagePath + str(pg) + ".png")
        print(pg)


# pdf_image('test.pdf', 'rst/', 5, 5, 90)


pdf_image('test.pdf', 'rst/', 5, 5, 90)
