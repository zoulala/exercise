# #!/usr/bin/python
# import sys
#
# for myline in sys.stdin:  # Input takes from standard input
#     myline = myline.strip()  # Remove whitespace either side
#     words = myline.split()   # Break the line into words
#     for myword in words:  # Iterate the words list
#         print ('%s\t%s' % (myword, 1))  # Write the results to standard output


#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
Created on 2018年1月14日
@author: liuyazhuang
'''
import sys
#输入为标准输入stdin
for line in sys.stdin:
    #删除开头和结尾的空格
    line = line.strip()
    #以默认空格分隔行单词到words列表
    words = line.split()
    for word in words:
        #输出所有单词，格式为“单词，1”以便作为Reduce的输入
        print ('%s\t%s' % (word, 1))
