
# MySQL 配置
mysql_config = {
    'host': '39.104.171.126',
    'port': 3306,
    'user': 'zhang',
    'passwd': '123456',
    'db': 'lanms',
    'charset': 'utf8',
    'autocommit': False
    }

# CSDN 博客点击设置
# 页码数
PAGE_RANGE = 3
# 每个文章的url的 xpath
ARTICLE_URL_XPATH = r'//h4/a'
BASE_URL = r'https://blog.csdn.net/zhang_ming_lu/article/list/{page_num}'
