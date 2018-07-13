#coding=utf8
""" 参考 ：http://blog.just4fun.site/create-wechat-bot.html
            https://github.com/liuwons/wxBot
注意：
    wxbot 在py2下运行
    chatterbot 在py3下运行
    作者通过 py3下运行chatterbot的web 的api, py2下运行wxbot 调用 该api 得到的回复 进行微信互动。
"""

from wxbot import WXBot
#import requests
#bot_api="http://127.0.0.1:8000/get_response"

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer



deepThought = ChatBot("deepThought")
deepThought.set_trainer(ChatterBotCorpusTrainer)
# 使用中文语料库训练它
deepThought.train("chatterbot.corpus.chinese")  # 语料库



class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            user_input = msg["content"]["data"]
            #payload={"user_input":user_input}
            #response = requests.get(bot_api,params=payload).json()["response"]
            #print(type(response)) # unicode
            response = deepThought.get_response(user_input).text
            self.send_msg_by_uid(response, msg['user']['id'])

def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    main()