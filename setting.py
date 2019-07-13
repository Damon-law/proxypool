# -*- coding: utf-8 -*-

#生成的代理文件
FILE_NAME = 'proxys.json'


# 代理分数
MAX_SCORE = 100
MIN_SCORE = 98  # 要求高一点
INITIAL_SCORE = 10

# 正常的状态码
VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 最大批测试量
BATCH_TEST_SIZE = 10

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'https://baidu.com/'

# 开关
# 测试模块
TESTER_ENABLED = True
# 获取模块
GETTER_ENABLED = True
# 接口模块
API_ENABLED = True