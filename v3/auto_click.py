# -*-coding: utf-8 -*-

import datetime
import time
import random
import threading

import pymysql
import requests

from setting import mysql_config, TIME_DELAY_1, TIME_DEALY_2, MAX_NUM

from get_article_id import save_article_id


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
    try:
        requests.get(article_url)
        time.sleep(TIME_DEALY_2)
        id = article_url.split("/")[-1]
        # print(id, end="; ")
    except Exception as e:
        # print()
        id = article_url.split("/")[-1]
        print("点击失败的id:", id)
        print(e)


def click(article_id_list):
    """模拟访问 article_url"""
    url = r'https://blog.csdn.net/zhang_Ming_lu/article/details/'
    num = 0
    count = 0
    # 死循环进行抓取
    while True:
        try:
            pos = random.randint(0, len(article_id_list))
            article_url = url + str(article_id_list[pos])
        except Exception:
            article_url = url + str(article_id_list[-1])
        num += 1
        if num == len(article_id_list):
            # 一个循环到达后，进行休眠，等待多有的线程执行完毕，同时也是进行延迟
            count += num
            print("一个完整的循环结束！ 目前自动点击次数为：{}次！".format(count))
            time.sleep(TIME_DELAY_1)
            num = 0
        # 每天23:30点进行url的更新
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second
        if int(hour) == 23 and int(minute) == 30 and int(second) < 5:
            save_article_id()
            article_id_list = get_article_id_list()
        try:
            # print("进入多线程的url", article_url)
            t = threading.Thread(target=request_get_url, args=(article_url,))
            t.start()
            t.join()
            # print('本次运行结束！！！')
        except Exception:
            pass


def main():
    # 说明： 在死循环中不断获取 url, 将获取的url使用多线程处理
    article_id_list = get_article_id_list()
    click(article_id_list)


if __name__ == "__main__":
    main()
