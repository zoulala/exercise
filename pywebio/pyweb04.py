#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     pyweb04.py.py
# author:   zlw2008ok@126.com
# date:     2022/8/6
# desc:     output
#
# cmd>e.g.:  
# *****************************************************

from pywebio.output import *


### ------------- 基本输出---------------
# 文本
put_text("hello world.","hello too")
put_text("a","a",sep='|',inline=True).style('color:red')
put_text("b","b",inline=True)
contents = []
for i in range(100):
    # a = put_text("咳嗽",inline=True).style('color:red')
    # contents.append(a)
    contents.append(put_text("咳嗽", inline=True).style('color:red'))
    contents.append(put_text("三天", inline=True).style('color:blue'))
put_info(*contents)
put_scope('aaa',content=contents)

# 表格
put_table([
    ['product','price'],
    ['apple','$5.5'],
    ['banner','$3'],
])

# span
put_table([
    ['C'],
    [span('E', col=2)],  # 'E' across 2 columns
], header=[span('A', row=2), 'B'])  # 'A' across 2 rows

put_grid([
    [put_text('A'), put_text('B')],
    [span(put_text('A'), col=2)],  # 'A' across 2 columns
])

# 图像
put_image(open('xx.png','rb').read())
put_image('http://example.com/some-image.png')  # internet image

# markdown
put_markdown('**Bold Text**')
put_markdown('~~Strikethrough~~')

# Show a notification message
toast('New message 🔔')
toast('Awesome PywebIO!')

# File Output,
put_file('xx.txt',b'hello world!')  # hello world! 输出到文件中

# html
put_html("E=mc<sup>2</sup>")

# Show a PopUp， 弹窗
with popup('poput title'):
    put_text('hello world!')
    put_table([
        ['product', 'price'],
        ['apple', '$5.5'],
        ['banner', '$3'],
    ])

# 按钮 及 促发
def on_click(btn):
    put_markdown("you click %s button"% btn)
put_buttons(['A','B','C'], onclick=on_click)  # onclick： Callback which will be called when button is clicked

# 单个按钮
put_button("Click me", onclick=lambda: toast("Clicked"))  # single button

# 都可以触发:不仅是按钮，所有的输出都可以绑定点击事件。你可以在输出函数之后调用 onclick() 方法来绑定点击事件:
put_image(open('xx.png','rb').read()).onclick(lambda: toast('You click an image'))

# 输出内容在水平方向上排列
put_row([put_code('A'), None, put_code('B')])

# 显示进度条
import time
put_processbar('bar1')
for i in range(1,11):
    set_processbar('bar1', i/10)
    time.sleep(1)



###  ------------- 组合输出 -------------
put_table([
    ['Type', 'Content'],
    ['html', put_html('X<sup>2</sup>')],
    ['text', '<hr/>'],  # equal to ['text', put_text('<hr/>')]
    ['buttons', put_buttons(['A', 'B'], onclick=...)],
    ['markdown', put_markdown('`Awesome PyWebIO!`')],
    ['file', put_file('hello.text', b'hello world')],
    ['table', put_table([['A', 'B'], ['C', 'D']])]
])

popup('Popup title', [
    put_html('<h3>Popup Content</h3>'),
    'plain html: <br/>',  # Equivalent to: put_text('plain html: <br/>')
    put_table([['A', 'B'], ['C', 'D']]),
    put_button('close_popup', onclick=close_popup)
])

# 输出自定义控件
tpl = '''
<details {{#open}}open{{/open}}>
    <summary>{{title}}</summary>
    {{#contents}}
        {{& pywebio_output_parse}}
    {{/contents}}
</details>
'''
put_widget(tpl, {    # tpl为template模版
    "open": True,
    "title": 'More content',
    "contents": [
        'text',
        put_markdown('~~Strikethrough~~'),
        put_table([
            ['Commodity', 'Price'],
            ['Apple', '5.5'],
            ['Banana', '7'],
        ])
    ]
})

# 上下文管理器：一些接受 put_xxx() 调用作为参数的输出函数支持作为上下文管理器来使用：
with put_collapse('This is title'):
    for i in range(4):
        put_text(i)

    put_table([
        ['Commodity', 'Price'],
        ['Apple', '5.5'],
        ['Banana', '7'],
    ])

# 带滚动条的文本区域
put_scrollable()

###  ------------- 事件回调 -------------
# 支持事件回调：PyWebIO允许你输出一些控件并绑定回调函数，当控件被点击时相应的回调函数便会被执行。
from functools import partial

def edit_row(choice, row):
    put_text("You click %s button ar row %s" % (choice, row))

put_table([
    ['Idx', 'Actions'],
    [1, put_buttons(['edit', 'delete'], onclick=partial(edit_row, row=1))],
    [2, put_buttons(['edit', 'delete'], onclick=partial(edit_row, row=2))],
    [3, put_buttons(['edit', 'delete'], onclick=partial(edit_row, row=3))],
])

###  ------------- 输出域Scope -------------
# 输出域Scope:使用scope模型来控制内容输出的位置。scope为输出内容的容器，你可以创建一个scope并将内容输出到其中。
# 每个输出函数（函数名形如 put_xxx() ）都会将内容输出到一个Scope，默认为”当前Scope”，”当前Scope”由 use_scope() 设置。
with use_scope('scope1'):  # 创建并进入scope 'scope1'
    put_text('text1 in scope1')  # 输出内容到 scope1

put_text('text in parent scope of scope1')  # 输出内容到 ROOT scope

with use_scope('scope1'):  # 进入之前创建的scope 'scope1'
    put_text('text2 in scope1')  # 输出内容到 scope1

# 清除scope
with use_scope('scope2'):
    put_text('create scope2')

put_text('text in parent scope of scope2')

with use_scope('scope2', clear=True):  # enter the existing scope and clear the previous content
    put_text('text in scope2')

# scope可以作为装饰器来用
from datetime import datetime

@use_scope('time', clear=True)  # 第一次调用 show_time 时，将会创建 scope：time 输出域并在其中输出当前时间，之后每次调用 show_time() ，输出域都会被新的内容覆盖。
def show_time():
    put_text(datetime.now())

# Scope支持嵌套。会话开始时，PyWebIO应用只有一个 ROOT scope。你可以在一个scope中创建新的scope。比如，以下代码将会创建3个scope:
with use_scope('A'):
    put_text('Text in scope A')

    with use_scope('B'):
        put_text('Text in scope B')

with use_scope('C'):
    put_text('Text in scope C')

'''
以上代码将会产生如下Scope布局:
┌─ROOT────────────────────┐
│                         │
│ ┌─A───────────────────┐ │
│ │ Text in scope A     │ │
│ │ ┌─B───────────────┐ │ │
│ │ │ Text in scope B │ │ │
│ │ └─────────────────┘ │ │
│ └─────────────────────┘ │
│                         │
│ ┌─C───────────────────┐ │
│ │ Text in scope C     │ │
│ └─────────────────────┘ │
└─────────────────────────┘
'''

# 将scope作为输出的子元素（比如将scope作为表格的一个cell），使用 put_scope() 来显式创建一个scope
# 所有的输出函数还支持使用 scope 参数来指定输出的目的scope，也可使用 position 参数来指定在目标scope中输出的位置
put_table([
    ['Name', 'Hobbies'],
    ['Tom', put_scope('hobby', content=put_text('Coding'))]  # hobby is initialized to coding
])

with use_scope('hobby', clear=True):
    put_text('Movie')  # hobby is reset to Movie


with use_scope('hobby'):  # append Music, Drama to hobby
    put_text('Music')
    put_text('Drama')

put_markdown('**Coding**', scope='hobby', position=0)  # insert the Coding into the top of the hobby

# scope控制函数：
clear(scope='hobby') # 清除scope的内容
remove(scope='hobby') #  移除scope
scroll_to(scope='hobby') # 将页面滚动到scope处

###  ------------- 布局 -------------
#通常，使用上述输出函数足以完成大部分输出，但是这些输出之间全都是竖直排列的。如果想创建更复杂的布局，需要使用布局函数。
'''
3个布局函数
put_row() : 使用行布局输出内容. 内容在水平方向上排列
put_column() : 使用列布局输出内容. 内容在竖直方向上排列
put_grid() : 使用网格布局输出内容
'''

put_row([
    put_column([
        put_code('A'),
        put_row([
            put_code('B1'), None,  # None represents the space between the output
            put_code('B2'), None,
            put_code('B3'),
        ]),
        put_code('C'),
    ]), None,
    put_code('D'), None,
    put_code('E')
])

#  支持各部分的尺寸设置
put_row([put_image(...), put_image(...)], size='40% 60%')  # 左右两图宽度比2:3



###  ------------- 样式 -------------
# 如果你熟悉 CSS样式 ，你还可以在输出函数后调用 style() 方法给输出设定自定义样式。
#
# 可以给单个的 put_xxx() 输出设定CSS样式，也可以配合组合输出使用:

put_text('hello').style('color: red; font-size: 20px')

# in combined output
put_row([
    put_text('hello').style('color: red'),
    put_markdown('markdown')
]).style('margin-top: 20px')