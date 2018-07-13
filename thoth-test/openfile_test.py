#coding=utf8

import os
import xlrd
import re

def method():
    # 方法1：使用os.listdir
    import os

    for filename in os.listdir(r'C:\Users\zoulingwei\Desktop\2016.07.01-2016.09.29\\'):
        print(filename)

    # 方法2：使用glob模块，可以设置文件过滤
    import glob

    for filename in glob.glob(r'C:\Users\zoulingwei\Desktop\2016.07.01-2016.09.29\*.xls'):
        print(filename)

    # 方法3：通过os.path.walk递归遍历，可以访问子文件夹
    import os.path


    def processDirectory(args, dirname, filenames):
        print('Directory', dirname)
        for filename in filenames:
            print( ' File', filename)
    os.path.walk(r'C:\Users\zoulingwei\Desktop\2016.07.01-2016.09.29', processDirectory, None)

    # 方法4：非递归
    import os
    for dirpath, dirnames, filenames in os.walk(r'C:\Users\zoulingwei\Desktop\2016.07.01-2016.09.29'):
        print('Directory', dirpath)
        for filename in filenames:
            print(' File', filename)


if __name__ == "__main__":

    path = r'C:\Users/zoulingwei\Desktop\2016.07.01-2016.09.29\\'
    # 打开每个文件
    for filename in os.listdir(path):
        pathname = path+filename
        #print(path+filename)

        bk = xlrd.open_workbook(pathname)
        try:
            sh = bk.sheet_by_name('TestSheet1')
        except:
            print('no sheet in %s named Sheet1' % path)

        #cols = sh.col_values(-1)

        # 读取文件的每一行，形成对话列表-->保存到mongo
        for i in range(1, sh.nrows):
            row_data = sh.row_values(i)
            if row_data[-2] > 0 and '天龙八部' in row_data[7]:
                print(row_data[7])
                text = row_data[-1]
                r1 = re.findall(r'\n(.*?)\xa0.*\>(.*)', text)

                names = ['IM','player']
                name = r1[0][0]
                dialog = []
                cont_list = []

                for qa in r1:
                    if qa[0] == name:
                        name_changed_flag = False
                        cont_list.append(qa[1])
                    else:
                        name_changed_flag = True


                    if name_changed_flag == True:
                        temp_name = names[0]
                        dialog.append((temp_name,cont_list))
                        cont_list = []
                        cont_list.append(qa[1])
                        name = qa[0]
                        names[0] = names[1]
                        names[1] = temp_name
                print(dialog)
                print (text)