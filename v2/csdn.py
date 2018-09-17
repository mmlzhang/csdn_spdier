# -*-coding: utf-8 -*-

import datetime

import pymysql

from v2.setting import mysql_config


num_list = []
# with open('../csdn_article_url.txt', 'r', encoding='utf-8') as f:
#     urls = f.read()
#     for url in urls.split("\n"):
#         num = url.split(r'/')[-1]
#         num_list.append(num)

# 连接 mysql 存入数据库
conn = pymysql.connect(**mysql_config)
sql = r'insert into tb_csdn (article_id, create_time) values (%s,%s)'
with conn.cursor() as cursor:
    create_time = datetime.datetime.now().strftime('%Y-%m-%d %X')
    for num in num_list:
        cursor.execute(sql, (num, create_time))
        conn.commit()
conn.close()
