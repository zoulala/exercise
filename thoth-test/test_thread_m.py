# ------------------------------线程操作内存测试----------------------------------
# ref:http://chuansong.me/n/572991951926

from threading import Thread,Timer
from time import ctime,sleep,time
import numpy as np

class Robot():
    def __init__(self,id):
        self.robotId = id
        # 私有库模型
        self.private_lib_vec_dict = {1:[], 2:[[5,5,5],[6,6,6],[7,7,7],[8,8,8]]}
        self.private_lib_id_dict = {1:[], 2:['e','f','g','h']}
        self.wait_flag = False

        for i in range(200000):
            self.private_lib_vec_dict[1].append(list(range(400)))
            self.private_lib_id_dict[1].append(i)


    def model_del(self, private_questionId_list ):
        self.wait_flag = True
        for questionId in private_questionId_list:
            for libId in self.private_lib_id_dict:
                if questionId in self.private_lib_id_dict[libId]:
                    print("删除问题Id:%s" % questionId)
                    index = self.private_lib_id_dict[libId].index(questionId)
                    del self.private_lib_id_dict[libId][index]
                    del self.private_lib_vec_dict[libId][index]
                    # print("删除问题成功！")
        self.wait_flag = False

def fn1(robot):
    while True:   # 线程会一直执行
        # while robot.wait_flag:  # while self.wait_flag:等待删除操作
        #     sleep(0.3)
        k = np.dot(robot.private_lib_vec_dict[1], list(range(400)))
        print('计算...ok:',len(k))
        # sleep(0)


def fn2(robot):
    for i in range(2,100,3):  # 线程执行完自动结束
        a_t = time()
        robot.model_del( [i,i+1,i+2,i+3,i+10,i+12,i+23])
        b_t = time()
        print('删除后：',len(robot.private_lib_vec_dict[1]), len(robot.private_lib_id_dict[1]),'------',str(float(b_t-a_t)))
        # sleep(0.2)

if __name__ == '__main__':

    ro = Robot(1008)
    t1 = Thread(target=fn1, args=(ro,))
    t1.start()
    t2 = Thread(target=fn2, args=(ro,))
    t2.start()




