# Redis数据库地址
REDIS_HOST = '39.104.171.126'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = 123456

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

# 状态可用是返回的 状态码
VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'http://www.baidu.com'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10

# CSDN 博客点击设置
# 页码数
PAGE_RANGE = 3
# 每个文章的url的 xpath
ARTICLE_URL_XPATH = r'//h4/a'
BASE_URL = r'https://blog.csdn.net/zhang_ming_lu/article/list/{page_num}'
phantomjs_driver = r'D:\venv\tools\spider\selenium\phantomjs-2.1.1-windows\bin\phantomjs.exe'