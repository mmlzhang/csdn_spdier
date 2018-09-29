# -*-coding: utf-8 -*-

import time
import datetime
import random
import threading
import asyncio

import aiohttp
import pymysql
import requests

from get_article_id import save_article_id

from v3.setting import mysql_config, TIME_DELAY_1, TIME_DEALY_2, MAX_NUM


class Click(object):

    def __init__(self, ):
        self.conn = pymysql.connect(**mysql_config)
        self.url = r'https://blog.csdn.net/zhang_Ming_lu/article/details/'
        self.flag = False
        self.num = 0

    # def __del__(self):
    #     self.conn.close()

    def get_article_id_list(self):
        """从数据库获取 article_id"""
        article_id_list = []
        sql = r'select article_id from tb_csdn'
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            for article_id in cursor.fetchall():
                article_id_list.append(article_id[0])
        self.conn.close()
        return article_id_list

    def article_url(self):
        """拼接 url"""
        article_id_list = self.get_article_id_list()
        while not self.flag:
            self.num += 1
            try:
                pos = random.randint(0, len(article_id_list))
                article_url = self.url + str(article_id_list[pos])
            except Exception:
                article_url = self.url + str(article_id_list[-1])
            if self.num == len(article_id_list):
                # 一个循环到达后，进行休眠，等待多有的线程执行完毕，同时也是进行延迟
                time.sleep(TIME_DELAY_1)
                self.num = 0
            # 每天23点进行url的更新
            hour = datetime.datetime.now().hour
            if int(hour) == 23:
                save_article_id()
                article_id_list = self.get_article_id_list()
                # self.flag = True   # 终止循环
            yield article_url

    async def click(self):
        """模拟点击"""
        article_url = next(self.article_url())
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                async with session.get(article_url, allow_redirects=False) as resp:
                    print(resp.status)
            except Exception as ec:
                print(ec)

    def start(self):
        for i in range(10):
            loop = asyncio.get_event_loop()
            tasks = [self.click(), self.click(), self.click()]
            loop.run_until_complete(asyncio.wait(tasks))


def main():
    csdn = Click()
    csdn.start()


if __name__ == '__main__':
    main()


