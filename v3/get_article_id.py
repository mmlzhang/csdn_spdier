# -*-coding: utf-8 -*-


"""抓取 csdn 博客文章的标题和id 存入 mysql 中"""
import datetime

import pymysql
import requests
from bs4 import BeautifulSoup

from setting import mysql_config


def get_url():
    """获取文章的 id 和 标题"""
    page_num = 0
    flag = True
    while flag:
        page_num += 1
        page_url = r'https://blog.csdn.net/zhang_ming_lu/article/list/{page_num}'
        page_html = requests.get(page_url.format(page_num=page_num))
        bsObj = BeautifulSoup(page_html.content, 'lxml')
        elements = bsObj.find_all('h4')
        if not elements:
            flag = False
        for element in elements[1:]:
            article_id = element.find('a').attrs['href'].split('/')[-1]
            article_title = element.text.strip().split('\n')[-1].strip()
            yield (article_title, article_id)


def mysql_conn():
    """连接mysql数据库"""
    mysql_conn = pymysql.connect(**mysql_config)
    return mysql_conn


def save_article_id():
    conn = mysql_conn()
    sql_insert = r'insert into tb_csdn (article_id, title, create_time) values (%s, %s, %s)'
    sql_select_ids = r'select article_id from tb_csdn'
    # sql = r'update tb_csdn set article_id="{article_id}", title="{article_title}", create_time="{create_time}" ' \
    #       r'where article_id="{article_id}"'
    for article_title, article_id in get_url():
        with conn.cursor() as cursor:
            cursor.execute(sql_select_ids)
            ids = cursor.fetchall()
            id_list = []
            for id in ids:
                id_list.append(id[0])
            if int(article_id) not in id_list:
                print(article_title, article_id)
                create_time = datetime.datetime.now().strftime('%Y-%m-%d %X')
                cursor.execute(sql_insert, (article_id, article_title, create_time))
                conn.commit()
    conn.close()


if __name__ == '__main__':
    save_article_id()
