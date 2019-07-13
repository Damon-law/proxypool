from tester import Tester
from crawler import Crawler
from setting import *
import sys
import json
class Getter():
    def __init__(self):
        self.cralwer = Crawler()
        self.proxies = []
    def is_over_threadshold(self):
        '''
        判断是否达到上限
        '''
        return False
    def write_json(self):
        '''
        写入json文件
        '''
        try:
            with open(file=FILE_NAME,mode = 'w',encoding = 'utf-8') as f:
                json.dump({'proxies':self.proxies},f)
            f.close()
        except Exception:
            print('写入json文件出错')
    def run(self):
        print("开始获取代理...")
        if not self.is_over_threadshold():
            for callback_label in range(self.cralwer.__CrawlFuncCount__):
                callback = self.cralwer.__CrawlFunc__[callback_label]
                #获取代理
                proxies = self.cralwer.get_proxies(callback)
                sys.stdout.flush()
                for proxy in proxies:
                    ps = proxy.split(':')
                    self.proxies.append({'ip':ps[0],'port':ps[1]})
            self.write_json()