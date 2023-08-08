#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     pyweb_zlw_01.py
# author:   zlw2008ok@126.com
# date:     2022/8/13
# desc:     实现文本输入，输出分词序列及词性按一定方式显示，并且不同词性对应的词高亮显示颜色不同
#
# cmd>e.g.:  
# *****************************************************

from pywebio import start_server
from pywebio.pin import *
from pywebio.output import *


def run_parser():
    with use_scope('output',clear=True):
        docContent = pin.docContent
        contents = []
        for i in range(100):
            # put_text("咳嗽", inline=True).style('color:red')
            # put_text("三天", inline=True).style('color:blue')
            contents.append(put_text("咳嗽",inline=True).style('color:red'))
            contents.append(put_text("三天", inline=True).style('color:blue'))
        # contents
        # put_info(*contents, )
        put_scope('aaa', content=contents)

def clear_input():
    pin.docContent=''

def main():
    put_scope('projectName', content=put_markdown('**医学文本分词与标注**').style('font-size: x-large;'))

    put_row([
        put_textarea('docContent', value='', rows=7),
        put_column([
            put_select('docType', options=['入院记录', '出院记录', '日常病程']),
            put_button(" 运  行 ", onclick=lambda: run_parser()),  # single button
            put_button(" 清  除 ", onclick=lambda: clear_input(), color="secondary"),  # single button
        ]),
    ], size='80% 20%')
    put_scrollable(put_scope('output', content=put_text('(结果显示在这里)').style('font-style:italic;color:BLUE')),
                   height=300).style('background:#E8E8E8'),


if __name__ == '__main__':
    start_server(main, port=8000, debug=True)  #使用 debug=True 来开启debug模式，这时server会在检测到代码发生更改后进行重启。


