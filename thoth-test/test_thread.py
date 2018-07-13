"""
测试python多线程操作
"""
from threading import Thread
from time import ctime,sleep
def music(func):
    while True:   # 线程会一直执行
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):  # 线程执行完自动结束
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(5)

if __name__ == '__main__':
    t1 = Thread(target=music, args=(u'子现在执行...',))
    t1.start()
    t2 = Thread(target=move, args=(u'阿凡达',))
    t2.start()

    print('==========主程序结束============')