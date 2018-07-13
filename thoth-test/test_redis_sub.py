from test_redis_pubsub_class import RedisPubSub
obj1 = RedisPubSub()
redis_sub = obj1.sub_fun()


for item in redis_sub.listen():
    print (item)
    if item['type'] == 'message':
        data =item['data']
        print('............')

        print ('fff',data)
        if item['data']=='over':
            break
print('000000000')
# p.unsubscribe('spub')
# print '取消订阅'
