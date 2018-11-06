import xlwt

def QAs_text():
    import re
    lib_file = 'd:\数据\QUESTIONS.csv'
    feed_file = 'd:\数据\FEEDBACKS.csv'

    QAs_file = 'd:\数据\query_text.txt'

    f_w = open(QAs_file, 'w')
    libs = {}
    with open(lib_file, 'r') as fs:
        print(fs.readline())
        lss = fs.readline().split(',')
        for line in fs:
            ls = line.split(',')
            if not re.findall(r'[^0-9]+', ls[0]):  # 遇到开头id是纯数字，则处理上一个样本lss
                if lss[-2] == '1': libs[lss[0]] = lss[2]
                lss = ls
            else:
                lss += ls
        if lss[-2] == '1': libs[lss[0]] = lss[2]  # 最后一句
    print('libs number:', len(libs))

    n = 0
    with open(feed_file, 'rb') as f:
        print(f.readline())
        for line in f:
            try:
                line = line.decode(encoding='gbk')
                ls = line.split(',')
                if len(ls) >= 11:  # 问题中带'\n'将被忽略
                    n += 1
                    query = ','.join(ls[1:-9])
                    g_id = ls[-5]
                    score = ls[-6]
                    q_id = ls[-9]
                    if g_id == '1':
                        f_w.write(query + '\n')

                        # if g_id=='1' and q_id in libs:
                        #     title = libs[q_id]
                        #     f_w.write(query+'\t:\t'+title+'\t:\t'+score+'\n')
            except Exception as e:
                print('error', n, e)
                continue
    print('samples number:', n)
    f_w.close()

def title_text():
    import re
    lib_file = 'd:\数据\QUESTIONS.csv'
    w_file = 'd:\数据\\answers_text.txt'

    f_w = open(w_file, 'w')
    libs = {}
    with open(lib_file, 'r') as fs:
        print(fs.readline())
        lss = fs.readline().split(',')
        for line in fs:
            ls = line.split(',')
            if not re.findall(r'[^0-9]+', ls[0]):  # 遇到开头id是纯数字，则处理上一个样本lss
                ans = ' '.join(''.join(lss[3:-12]).split('\n'))
                if lss[-2] == '1': f_w.write(ans + '\n')
                lss = ls
            else:
                lss += ls

    print('libs number:', len(libs))
    f_w.close()


def score_text():
    QAs_file = 'd:\数据\\QAs_text.txt'
    score_file = 'd:\数据\\score_text.txt'

    ws_f = open(score_file, 'w', encoding='utf8')
    with open(QAs_file, 'r', encoding='gbk') as f:
        a, y, n = 0, 0, 0
        for line in f:
            a += 1
            ls = line.strip().split('\t:\t')
            if ls[-1] == '2':
                n += 1
                ws_f.write(line)
            if ls[-1] == '1':
                y += 1
                ws_f.write(line)
        print('all:', a)
        print('y:', y)
        print('n:', n)
    ws_f.close()


def sort_to_excel():
    '''评价数据按次数排序'''
    score_file = 'd:\数据\\score_text.txt'
    yes_dict = {}
    no_dict = {}

    with open(score_file,'r',encoding='utf8') as f:
        for line in f:
            ls = line.strip().split('\t:\t')
            if ls[-1]=='2':
                no_str = ls[0]+'\t:\t'+ls[1]
                if no_str in no_dict:
                    no_dict[no_str] += 1
                else:
                    no_dict[no_str] = 1
            if ls[-1] == '1':
                yes_str = ls[0]+'\t:\t'+ls[1]
                if yes_str in yes_dict:
                    yes_dict[yes_str] += 1
                else:
                    yes_dict[yes_str] = 1

    no_tuple = sorted(no_dict.items(), key=lambda x: x[1], reverse=True)  # 按照第1个元素降序排列
    yes_tuple = sorted(yes_dict.items(), key=lambda x: x[1], reverse=True)  # 按照第1个元素降序排列

    outputbook = xlwt.Workbook()
    yh = outputbook.add_sheet('sheet1', cell_overwrite_ok=True)
    nh = outputbook.add_sheet('sheet2', cell_overwrite_ok=True)
    y_index = 0
    for y_str,y_n in yes_tuple[:65500]:
        ys = y_str.split('\t:\t')
        yh.write(y_index, 0, ys[0])
        yh.write(y_index, 1, ys[1])
        yh.write(y_index, 2, y_n)
        y_index+=1

    n_index = 0
    for n_str, n_n in no_tuple[:65500]:
        ns = n_str.split('\t:\t')
        nh.write(n_index, 0, ns[0])
        nh.write(n_index, 1, ns[1])
        nh.write(n_index, 2, n_n)
        n_index += 1

    path = 'd:\数据\\score_sorted.xls'
    outputbook.save(path)

def sort_sameQAs_to_excel():
    '''问句和回复相同 统计按次数排序'''
    score_file = 'd:\数据\\score_text.txt'
    yes_dict = {}
    no_dict = {}

    with open(score_file, 'r', encoding='utf8') as f:
        for line in f:
            ls = line.strip().split('\t:\t')
            if ls[-1] == '2':
                no_str = ls[0] + '\t:\t' + ls[1]
                if no_str in no_dict:
                    no_dict[no_str] += 1
                else:
                    no_dict[no_str] = 1
            if ls[-1] == '1':
                yes_str = ls[0] + '\t:\t' + ls[1]
                if yes_str in yes_dict:
                    yes_dict[yes_str] += 1
                else:
                    yes_dict[yes_str] = 1

    no_tuple = sorted(no_dict.items(), key=lambda x: x[1], reverse=True)  # 按照第1个元素降序排列
    yes_tuple = sorted(yes_dict.items(), key=lambda x: x[1], reverse=True)  # 按照第1个元素降序排列

    outputbook = xlwt.Workbook()
    yh = outputbook.add_sheet('sheet1', cell_overwrite_ok=True)
    nh = outputbook.add_sheet('sheet2', cell_overwrite_ok=True)
    y_index = 0
    for y_str, y_n in yes_tuple:
        ys = y_str.split('\t:\t')
        # if re.sub(r'[^\w]+', '', ys[0]) == re.sub(r'[^\w]+', '', ys[1]):
        if ys[0] == ys[1]:
            yh.write(y_index, 0, ys[0])
            yh.write(y_index, 1, ys[1])
            yh.write(y_index, 2, y_n)
            y_index += 1

    n_index = 0
    for n_str, n_n in no_tuple:
        ns = n_str.split('\t:\t')
        if ns[0] == ns[1]:
            nh.write(n_index, 0, ns[0])
            nh.write(n_index, 1, ns[1])
            nh.write(n_index, 2, n_n)
            n_index += 1

    path = 'd:\数据\\score_sameQAsorted.xls'
    outputbook.save(path)

def unique_QAs_text():
    score_file = 'd:\数据\\score_text.txt'
    w_file = 'd:\数据\\unique_text.txt'
    w_f = open(w_file, 'w', encoding='utf8')
    set_list = {}
    with open(score_file, 'r', encoding='utf8') as f:
        for line in f:
            if line not in set_list:
                w_f.write(line)
                set_list[line]=1

    w_f.close()


# score_text()
#
# sort_to_excel()
#
# sort_sameQAs_to_excel()
unique_QAs_text()