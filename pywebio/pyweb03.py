#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     pyweb03.py
# author:   zlw2008ok@126.com
# date:     2022/8/3
# desc:     
#
# cmd>e.g.:  
# *****************************************************
from pywebio import start_server
from pywebio.input import *


# input("what's, your name?")
# select("select",['A','B'])
# checkbox("checkbox",options=['checked'])
# radio("radio", options=['A','B','C'])
# textarea('text',placeholder='some text')
# file_upload('select a file')
# textarea('code edit', code={'mode':'python','theme':'darcula'}, value='import ...')


from pywebio.output import *

put_text("hello world.")
put_table([
    ['product','price'],
    ['apple','$5.5'],
    ['banner','$3'],
])
put_image(open('xx.png','rb').read())
put_markdown('**Bold Text**')
toast('Awesome PywebIO!')
put_file('xx.txt',b'hello world!')
put_html("E=mc<sup>2</sup>")
with popup('poput title'):
    put_text('hello world!')
    put_table([
        ['product', 'price'],
        ['apple', '$5.5'],
        ['banner', '$3'],
    ])

def on_click(btn):
    put_markdown("you click %s button"% btn)

put_buttons(['A','B','C'], onclick=on_click)

put_row([put_code('A'), None, put_code('B')])

import time
put_processbar('bar1')
for i in range(1,11):
    set_processbar('bar1', i/10)
    time.sleep(1)


if __name__ == '__main__':
    pass
    # start_server('', port=8000)
