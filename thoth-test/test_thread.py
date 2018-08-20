"""
测试python多线程操作
"""
from threading import Thread,Timer
from time import ctime,sleep
def music(func):
    while True:   # 线程会一直执行
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):  # 线程执行完自动结束
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(5)


#  参数args测试
class Threads():
    def __init__(self):
        self.key = 1
        pass

    def redis_monitor_thread(self, dict):
        '''redis 过期监控,robot过期则清除，释放内存'''
        robotId_list = list(dict.keys())
        print(self.key)
        print(robotId_list)

        t = Timer(3, self.redis_monitor_thread, args=(dict,))
        t.start()
        # ref:https://blog.csdn.net/a6225301/article/details/48848009


if __name__ == '__main__':

    # --------------------------参数args测试----------------------------
    dict={1:[1,2,],2:'abc',3:'aa'}
    ts = Threads()
    ts.redis_monitor_thread(dict)
    while 1:
        pass

    # ---------------------------线程测试------------------------------------
    # t1 = Thread(target=music, args=(u'子现在执行...',))
    # t1.start()
    # t2 = Thread(target=move, args=(u'阿凡达',))
    # t2.start()
    # print('==========主程序结束============')



