#!/usr/bin/python3
import re
import pymysql


# 打开数据库连接
db = pymysql.connect(host='10.0.8.41',
                     user='root',
                     password='Aic@2020',
                     database='sharding_as_communication')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT send_content FROM sharding_as_communication.communication_log_2023 WHERE receive_account like '%15089414758%'order by id desc limit 1;")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print(data)
code=re.findall(r'[0-9]+',str(data))[0]
print(code)

# 关闭数据库连接
db.close()