# -*- coding: utf-8 -*-

from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious" , #机器人名称
                    storage_adapter="chatterbot.storage.MongoDatabaseAdapter",
                    #database_uri='mongodb://admin:admin@127.0.0.1:27017/admin?authMechanism=MONGODB-CR',
                    database='chatterbot-database',  #设置数据库，训练的对话会保存到该文件 #py3 不产生生文件, py2产生
                    #read_only=True
                    )


from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

conversation1 = [
    "Hello",
    "Hi there!",
]
conversation2 = [
    "hello",
    "good"
]
conversation3 = [
    "你好",
    "对，我很好",
    "加油"
]

# chatbot.set_trainer(ListTrainer)
# chatbot.train(conversation1)   #训练对话，并保存到设定的数据库中
# chatbot.train(conversation2)
# chatbot.train(conversation3)
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.chinese")

while True:
    str = input("you:")
    response = chatbot.get_response(str)
    print("robot:",response)
