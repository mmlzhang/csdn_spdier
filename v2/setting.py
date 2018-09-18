
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
ARTICLE_TITLE_XPATH = r'//h4/a//text()'
BASE_URL = r'https://blog.csdn.net/zhang_ming_lu/article/list/{page_num}'

# 将所有文章的url全部请求一次的时间间隔
TIME_DELAY_1 = 18
# 每个url请求之间的时间间隔
TIME_DEALY_2 = 3
# 最大访问的次数, 即每个文章的最大访问次数
MAX_NUM = 10000