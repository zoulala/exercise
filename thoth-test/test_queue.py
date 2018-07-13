"""
测试python队列操作，先进先出
"""

import random
import time
from queue import Queue
# from Queue import Queue
from threading import Thread

queue = Queue(10)

class Producer(Thread):
    def run(self):  # Thread.run()函数重载
        while True:
            elem = random.randrange(9)
            queue.put(elem)
            print ("厨师 {} 做了 {} 饭 --- 还剩 {} 饭没卖完".format(self.name, elem, queue.qsize()))
            time.sleep(random.random())

class Consumer(Thread):
    def run(self):
        while True:
            elem = queue.get()
            print ("吃货{} 吃了 {} 饭 --- 还有 {} 饭可以吃".format(self.name, elem, queue.qsize()))
            time.sleep(random.random())



def main():
    for i in range(3):
        p = Producer()
        p.start()
    for i in range(2):
        c = Consumer()
        c.start()

    print('============================')

if __name__ == '__main__':
    main()

