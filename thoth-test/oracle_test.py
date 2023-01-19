
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


import oracledb
from datetime import datetime
oracledb.init_oracle_client(lib_dir="/Users/zlw/Downloads/instantclient_19_8")
conn = oracledb.connect(user='zy_lclj',password='zy_lclj',dsn='192.168.8.212:1521/orcl')
cursor = conn.cursor()
sql = "select PATIENT_NAME,SEX,DIAG_TYPE,DIAG_NO,DIAG_CODE,DIAG_NAME from T_DWD_DIAG_CAT  where PATIENT_ID=:patient_id and VISIT_ID=:visit_id"
sql = "select PATIENT_NAME,SEX,DIAG_TYPE,DIAG_NO,DIAG_CODE,DIAG_NAME from T_DWD_DIAG_CAT WHERE ROWNUM <= 40"
sql = "select operation_icd_no, oper_code, oper_name from t_dwd_operation_icd  WHERE ROWNUM <= 100"
# params = {
#             # "limit": 5,
#             "patient_id": '8675393',
#             "visit_id": 4
#         }
table1 = 't_dwd_inpatient'
start_time = '2017-12-01'
end_time = '2018-12-01'
start_time = datetime.strptime(start_time, '%Y-%m-%d')
end_time = datetime.strptime(end_time, '%Y-%m-%d')


# sql = "select patient_id, visit_id from %s  where admiss_diag_date between to_date(:start_time,'yyyy-mm-dd') and to_date(:end_time,'yyyy-mm-dd')" % table1
sql = "select patient_id, visit_id from %s  where admiss_diag_date between :start_time and :end_time" % table1

params = {
    # "talbe": table1,
    "start_time": start_time,
    "end_time": end_time,
}

cursor.execute(sql, params)
# results = cursor.fetchall()  # 全部获取
while True:
    results = cursor.fetchmany(12)  # 分页获取，防止使用内存过大
    if not results:
        break
    print(len(results))

exit()
sql ="""SELECT last_name
     FROM employees
     ORDER BY last_name
     OFFSET :offset ROWS FETCH NEXT :maxnumrows ROWS ONLY"""
cursor.execute(sql, offset=101, maxnumrows=300)


