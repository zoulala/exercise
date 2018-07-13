#coding=utf8


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
deepThought = ChatBot("deepThought")
deepThought.set_trainer(ChatterBotCorpusTrainer)
# 使用中文语料库训练它
deepThought.train("chatterbot.corpus.chinese")  # 语料库

while True:
    # print(deepThought.get_response("很高兴认识你"))
    # print(deepThought.get_response("嗨，最近如何?"))
    # print(deepThought.get_response("复杂优于晦涩"))  # 语出 The Zen of Python
    # print(deepThought.get_response("面对模棱两可，拒绝猜测的诱惑."))
    str = input("you:")
    response = deepThought.get_response(str)
    print("robot:", response)