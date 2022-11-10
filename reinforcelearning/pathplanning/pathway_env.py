#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     pathway_env.py
# author:   zlw2008ok@126.com
# date:     2022/10/18
# desc:     
#
# cmd>e.g.:  
# *****************************************************

import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


SITES_LOCATIONS = [(1,2), (1,7), (9,3), (6,1), (5,5), (4,8), (3,2), (2,9), (8,10), (7,6)]
SITES_RATES = [7, 5, 7, 10, 3, 4, 4, 5, 10, 8]


class CampSite(object):
    """野外营地站点
    """

    def __init__(self, rate,location, value=85,max_value=100):
        self.value=value  # 物资剩余量
        self.rate=rate  # 物资消耗速率
        self.location=location  # 地图坐标
        self.max_value=max_value  # 物资最大容积

    def reduce_once(self):
        self.value -= self.rate
        if self.value<0:
            self.value = 0

    def add_once(self, volume):
        gap = self.max_value-self.value
        if volume>gap:
            self.value = self.max_value
            leave_volume = volume-gap
        else:
            self.value += volume
            leave_volume = 0
        return leave_volume

    def is_alive(self):
        if self.value>=5:
            return True
        else:
            return False

    def get_state(self):
        return [self.value, ]

class Plane(object):
    """飞机"""
    def __init__(self, oil=100,max_oil=100,volume=300,max_volume=300,oil_rate=1, location=(0,0)):
        self.oil=oil  # 油量
        self.volume=volume  # 当前物资量
        self.location=location  # 地图坐标
        self.max_oil = max_oil  # 最大油量
        self.max_volume = max_volume  # 最大物资容量
        self.oil_rate = oil_rate  # 油耗/单位距离

    def reset(self):
        self.__init__()

    def can_arrived(self, distance,):
        if self.oil/self.oil_rate - distance>0:
            return True
        else:
            return False

    def is_enough(self):
        '''oil>1/2 + volume>1/2'''
        if self.oil> self.max_oil*3/4 and self.volume> self.max_volume*3/4:
            return True
        return False

    def get_state(self):

        return [self.oil,self.volume,self.location[0],self.location[1]]


class PathWayEnv(object,):
    def __init__(self, num_site=10, num_plane=1):
        self.num_site = num_site
        self.action_space = list(range(num_site+num_plane))
        self.locations = [(i,j) for i in range(1,11) for j in range(1,11)]  # 10x10区域可建营地站点
        self.origin_location = (0, 0)   # 后勤补给点（原点）
        self.last_action = -1

        self.sites_locations = random.sample(self.locations, num_site)  # 随机10个点作为营地
        # self.sites_locations = SITES_LOCATIONS
        print(self.sites_locations)

        self.sites_rates = [random.randint(2,10) for i in range(num_site)]  # 随机10个营地的物资消耗速率
        # self.sites_rates = SITES_RATES
        print(self.sites_rates)

        self.sites=[]
        self._build_sites()

        self.plane = Plane()

        self.env_state = self._get_env_state()

    def set_sites(self, sites_locations, sites_rates):
        self.sites_locations = sites_locations
        self.sites_rates = sites_rates

    def _build_sites(self):
        '''构建营地'''
        for location,rate in zip(self.sites_locations,self.sites_rates):
            site = CampSite(rate, location)
            self.sites.append(site)

    def _get_env_state(self):
        arrays = self.plane.get_state()
        for site in self.sites:
            arrays += site.get_state()
        return np.array(arrays, dtype=np.float32)

    def _calculate_distance(self, location1, location2):
        distance = abs(location1[0]-location2[0])+abs(location1[1]-location2[1])
        return distance

    def reset(self):
        '''环境重制，初始化'''
        self.sites=[]
        self._build_sites()
        self.plane.reset()
        self.env_state = self._get_env_state()
        return self.env_state

    def step(self, action):
        info = ""
        done = False
        reward = 1
        # get correct location
        plane_location = self.plane.location

        for site in self.sites:  # 每次action间隙 营地消耗变化
            site.reduce_once()

        # action

        if action==self.last_action:  # 飞机不应该两次去同一个地方
            done = True
            reward = 0
            info = "same action"
        self.last_action= action

        if action ==0:
            next_location = self.origin_location
            distance = self._calculate_distance(plane_location, next_location)

            if self.plane.is_enough():  # 飞机油量和物资充足不应该回原点(节约路线)
                done = True
                reward = 0
                info = "plane enough"

            if self.plane.can_arrived(distance):
                self.plane.reset()  # update plane

            else:  # 飞机油耗殆尽结束
                done = True
                reward = 0
                info = "oil done"

        else:
            next_site = self.sites[action-1]
            next_location = next_site.location
            distance = self._calculate_distance(plane_location, next_location)
            if self.plane.can_arrived(distance):
                leave_volume = next_site.add_once(self.plane.volume)
                self.plane.volume = leave_volume  # update plane
                self.plane.location = next_location
                self.plane.oil -= distance*self.plane.oil_rate

            else:  # 飞机油耗殆尽结束
                done = True
                reward = 0
                info = "oil done"

        # next state
        next_env_state = self._get_env_state()

        # reward function
        alive_count = 0
        sum_value = 0
        site_no = 1
        for site in self.sites:
            if site.is_alive():
                alive_count += 1
            sum_value += site.value

            if site.value==0:  # 站点物资耗尽
                done=True
                reward = 0
                info = "value%s done" % site_no
            site_no += 1

        if sum_value==0:  # 所有站点物资耗尽
            done=True
            reward = 0
            info = "value all done"

        # reward = alive_count + 0.2*(sum_value/self.num_site)

        return next_env_state, reward, done, info

    def render(self):

        x, y = zip(*self.sites_locations)
        n = len(self.sites_locations)
        text = [str(i) for i in range(1,n+1)]

        t = np.array(range(n))  # 取10个点作为颜色与数值的映射
        # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        # a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])  # 查看字体
        # for i in a:
        #     print(i)
        # plt.rcParams['font.family'] = ['Heiti TC']  # 用来正常显示中文标签

        # plt.scatter(x, y, s=50, c=t, marker='x', cmap=plt.cm.Spectral, alpha=0.8)

        lo=plt.scatter(0, 0, s=80,  c='red', marker='^', cmap=plt.cm.Spectral, alpha=1.0, label="原点位置")
        ll=plt.scatter(x, y, s=60,  c='blue', marker='o', cmap=plt.cm.Spectral, alpha=0.5, label="医疗站点")
        lp = plt.scatter(self.plane.location[0], self.plane.location[1]+0.2, s=80, c='g', marker='*', cmap=plt.cm.Spectral, alpha=1.0, label="飞机位置")
        plt.legend((ll, lo, lp), ('sites', 'home', 'plane'), scatterpoints=1, loc='upper left', ncol=3, fontsize=8)

        plt.xlim((-1.5, 11))
        plt.ylim((-1.5, 11))

        plt.annotate('✈️', (self.plane.location[0], self.plane.location[1]+0.4),fontsize=20)  # 原点
        for i in range(len(x)):
            plt.annotate(text[i], (x[i], y[i] + 0.2),fontsize=10)

        # plt.xticks(())
        # plt.yticks(())

        plt.savefig('models/map.jpg')
        plt.show()

