'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 14:11
# @Author  : qijincheng
# @email   : 877767216@qq.com
# @Site    : 
# @File    : Connect_db.py
# @Software: PyCharm

'''

import pymysql

IP = 'rm-m5eeoyyg67i2c84mc1o.mysql.rds.aliyuncs.com'
Port = 3306
user = 'user_dev'
pwd = 'Aa123654'
database = 'house_dev' # 必须是正确的库名



conn = pymysql.connect(host = IP,port = Port,user = 'user_dev',passwd = pwd,db = database)

cursor = conn.cursor()

sql = "SELECT * FROM house_pm_member_t WHERE id = %s or id = %s"
cursor.execute(sql,args=(78,80))

print('fetchall的输出结果：',cursor.fetchall())