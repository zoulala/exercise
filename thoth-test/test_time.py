"""
测试定时任务
"""

from threading import Timer
import time

# sleep 循环，阻塞式
# k = 5
# while k:
#     print('sleep.阻塞')
#     time.sleep(2)
#     k -= 1

# 循环调用线程, 非阻塞
# k = 0
aaa = [1,2]
def printHello(a):
    # print('hello world')
    print(a)
    global k
    # k += 1
    # global t
    t = Timer(2, printHello,(a,))
    t.start()
    # if k >5:
    #     t.cancel()

    # time.sleep(6)
    # t.cancel()


printHello(aaa)

time.sleep(5)
aaa.append(5)
print('--------------')



