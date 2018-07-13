#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient

# 连接mongodb
# ------------------------------
conn = MongoClient('localhost', 27017)
db = conn.mydb  #连接mydb数据库，没有则自动创建
my_set = db.test_set  # 使用test_set集合，没有则自动创建


# 插入数据（insert插入一个列表多条数据不用遍历，效率高， save需要遍历列表，一个个插入）
# ------------------------------
my_set.insert({"name":"zhangsan","age":18})
#或
my_set.save({"name":"zhangsan","age":18})

#添加多条数据到集合中
users=[{"name":"zhangsan","age":18},{"name":"lisi","age":20}]
my_set.insert(users)
#或
for w in users:
    my_set.save(w)


# 查询数据库
# ------------------------------
# 查询全部
for i in my_set.find():
    print(i)
#查询name=zhangsan的
for i in my_set.find({"name":"zhangsan"}):
    print(i)
print(my_set.find_one({"name":"zhangsan"}))


# 更新数据
# ------------------------------

my_set.update({"name":"zhangsan"},{'$set':{"age":20}},
              {
                  'upsert': True, #如果不存在update的记录，是否插入
                  'multi': False, #可选，mongodb 默认是false,只更新找到的第一条记录
                  'writeConcern': True #可选，抛出异常的级别。
              }
              )


# 删除数据
# ------------------------------
#删除name=lisi的全部记录
my_set.remove({'name': 'zhangsan'})

#删除name=lisi的某个id的记录
id = my_set.find_one({"name":"zhangsan"})["_id"]
my_set.remove(id)

#删除集合里的所有记录
db.users.remove()

# mongodb的条件操作符
# ------------------------------
#    (>)  大于 - $gt
#    (<)  小于 - $lt
#    (>=)  大于等于 - $gte
#    (<= )  小于等于 - $lte
#例：查询集合中age大于25的所有记录
for i in my_set.find({"age":{"$gt":25}}):
    print(i)


# 排序 \在MongoDB中使用sort()方法对数据进行排序，sort()方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序，-1为降序。
# ------------------------------
for i in my_set.find().sort([("age",1)]):
    print(i)

# limit和skip
# ------------------------------
#limit()方法用来读取指定数量的数据
#skip()方法用来跳过指定数量的数据
#下面表示跳过两条数据后读取6条
for i in my_set.find().skip(2).limit(6):
    print(i)

# in
# ------------------------------
#找出age是20、30、35的数据
for i in my_set.find({"age":{"$in":(20,30,35)}}):
    print(i)

# or
# ------------------------------
#找出age是20或35的记录
for i in my_set.find({"$or":[{"age":20},{"age":35}]}):
    print(i)

#all
# ------------------------------
# 查看是否包含全部条件
dic = {"name":"lisi","age":18,"li":[1,2,3]}
dic2 = {"name":"zhangsan","age":18,"li":[1,2,3,4,5,6]}

my_set.insert(dic)
my_set.insert(dic2)
for i in my_set.find({'li':{'$all':[1,2,3,4]}}):
    print(i)
#输出：{'_id': ObjectId('58c503b94fc9d44624f7b108'), 'name': 'zhangsan', 'age': 18, 'li': [1, 2, 3, 4, 5, 6]}


#push/pushAll
# ------------------------------
my_set.update({'name':"lisi"}, {'$push':{'li':4}})
for i in my_set.find({'name':"lisi"}):
    print(i)
#输出：{'li': [1, 2, 3, 4], '_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'age': 18, 'name': 'lisi'}

my_set.update({'name':"lisi"}, {'$pushAll':{'li':[4,5]}})
for i in my_set.find({'name':"lisi"}):
    print(i)
#输出：{'li': [1, 2, 3, 4, 4, 5], 'name': 'lisi', 'age': 18, '_id': ObjectId('58c50d784fc9d44ad8f2e803')}



# pop/pull/pullAll
# ------------------------------
# pop
# 移除最后一个元素(-1为移除第一个)
my_set.update({'name':"lisi"}, {'$pop':{'li':1}})
for i in my_set.find({'name':"lisi"}):
    print(i)
#输出：{'_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'age': 18, 'name': 'lisi', 'li': [1, 2, 3, 4, 4]}

# pull （按值移除）
# 移除3
my_set.update({'name':"lisi"}, {'$pull':{'li':3}})

#pullAll （移除全部符合条件的）
my_set.update({'name':"lisi"}, {'$pullAll':{'li':[1,2,3]}})
for i in my_set.find({'name':"lisi"}):
    print(i)
#输出：{'name': 'lisi', '_id': ObjectId('58c50d784fc9d44ad8f2e803'), 'li': [4, 4], 'age': 18}


# 多级路径元素操作
# ------------------------------
dic = {"name":"zhangsan",
       "age":18,
       "contact" : {
           "email" : "1234567@qq.com",
           "iphone" : "11223344"}
       }
my_set.insert(dic)

#多级目录用. 连接
for i in my_set.find({"contact.iphone":"11223344"}):
    print(i)
#输出：{'name': 'zhangsan', '_id': ObjectId('58c4f99c4fc9d42e0022c3b6'), 'age': 18, 'contact': {'email': '1234567@qq.com', 'iphone': '11223344'}}

result = my_set.find_one({"contact.iphone":"11223344"})
print(result["contact"]["email"])
#输出：1234567@qq.com

#多级路径下修改操作
result = my_set.update({"contact.iphone":"11223344"},{"$set":{"contact.email":"9999999@qq.com"}})
result1 = my_set.find_one({"contact.iphone":"11223344"})
print(result1["contact"]["email"])
#输出：9999999@qq.com

# 还可以对数组用索引操作
dic = {"name":"lisi",
       "age":18,
       "contact" : [
           {
           "email" : "111111@qq.com",
           "iphone" : "111"},
           {
           "email" : "222222@qq.com",
           "iphone" : "222"}
       ]}
my_set.insert(dic)

#查询
result1 = my_set.find_one({"contact.1.iphone":"222"})
print(result1)
#输出：{'age': 18, '_id': ObjectId('58c4ff574fc9d43844423db2'), 'name': 'lisi', 'contact': [{'iphone': '111', 'email': '111111@qq.com'}, {'iphone': '222', 'email': '222222@qq.com'}]}

#修改
result = my_set.update({"contact.1.iphone":"222"},{"$set":{"contact.1.email":"222222@qq.com"}})
print(result1["contact"][1]["email"])
#输出：222222@qq.com



# 索引
#---------------------------------
my_set.ensureIndex({'age':1})  # 在age字段上构建索引（B-tree），，，
my_set.find({'age':23})  # 通过age字段查找速度将会大大提高
my_set.getIndexes()  # 查看索引
my_set.dropIndex({'age':1})  # 删除索引
# demo
#====================================================================================

#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient

settings = {
    "ip":'192.168.0.113',   #ip
    "port":27017,           #端口
    "db_name" : "mydb",    #数据库名字
    "set_name" : "test_set"   #集合名字
}

class MyMongoDB(object):
    def __init__(self):
        try:
            self.conn = MongoClient(settings["ip"], settings["port"])
        except Exception as e:
            print(e)
        self.db = self.conn[settings["db_name"]]
        self.my_set = self.db[settings["set_name"]]

    def insert(self,dic):
        print("inser...")
        self.my_set.insert(dic)

    def update(self,dic,newdic):
        print("update...")
        self.my_set.update(dic,newdic)

    def delete(self,dic):
        print("delete...")
        self.my_set.remove(dic)

    def dbfind(self,dic):
        print("find...")
        data = self.my_set.find(dic)
        for result in data:
            print(result["name"],result["age"])

def main():
    dic={"name":"zhangsan","age":18}
    mongo = MyMongoDB()
    mongo.insert(dic)
    mongo.dbfind({"name":"zhangsan"})

    mongo.update({"name":"zhangsan"},{"$set":{"age":"25"}})
    mongo.dbfind({"name":"zhangsan"})

    mongo.delete({"name":"zhangsan"})
    mongo.dbfind({"name":"zhangsan"})

if __name__ == "__main__":
    main()

