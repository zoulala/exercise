import re
import xlwt
import pymysql
MYSQL_SETTINGS1 = {"user": "root", "host": "10.12.28.223", "port": 3306, "passwd": "root"}
# MYSQL_SETTINGS1 = {"user": "root", "host": "localhost", "port": 3306, "passwd": "560320"}

class Mysql():
    def __init__(self, dbname):
        self.db = pymysql.connect(MYSQL_SETTINGS1["host"], MYSQL_SETTINGS1["user"], MYSQL_SETTINGS1["passwd"],
                                  charset='utf8')
        sql = 'create database if not exists %s' % dbname
        self.cursor = self.db.cursor()
        # self.cursor.execute(sql)
        self.db.select_db(dbname)  # 选中数据库

    def __del__(self):
        self.db.commit()
        self.db.close()
        # print('------------')

    def create_table_mysql(self, sql_str="create table if not exists table1("
                                         "id int(1) unsigned not null auto_increment primary key,"
                                         "data_id int(1),"
                                         "content text(5000),"
                                         "time datetime"
                                         ");"):
        self.cursor.execute(sql_str)

    def select_from_mysql(self, sql_str, count=-1):
        '''sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d'" % (1000)'''
        self.cursor.execute(sql_str)
        if count > 0:
            result = self.cursor.fetchall()
        else:
            result = self.cursor.fetchone()
        return result

    def insert_into_mysql(self, sql_str, data):
        '''sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)'''
        self.cursor.execute(sql_str, data)

    def remove_from_mysql(self, sql_str):
        '''sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)'''
        self.cursor.execute(sql_str)

    def update_from_mysql(self, sql_str):
        '''sql = "UPDATE EMPLOYEE SET AGE = AGE + 1
                          WHERE SEX = '%c'" % ('M')'''
        self.cursor.execute(sql_str)


def QAs_to_text():
    ob = Mysql('test')
    # sql = 'insert into aaa (content,question_id,title,related_id,msg_owner_type,evaluate) select content,question_id,title,related_id,msg_owner_type,evaluate from export'
    # ob.create_table_mysql(sql)

    w_file = 'd:\数据\\zhiU_QAs.txt'
    w_f = open(w_file,'w',encoding='utf8')
    id_i = 0
    er_n = 0
    while 1:
        id_i += 1
        query, title = '', ''
        sql = 'select * from aaa where id=%d' % id_i
        result = ob.select_from_mysql(sql)
        score = result[-1]
        try:
            if result[5]==0:
                query = result[1]
                sql = "select title from aaa where related_id='%s' and msg_owner_type=1" % result[4]
                title = ob.select_from_mysql(sql)[0]
            if result[5]==1:
                title = result[3]
                sql = "select content from aaa where related_id='%s' and msg_owner_type=0" % result[4]
                query = ob.select_from_mysql(sql)[0]
        except Exception as e:
            er_n += 1

        if query and title:
            w_f.write(query+'\t+\t'+title+'\t+\t'+str(score)+'\n')
        if id_i%1000==0:
            print(id_i,'err_n:',er_n,' :',query,' : ',title)

def query_to_text():
    QAs_file = 'd:\数据\\zhiU_QAs_text.txt'
    query_file = 'd:\数据\\zhiU_query_text.txt'
    score_file = 'd:\数据\\zhiU_score_text.txt'
    w_f = open(query_file,'w',encoding='utf8')
    ws_f = open(score_file,'w',encoding='utf8')
    with open(QAs_file, 'r',encoding='utf8') as f:
        a,y,n = 0,0,0
        for line in f:
            a += 1
            ls = line.strip().split('\t+\t')
            w_f.write(ls[0]+'\n')
            if ls[-1]=='1':
                n+=1
                ws_f.write(line)
            if ls[-1]=='2':
                y+=1
                ws_f.write(line)
        print('all:',a)
        print('y:',y)
        print('n:',n)
    w_f.close()
    ws_f.close()

def sort_to_excel():
    '''评价数据按次数排序'''
    score_file = 'd:\数据\\zhiU_score_text.txt'
    yes_dict = {}
    no_dict = {}

    with open(score_file,'r',encoding='utf8') as f:
        for line in f:
            ls = line.strip().split('\t+\t')
            if ls[-1]=='1':
                no_str = ls[0]+'\t+\t'+ls[1]
                if no_str in no_dict:
                    no_dict[no_str] += 1
                else:
                    no_dict[no_str] = 1
            if ls[-1] == '2':
                yes_str = ls[0]+'\t+\t'+ls[1]
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
    for y_str,y_n in yes_tuple:
        ys = y_str.split('\t+\t')
        yh.write(y_index, 0, ys[0])
        yh.write(y_index, 1, ys[1])
        yh.write(y_index, 2, y_n)
        y_index+=1

    n_index = 0
    for n_str, n_n in no_tuple:
        ns = n_str.split('\t+\t')
        nh.write(n_index, 0, ns[0])
        nh.write(n_index, 1, ns[1])
        nh.write(n_index, 2, n_n)
        n_index += 1

    path = 'd:\数据\\zhiU_score_sorted.xls'
    outputbook.save(path)

def sort_sameQAs_to_excel():
    '''问句和回复相同 统计按次数排序'''
    score_file = 'd:\数据\\zhiU_score_text.txt'
    yes_dict = {}
    no_dict = {}

    with open(score_file, 'r', encoding='utf8') as f:
        for line in f:
            ls = line.strip().split('\t+\t')
            if ls[-1] == '1':
                no_str = ls[0] + '\t+\t' + ls[1]
                if no_str in no_dict:
                    no_dict[no_str] += 1
                else:
                    no_dict[no_str] = 1
            if ls[-1] == '2':
                yes_str = ls[0] + '\t+\t' + ls[1]
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
        ys = y_str.split('\t+\t')
        if re.sub(r'[^\w]+','',ys[0])==re.sub(r'[^\w]+','',ys[1]):
            yh.write(y_index, 0, ys[0])
            yh.write(y_index, 1, ys[1])
            yh.write(y_index, 2, y_n)
            y_index += 1

    n_index = 0
    for n_str, n_n in no_tuple:
        ns = n_str.split('\t+\t')
        if re.sub(r'[^\w]+','',ns[0])==re.sub(r'[^\w]+','',ns[1]):
            nh.write(n_index, 0, ns[0])
            nh.write(n_index, 1, ns[1])
            nh.write(n_index, 2, n_n)
            n_index += 1

    path = 'd:\数据\\zhiU_score_sameQAsorted1.xls'
    outputbook.save(path)


# QAs_to_text()
query_to_text()
# sort_to_excel()
# sort_sameQAs_to_excel()
