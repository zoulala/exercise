#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     pyweb02.py
# author:   zlw2008ok@126.com
# date:     2022/8/3
# desc:     提供web服务
#
# cmd>e.g.:  
# *****************************************************

from pywebio import start_server
from pywebio.input import input, FLOAT
from pywebio.output import put_text

'''
在PyWebIO中，有两种方式用来运行PyWebIO应用：作为脚本运行和使用 pywebio.start_server() 或 pywebio.platform.path_deploy() 来作为Web服务运行。
def main():  # PyWebIO application function
    name = input.input("what's your name")
    output.put_text("hello", name)

start_server(main, port=8080, debug=True)
使用 debug=True 来开启debug模式，这时server会在检测到代码发生更改后进行重启。

start_server() 提供了对远程访问的支持，当开启远程访问后（通过在 start_server() 中传入 remote_access=True 开启 ），你将会得到一个用于访问当前应用的临时的公网访问地址，其他任何人都可以使用此地址访问你的应用。远程接入可以很方便地将应用临时分享给其他人。

将PyWebIO应用部署为web服务的另一种方式是使用 path_deploy() 。path_deploy() 可以从一个目录中部署PyWebIO应用，只需要在该目录下的python文件中定义PyWebIO应用，就可以通过URL中的路径来访问这些应用了。
'''

### 并发
'''Server模式下多线程的使用示例:

def show_time():
    while True:
        with use_scope(name='time', clear=True):
            put_text(datetime.datetime.now())
            time.sleep(1)

def app():
    t = threading.Thread(target=show_time)
    register_thread(t)   ### Server模式下，如果需要在新创建的线程中使用PyWebIO的交互函数，需要手动调用 register_thread(thread) 对新进程进行注册（这样PyWebIO才能知道新创建的线程属于哪个会话）。如果新创建的线程中没有使用到PyWebIO的交互函数，则无需注册。没有使用 register_thread(thread) 注册的线程不受会话管理，其调用PyWebIO的交互函数将会产生 SessionNotFoundException 异常。
    put_markdown('## Clock')
    t.start()  # run `show_time()` in background

    # ❌ this thread will cause `SessionNotFoundException`
    threading.Thread(target=show_time).start()

    put_text('Background task started.')


start_server(app, port=8080, debug=True)
'''

### 会话的结束
'''
当用户关闭浏览器页面时，与之相应的会话也将被关闭。会话关闭后，应用中未返回的PyWebIO输入函数的调用将会抛出 SessionClosedException 异常，后续对PyWebIO交互函数的调用将会引发 SessionNotFoundException 或 SessionClosedException 异常。

大部分情况下，你不需要捕获这些异常，让这些异常来终止代码的执行通常是比较合适的。

可以使用 pywebio.session.defer_call(func) 来设置会话结束时需要调用的函数。无论是因为用户主动关闭页面还是任务结束使得会话关闭，设置的函数都会被执行。defer_call(func) 可以用于资源清理等工作。在会话中可以多次调用 defer_call() ,会话结束后将会顺序执行设置的函数。
'''


# start_server()启动多应用
'''
start_server() 接收一个函数作为PyWebIO应用，另外， start_server() 还支持传入函数列表或字典，从而启动多个PyWebIO应用，应用之间可以通过 go_app() 或 put_link() 进行跳转:

def task_1():
    put_text('task_1')
    put_buttons(['Go task 2'], [lambda: go_app('task_2')])

def task_2():
    put_text('task_2')
    put_buttons(['Go task 1'], [lambda: go_app('task_1')])

def index():
    put_link('Go task 1', app='task_1')  # Use `app` parameter to specify the task name
    put_link('Go task 2', app='task_2')

# equal to `start_server({'index': index, 'task_1': task_1, 'task_2': task_2})`
start_server([index, task_1, task_2])

当 start_server() 的第一个参数的类型为字典时，字典键为应用名，类型为列表时，函数名为应用名。
可以通过 app URL参数选择要访问的应用(例如使用 http://host:port/?app=foo 来访问 foo 应用)， 为提供了 app URL参数时默认使用运行 index 应用，当 index 应用不存在时，PyWebIO会提供一个默认的索引页作为 index 应用

'''


# 与Web框架整合
'''
可以将PyWebIO应用集成到现有的Python Web项目中，PyWebIO应用与Web项目共用一个Web框架。目前支持与Flask、Tornado、Django、aiohttp和FastAPI(Starlette) Web框架的集成。

Flask:
from pywebio.platform.flask import webio_view
from flask import Flask

app = Flask(__name__)

# `task_func` is PyWebIO task function
app.add_url_rule('/tool', 'webio_view', webio_view(task_func),
            methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods

app.run(host='localhost', port=80)

'''

# 生产环境部署
'''
在生产环境中，你可能会使用一些 WSGI/ASGI 服务器（如 uWSGI、Gunicorn、Uvicorn）部署 Web 应用程序。由于 PyWebIO 应用程序会在进程中存储会话状态，当使用基于 HTTP 的会话（使用Flask 和 Django后端时）并生成多个进程来处理请求时，请求可能会被分发到错误的进程中。因此，在使用基于 HTTP 的会话时，只能启动一个进程来处理请求。

如果仍然希望使用多进程来提高并发，一种方式是使用 Uvicorn+FastAPI，或者你也可以启动多个Tornado/aiohttp进程，并在它们之前添加外部的负载均衡软件（如 HAProxy 或 nginx）。这些后端使用 WebSocket 协议与浏览器进行通信，所以不存在上述问题。
'''

# PyWebIO静态资源的托管
'''
PyWebIO默认使用CDN来获取前端的静态资源，如果要将PyWebIO应用部署到离线环境中，需要自行托管静态文件， 并将 webio_view() 或 webio_handler() 的 cdn 参数设置为 False 。

cdn=False 时需要将静态资源托管在和PyWebIO应用同级的目录下。 同时，也可以通过 cdn 参数直接设置PyWebIO静态资源的URL目录。

PyWebIO的静态文件的路径保存在 pywebio.STATIC_PATH 中，可使用命令 python3 -c "import pywebio; print(pywebio.STATIC_PATH)" 将其打印出来。
'''


# 基于协程的会话
'''
在大部分情况下，你并不需要使用基于协程的会话。PyWebIO中所有仅用于协程会话的函数或方法都在文档中均有特别说明。

PyWebIO的会话实现默认是基于线程的，用户每打开一个和服务端的会话连接，PyWebIO会启动一个线程来运行任务函数。 除了基于线程的会话，PyWebIO还提供了基于协程的会话。基于协程的会话接受协程函数作为任务函数。

基于协程的会话为单线程模型，所有会话都运行在一个线程内。对于IO密集型的任务，协程比线程占用更少的资源同时又拥有媲美于线程的性能。 另外，协程的上下文切换具有可预测性，能够减少程序同步与加锁的需要，可以有效避免大多数临界区问题。


要使用基于协程的会话，需要使用 async 关键字将任务函数声明为协程函数，并使用 await 语法调用PyWebIO输入函数:

 from pywebio.input import *
 from pywebio.output import *
 from pywebio import start_server

 async def say_hello():
     name = await input("what's your name?")
     put_text('Hello, %s' % name)

 start_server(say_hello, auto_open_webbrowser=True)
 
 
 在协程任务函数中，也可以使用 await 调用其他协程或标准库 asyncio 中的可等待对象( awaitable objects ):

 import asyncio
 from pywebio import start_server

 async def hello_word():
     put_text('Hello ...')
     await asyncio.sleep(1)  # await awaitable objects in asyncio
     put_text('... World!')

 async def main():
     await hello_word()  # await coroutine
     put_text('Bye, bye')

 start_server(main, auto_open_webbrowser=True)
 
 注意

在基于协程的会话中， pywebio.input 模块中的定义输入函数都需要使用 await 语法来获取返回值，忘记使用 await 将会是在使用基于协程的会话时常出现的错误。

其他在协程会话中也需要使用 await 语法来进行调用函数有:

pywebio.session.run_asyncio_coroutine(coro_obj)
pywebio.session.eval_js(expression)
'''


# 协程会话与Web框架集成
'''

基于协程的会话同样可以与Web框架进行集成，只需要在原来传入任务函数的地方改为传入协程函数即可。

但当前在使用基于协程的会话集成进Flask或Django时，存在一些限制：

一是协程函数内还无法直接通过 await 直接等待asyncio库中的协程对象，目前需要使用 run_asyncio_coroutine() 进行包装。

二是，在启动Flask/Django这类基于线程的服务器之前需要启动一个单独的线程来运行事件循环。

使用基于协程的会话集成进Flask的示例:

 import asyncio
 import threading
 from flask import Flask, send_from_directory
 from pywebio import STATIC_PATH
 from pywebio.output import *
 from pywebio.platform.flask import webio_view
 from pywebio.platform import run_event_loop
 from pywebio.session import run_asyncio_coroutine

 async def hello_word():
     put_text('Hello ...')
     await run_asyncio_coroutine(asyncio.sleep(1))  # can't just "await asyncio.sleep(1)"
     put_text('... World!')

 app = Flask(__name__)
 app.add_url_rule('/hello', 'webio_view', webio_view(hello_word),
                             methods=['GET', 'POST', 'OPTIONS'])

 # thread to run event loop
 threading.Thread(target=run_event_loop, daemon=True).start()
 app.run(host='localhost', port=80)
最后，使用PyWebIO编写的协程函数不支持Script模式，总是需要使用 start_server 来启动一个服务或者集成进Web框架来调用。
'''

def bmi():
    height = input("请输入你的身高(cm)：", type=FLOAT)
    weight = input("请输入你的体重(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(14.9, '极瘦'), (18.4, '偏瘦'),
                  (22.9, '正常'), (27.5, '过重'),
                  (40.0, '肥胖'), (float('inf'), '非常肥胖')]

    for top, status in top_status:
        if BMI <= top:
            put_text('你的 BMI 值: %.1f，身体状态：%s' % (BMI, status))
            break

if __name__ == '__main__':
    start_server(bmi, port=8000, debug=True)  #使用 debug=True 来开启debug模式，这时server会在检测到代码发生更改后进行重启。
