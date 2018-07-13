#!/usr/bin/env python
#conding=utf8


import pymysql
import pymongo
from lib import pinyin

mysql_set = {"user": "app_cloudcs_im",
           "host": "10.127.138.2",
           "database": "cloudcs_dev",
           "port": 3306,
           "passwd": "app_cloudcs_1"
           }
mongo_set = {'host':'localhost',
             'port':27017
             }

class Mysql():
    def __init__(self):
        db = pymysql.connect(mysql_set["host"],mysql_set["user"],mysql_set["passwd"],mysql_set["database"],charset='utf8')
        self.cursor = db.cursor()


    def get_mysql_keyslist(self):
        sql = "select prekey from jl_keymap where group_pos=0"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        keyslist = []
        for keys in result:
            word = keys[0]
            if word not in keyslist:
                keyslist.append(word)
        return keyslist

    def get_mysql_questions(self):
        sql = "select title,answer from jl_questions"
        self.cursor.execute(sql)
        questions = self.cursor.fetchall()
        return questions


class Mongo():
    def __init__(self):
        conn = pymongo.MongoClient(mongo_set['host'], mongo_set['port'])
        self.db = conn.umi  # 连接umi库，没有则创建

    def keys_to_mongodb(self,keywords_list):

        keys = self.db.keywords  # 使用集合，没有则创建

        keys_pinyin_list = pinyin.get_listpin_plus(keywords_list)  # 关键词拼音列表
        # keys_syn_list =   # 关键词同义词列表
        # keys_index_list =  # 关键词titles索引列表

        for i in range(len(keywords_list)):
            dic = {'id':i,'key':keywords_list[i], 'pinyin':keys_pinyin_list[i]}
            keys.insert(dic)
        print('keys writing in mongodb is ok !')

    def questions_to_mongodb(self,questions_tuple):
        que = self.db.questions
        leng = len(questions_tuple)
        for i in range(leng):
            dic = {'id':i, 'title':questions_tuple[i][0],'answer':questions_tuple[i][1]}
            que.insert(dic)
        print("questions writing in mongodb is ok !")


if __name__ == "__main__":
    mysql = Mysql()

    keys_list = mysql.get_mysql_keyslist()
    print (len(keys_list))
    questions = mysql.get_mysql_questions()

    keys_list = [key for key in keys_list if len(key)>1]  # 关键词去噪


    mongo = Mongo()

    mongo.db.keywords.remove()  # 删除集合
    mongo.db.questions.remove()

    mongo.keys_to_mongodb(keys_list)
    mongo.questions_to_mongodb(questions)

    w = mongo.db.questions.find({},{'title':1,'id':1,'_id':0})
    for x in w:
        print(x)




