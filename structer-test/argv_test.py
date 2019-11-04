#!/usr/bin/python
# -*- coding: utf8 -*-
#
# *****************************************************
#
# file:     argv_test.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2019-10-27
# brief:    
#
# cmd>e.g:  
# *****************************************************

import sys
import argparse



# ------------1-----------
argvs = sys.argv
print(argvs[0])  # 脚本名
'''
argv_test.py
'''

# -------------2 ----------  # python argv_test.py --log_path='abc/def/' --flag 3 --port=8080 -l
parser = argparse.ArgumentParser(usage="it's usage test.", description="help info.")
parser.add_argument("--log_path", default='./', help="the logs path.")
parser.add_argument("--flag", type=int, choices=[0, 1, 2, 3], default=0, help="test choices")
parser.add_argument("-p","--port", type=int, required=True, help="the port number.")
parser.add_argument("-l", "--log", default=False, action="store_true", help="active log info.")
parser.add_argument("-r", "--rog", default=False, action="store_true", help="active log info.")

args = parser.parse_args()

print(args.log_path)
print(args.flag)
print(args.port)
print(args.log)
print(args.rog)


'''
abc/def/
3
8080
True
False
'''