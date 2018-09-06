# -*-coding: utf-8 -*-

import time

from selenium import webdriver

from setting import *
from redis_conn import RedisClient


browser = webdriver.PhantomJS(phantomjs_driver)
article_url_list = []
for page_num in range(PAGE_RANGE):
    url = BASE_URL.format(page_num=page_num+1)
    browser.get(url)
    tag_a_list = browser.find_elements_by_xpath(ARTICLE_URL_XPATH)
    for a in tag_a_list:
        href = a.get_attribute('href')
        article_url_list.append(href)
# 关闭浏览器
browser.close()

print(article_url_list)
num = 0
while True:
    # 访问文章的url，是访问数增加
    for article_url in article_url_list:
        num += 1
        # 设置代理
        random_proxy = RedisClient().random()
        proxy = '--proxy=' + random_proxy
        proxy_type = '--proxy-type=http'
        # service_args = [
        #     proxy,
        #     proxy_type,
        #     # '--proxy-auth=username:password'
        # ]
        service_args = None
        browser = webdriver.PhantomJS(phantomjs_driver, service_args=service_args)
        browser.get(article_url)
        time.sleep(1)
        print(num)
        browser.close()

# 将文章的 url 写入放到文件中
# with open('csdn_article_url.txt', 'w', encoding='utf-8') as f:
#     for article_url in article_url_list:
#         f.write(article_url+'\n')
