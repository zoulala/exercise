#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     pyweb03.py
# author:   zlw2008ok@126.com
# date:     2022/8/3
# desc:     input
#
# cmd>e.g.:  
# *****************************************************
from pywebio import start_server
from pywebio.input import *



yourname = input("what's, your name?",)
# 输入类型-type：`TEXT` , `NUMBER` , `FLOAT` , `PASSWORD` , `URL` , `DATE` , `TIME`, `COLOR`, `DATETIME_LOCAL`
password = input("Input password", type=PASSWORD)
print(yourname)

# 输入校验-validate
def check_age(p):  # return None when the check passes, otherwise return the error message
    if p < 10:
        return 'Too young!!'
    if p > 60:
        return 'Too old!!'
age = input("How old are you?", type=NUMBER, validate=check_age)
print(age)

# 支持组输入:输入组中同样支持使用 validate 参数设置校验函数，其接受整个表单数据作为参数:
def check_form(data):  # return (input name, error msg) when validation fail
    if len(data['name']) > 6:
        return ('name', 'Name too long!')
    if data['age'] <= 0:
        return ('age', 'Age can not be negative!')
data = input_group("Basic info",[
  input('Input your name', name='name'),    #PyWebIO 根据是否在输入函数中传入 name 参数来判断输入函数是在 input_group() 中还是被单独调用。所以当单独调用一个输入函数时, 不要 设置 name 参数；而在 input_group() 中调用输入函数时，需 务必提供 name 参数。
  input('Input your age', name='age', type=NUMBER, validate=check_age)
],validate=check_form)



gift = select("select",['A','B'])
agree = checkbox("checkbox",options=['checked'])
answer = radio("radio", options=['A','B','C'])
text = textarea('text',placeholder='some text')
img = file_upload('select a file',accept="image/*")
# print(img)

# 编辑风格-code：指定代码风格
textarea('code edit', code={'mode':'python','theme':'darcula'}, value='import ...')



### 持续输入pin
from pywebio.pin import *
from pywebio.output import *
# 你已经知道，PyWebIO的输入函数是阻塞式的，并且输入表单会在成功提交后消失。在某些时候，你可能想要输入表单一直显示并可以持续性接收用户输入，
# 这时你可以使用 pywebio.pin 模块。
put_input('input', label='This is a input widget')

# 实际上, pin 组件函数的调用方式和输出函数是一致的，你可以将其作为组合输出的一部分, 也可以将其输出到某个scope中:
put_row([
    put_input('input'),
    put_select('select', options=['A', 'B', 'C'])
])

with use_scope('search-area'):
    put_input('search', placeholder='Search')

# 然后，你可以使用 pin 对象来获取pin组件的值：
put_input('pin_name')
put_buttons(['Get Pin Value'], lambda _: put_text(pin.pin_name))


# pin_wait_change() 监听一组pin组件，当其中任意一个的值发生变化后，函数返回发生变化的组件的 name 和值。
put_input('a', type='number', value=0)
put_input('b', type='number', value=0)
while True:
    changed = pin_wait_change('a', 'b')
    with use_scope('res', clear=True):
        put_code(changed)
        put_text("a + b = %s" % (pin.a + pin.b))

'''
pywebio.pin.put_input(name, type='text', *, label='', value=None, placeholder=None, readonly=None, datalist=None, help_text=None, scope=None, position=- 1) → pywebio.io_ctrl.Output[源代码]
输出一个文本输入组件。参见 pywebio.input.input()

pywebio.pin.put_textarea(name, *, label='', rows=6, code=None, maxlength=None, minlength=None, value=None, placeholder=None, readonly=None, help_text=None, scope=None, position=- 1) → pywebio.io_ctrl.Output[源代码]
输出一个文本域输入组件。参见 pywebio.input.textarea()

pywebio.pin.put_select(name, options=None, *, label='', multiple=None, value=None, help_text=None, scope=None, position=- 1) → pywebio.io_ctrl.Output[源代码]
输出一个下拉选择输入组件。参见 pywebio.input.select()

pywebio.pin.put_checkbox(name, options=None, *, label='', inline=None, value=None, help_text=None, scope=None, position=- 1) → pywebio.io_ctrl.Output[源代码]
输出一个多选框组件。参见 pywebio.input.checkbox()

pywebio.pin.put_radio(name, options=None, *, label='', inline=None, value=None, help_text=None, scope=None, position=- 1) → pywebio.io_ctrl.Output[源代码]
输出一个单选按钮组件。参见 pywebio.input.radio()

pywebio.pin.put_slider(name, *, label='', value=0, min_value=0, max_value=100, step=1, required=None, help_text=None, scope=None, position=- 1) → pywebio.io_ctrl.Output[源代码]
输出一个滑块输入组件。参见 pywebio.input.slider()

pywebio.pin.put_actions(name, *, label='', buttons=None, help_text=None, scope=None, position=- 1) → pywebio.io_ctrl.Output[源代码]
输出一组action按钮。参见 pywebio.input.actions()

不像 actions()` 函数，``put_actions() 不会提交任何表单，它只会设置pin组件的值。 put_actions() 只接受 ‘submit’ 类型的按钮。

'''


'''
pywebio.pin.pin_update(name, **spec)[源代码]
更新pin组件的输出属性。

参数
name (str) – 目标pin组件的 name 。

spec – 需要被更新的pin组件的参数。注意以下参数无法被更新： type, name, code, multiple
'''

if __name__ == '__main__':
    pass
    # start_server('', port=8000)
