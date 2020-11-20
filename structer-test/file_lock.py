#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     file_lock.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-11-20
# brief:    
#
# cmd>e.g:  
# *****************************************************


'''
锁类型（fcntl.flock函数的第二个参数）
LOCK_SH：  表示要创建一个共享锁，在任意时间内，一个文件的共享锁可以被多个进程拥有
LOCK_EX：  表示创建一个排他锁，在任意时间内，一个文件的排他锁只能被一个进程拥有
LOCK_UN：  表示删除该进程创建的锁
LOCK_MAND：它主要是用于共享模式强制锁，它可以与 LOCK_READ 或者 LOCK_WRITE 联合起来使用，从而
           表示是否允许并发的读操作或者并发的写操作（尽管在 flock() 的手册页中没有介绍
           LOCK_MAND，但是阅读内核源代码就会发现，这在内核中已经实现了）
'''

import time
import fcntl
import threading
import random

# 如下例子中，分别加锁和不加锁，结果
#   不加锁时，多个线程间竞争文件写权限，会出现覆盖，导致写内容不可预期（见test.log.withoutlock)
#   加锁时，多个线程间会等待一个线程结束（因为设置的是阻塞锁）后，第二个线程才开始写，不会相互
#       覆盖（见test.log.withlock)
def demo(name="null"):
    fp = open("test.log", "a+")
    cnt = 0
    # 在3s内随机等待一段时间,打乱加锁顺序
    time.sleep(float(random.randint(0, 300)) / 300)
    fcntl.flock(fp, fcntl.LOCK_EX)
    print ("call demo by %s" % name)

    # 在10s内进行写入，为了避免写入的内容过多，写0.5s，停0.5s
    for i in range(10):
        # 写0.5s
        for i in range(100):

            fp.write("write by %s, %d\n" % (name, cnt))
            print(name)
            cnt += 1
            time.sleep(0.005*random.randint(0, 9))

        # 停0.5s
        time.sleep(0.1*random.randint(0, 9))
    fcntl.flock(fp, fcntl.LOCK_UN)
    fp.close()


if __name__ == "__main__":
    # 创建3个进程，并发写入
    for cnt in range(3):
        name = "thread_%d" % cnt
        thd = threading.Thread(target=demo, args=(name,))
        thd.start()
