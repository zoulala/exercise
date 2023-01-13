
# ref:https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
# ref:https://python-oracledb.readthedocs.io/en/latest/user_guide/installation.html

import cx_Oracle                                         #引用模块cx_Oracle
conn=cx_Oracle.connect('app_cyfairy_0413@10.129.0.63:1521/csdb')    #连接数据库
conn = cx_Oracle.connect('username','password','192.168.8.212:1521/dbname')
# c=conn.cursor()                                           #获取cursor
# x=c.execute('select sysdate from dual')                   #使用cursor进行各种操作
# x.fetchone()
# c.close()                                                 #关闭cursor
# conn.close()                                              #关闭连接

cursor=conn.cursor()
cursor.execute(sql, )
# results = cursor.fetchall()  # 全部获取
while True:
    results = cursor.fetchmany(12)  # 分页获取，防止使用内存过大
    if not results:
        break
    print(len(results))