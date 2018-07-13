"""
测试python操作redis
"""

import redis
from rediscluster import StrictRedisCluster
import json

def redis_t():
    '''redis base test'''
    r = redis.Redis(host='10.12.28.222',port=6380)


    print(r.keys())
    print(r.get('rampage:msgCenter:ipcansession:_sessionId:%df5f71dd209edb7078e9b68ec6c87bb3e'))

def redispool_t():
    '''
    connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销
    默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。
    '''
    pool = redis.ConnectionPool(host='10.12.28.222',port=6380)  # 测试会报错，因为该地址是redis集群的主机。能获取不能写入
    r = redis.Redis(connection_pool=pool)
    r2 = redis.Redis(connection_pool=pool)
    print(r.keys())
    print(len(r.keys()))
    r.set('thoth:thoth-ai:robot:1','aaa')
    lis = r.get('thoth:thoth-ai:robot:1')
    print('lis:',lis)

def redis_cluster():
    '''集群操作'''
    redis_nodes = [{'host':'10.12.28.222','port':6380},
                   {'host':'10.12.28.222','port':6381},
                   {'host':'10.12.28.224','port':6380},
                   {'host':'10.12.28.224','port':6381},
                   {'host':'10.12.28.227','port':6380},
                   {'host':'10.12.28.227','port':6381}
                  ]

    try:
        r = StrictRedisCluster(startup_nodes = redis_nodes)
    except Exception as e:
        print("connect error %s" % e)

    # string 操作
    r.set('thoth:thoth-ai:robot:1','kk')
    # r.delete('thoth:thoth-ai:robot:1')
    print ("name is", r.get('thoth:thoth-ai:robot:1'))

    # list 操作
    r.lpush('thoth:thoth-ai:robot:2',[[1,2,3],[2,3,4]])
    print('list len:',r.llen("thoth:thoth-ai:robot:2"))  # list size
    print("list ", r.lindex('thoth:thoth-ai:robot:2',0))


    # hash 操作
    r.hset('thoth:thoth-ai:robot:3', 'private_vector', [[1,2,3],[2,3,4]])
    r.hset('thoth:thoth-ai:robot:3', 'public_vector', [['4', 3, 2], [0, 1, 1]])

    pv = r.hget('thoth:thoth-ai:robot:3', 'public_vector',)
    print('hash.robot3.public_vector:',pv)
    aaa = pv.decode('utf-8')
    print(type(aaa),aaa)
    b = eval(aaa)  # eval 函数妙用：将string‘[1,2,3]’--->list [1,2,3]
    print(type(b),b)
    # public = str(pv,encoding='utf-8')
    # print('...',type(public))
    # dict_data = json.loads(public)
    # print('ppp',type(dict_data))

def redis_time():
    redis_nodes = [{'host':'10.12.28.222','port':6380},
                   {'host':'10.12.28.222','port':6381},
                   {'host':'10.12.28.224','port':6380},
                   {'host':'10.12.28.224','port':6381},
                   {'host':'10.12.28.227','port':6380},
                   {'host':'10.12.28.227','port':6381}
                  ]

    try:
        r = StrictRedisCluster(startup_nodes = redis_nodes)
    except Exception as e:
        print("connect error %s" % e)

    # print(r.set('thoth-ai','过期测试'))
    #
    # print(r.expire('thoth-ai',10))  # 设定key过期时间 10s

    print(r.get('thoth-ai:robotId:'))


# redis_t()
# redispool_t()
# redis_cluster()
redis_time()






