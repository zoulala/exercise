#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     pdf2imge.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-10-25
# brief:    poppler install refer:https://blog.csdn.net/qq_36489878/article/details/103880834
#
# cmd>e.g:  
# *****************************************************

import os
from pdf2image import convert_from_path, convert_from_bytes
import tempfile
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


def pdf2image2(pdfPath, imagePath, pageNum):
    # 方法一：
    # convert_from_path('a.pdf', dpi=500, "output",fmt="JPEG",output_file="ok",thread_count=4)
    # 这会将a.pdf转换成在output文件夹下形如ok_线程id-页码.jpg的一些文件。
    # 若不指定thread_count则默认为1，并且在文件名中显示id. 这种转换是直接写入到磁盘上的，因此不会占用太多内存。

    # 下面的写法直接写入到内存,默认是C:\Users\pppp\AppData\Local\Temp\生成的uuid4名字
    images = convert_from_path(pdfPath, dpi=72)
    for image in images:
        if not os.path.exists(imagePath):
            os.makedirs(imagePath)
        image.save(imagePath + '/' + 'psReport_%s.png' % images.index(image), 'PNG')

    # 方法二：
    images = convert_from_bytes(open('/home/belval/example.pdf', 'rb').read())
    for image in images:
        if not os.path.exists(imagePath):
            os.makedirs(imagePath)
        image.save(imagePath + '/' + 'psReport_%s.png' % images.index(image), 'PNG')

        # 方法三，也是最推荐的方法
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path(pdfPath, output_folder=path, dpi=72)
        for image in images_from_path:
            if not os.path.exists(imagePath):
                os.makedirs(imagePath)
            image.save(imagePath + '/' + 'psReport_%s.png' % images_from_path.index(image), 'PNG')
        print(images_from_path)


pdf2image2('test.pdf','rst2',5)

