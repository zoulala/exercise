
from rediscluster import StrictRedisCluster

class RedisPubSub():
    def __init__(self):
        redis_nodes = [{'host': '10.12.28.222', 'port': 6380},
                       {'host': '10.12.28.222', 'port': 6381},
                       {'host': '10.12.28.224', 'port': 6380},
                       {'host': '10.12.28.224', 'port': 6381},
                       {'host': '10.12.28.227', 'port': 6380},
                       {'host': '10.12.28.227', 'port': 6381}
                       ]

        try:
            self.__r = StrictRedisCluster(startup_nodes=redis_nodes)
            self.chan_sub = 'fm99'
            self.chan_pub = 'fm99'
        except Exception as e:
            print("connect error %s" % e)

    def pub_fun(self, msg):
        self.__r.publish(self.chan_pub, msg)
        return True


    def sub_fun(self):
        pub = self.__r.pubsub()
        pub.subscribe(self.chan_sub)
        # pub.psubscribe('*')  # 订阅所有频道
        pub.parse_response()
        return pub




