# -*-coding: utf-8 -*-


# -*-coding: utf-8 -*-

"""

    Linux 下使用，多线程实现点击事件，访问数增加

"""

import time
import threading
import requests

from selenium import webdriver

from setting import *


def get_article_url_list():
    """读取文件，获取article_url_list"""
    with open('csdn_article_url.txt', 'r', encoding='utf-8') as f:
        article_url_list = [url.replace('\n', '') for url in f.readlines()]
        return article_url_list


def get_url(article_url):
    """phantomjs 获取url的数据，模拟浏览器发起请求，访问数量加 1 """
    browser = webdriver.PhantomJS(phantomjs_driver)
    browser.get(article_url)
    time.sleep(1)
    browser.close()


def request_get_url(article_url):
    requests.get(article_url)


def main():
    article_url_list = get_article_url_list()
    num = 0
    flag = True
    while flag:
        article_url = article_url_list[num]
        num += 1
        if num == len(article_url_list):
            num = 0
            # flag = False
            time.sleep(60)
        # t = threading.Thread(target=get_url, args=(article_url,))
        t = threading.Thread(target=request_get_url, args=(article_url,))
        t.start()
        time.sleep(8)
    print('运行结束！！！')


if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time()
    print("共计耗时：", t2 - t1)
