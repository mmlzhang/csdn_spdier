# -*-coding: utf-8 -*-

import time
import random
import threading

import pymysql
import requests

from v2.setting import mysql_config, TIME_DELAY_1, TIME_DEALY_2, MAX_NUM


def get_article_id_list():
    """从数据库获取 article_id"""
    article_id_list = []
    conn = pymysql.connect(**mysql_config)
    sql = r'select article_id from tb_csdn'
    with conn.cursor() as cursor:
        cursor.execute(sql)
        for article_id in cursor.fetchall():
            article_id_list.append(article_id[0])
    return article_id_list


def request_get_url(article_url):
    """获取article_url的文章，使访问数量加1"""
    requests.get(article_url)


def click(article_id_list):
    """模拟访问 article_url"""
    url = r'https://blog.csdn.net/zhang_Ming_lu/article/details/'
    num = random.randint(0, len(article_id_list))
    flag = True
    while flag:
        try:
            article_url = url + str(article_id_list[num])
        except Exception:
            article_url = url + str(article_id_list[-1])
        num += 1
        if num == len(article_id_list):
            flag = False
        print(article_url)
        t = threading.Thread(target=request_get_url, args=(article_url,))
        t.start()
        t.join()
        time.sleep(TIME_DEALY_2)
    # print('本次运行结束！！！')
    return True


def main():
    article_id_list = get_article_id_list()
    flag = True
    num = 0
    while flag:
        num += 1
        # print("开始运行！！！ ")
        click(article_id_list)
        time.sleep(TIME_DELAY_1)
        if num > MAX_NUM:
            flag = False


if __name__ == "__main__":
    main()
