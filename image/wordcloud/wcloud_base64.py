#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     wcloud_base64.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-10-19
# brief:    
#
# cmd>e.g:  
# *****************************************************

import numpy as np
import base64
from PIL import Image
import matplotlib.pyplot as plt
from io import BytesIO
from wordcloud import WordCloud

def get_wcloud_image_str(words):
    if not words:return ''
    wc = WordCloud( background_color = 'white',    # 设置背景颜色
                    # mask = backgroud_Image,        # 设置背景图片
                    max_words = 100,            # 设置最大现实的字数
                    # stopwords = STOPWORDS,        # 设置停用词
                    font_path ="STHeiti Light.ttc", #'C:/Users/Windows/fonts/msyh.ttf',# 设置字体格式，如不设置显示不了中文
                    max_font_size = 60,            # 设置字体最大值
                    random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
                    # min_font_size=10,
                    scale=2,
                    # width=1000, height=500,
                    )
    # wc.generate(text)
    wc.generate_from_frequencies(words)

    img_arr = wc.to_array()
    img_opt = Image.fromarray(np.uint8(img_arr))
    output_buffer = BytesIO()
    img_opt.save(output_buffer, format='JPEG')
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    base64_str = base64_str.decode()
    base64_str = 'data:image/jpeg;base64,%s' % base64_str
    return base64_str