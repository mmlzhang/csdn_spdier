# -*-coding: utf-8 -*-

import time
import random
import threading

import pymysql
import requests

from v2.setting import mysql_config, TIME_DELAY_1, TIME_DEALY_2


def get_article_id_list():
    article_id_list = []
    conn = pymysql.connect(**mysql_config)
    sql = r'select article_id from tb_csdn'
    with conn.cursor() as cursor:
        cursor.execute(sql)
        for article_id in cursor.fetchall():
            article_id_list.append(article_id[0])
    return article_id_list


def request_get_url(article_url):
    requests.get(article_url)


def main():
    url = r'https://blog.csdn.net/zhang_Ming_lu/article/details/'
    article_id_list = get_article_id_list()
    num = random.randint(0, len(article_id_list))
    flag = True
    while flag:
        try:
            article_url = url + str(article_id_list[num])
        except Exception:
            article_url = url + str(article_id_list[-1])
        num += 1
        if num == len(article_id_list):
            num = 0
            time.sleep(TIME_DELAY_1)
        print(article_url)
        t = threading.Thread(target=request_get_url, args=(article_url,))
        t.start()
        time.sleep(TIME_DEALY_2)
    print('运行结束！！！')


if __name__ == "__main__":
    main()