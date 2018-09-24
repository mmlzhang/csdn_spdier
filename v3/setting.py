
# MySQL 配置
mysql_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'zhang',
    'passwd': '123456',
    'db': 'lanms',
    'charset': 'utf8',
    'autocommit': False
    }

# CSDN 博客点击设置

# 将所有文章的url全部请求一次的时间间隔
TIME_DELAY_1 = 300
# 每个url请求之间的时间间隔
TIME_DEALY_2 = 3
# 最大访问的次数, 即每个文章的最大访问次数
MAX_NUM = 10000