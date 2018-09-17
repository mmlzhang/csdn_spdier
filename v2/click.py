# -*-coding: utf-8 -*-


import pymysql
from v2.setting import mysql_config


def get_article_id_list():
    article_id_list = []
    conn = pymysql.connect(**mysql_config)
    sql = r'select article_id from tb_csdn'
    with conn.cursor() as cursor:
        cursor.execute(sql)
        for article_id in cursor.fetchall():
            article_id_list.append(article_id[0])
    return article_id_list


