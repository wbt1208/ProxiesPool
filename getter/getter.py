from proxies_pool.crawler_model import Crawler
from proxies_pool.save_model import RedisClient
POOL_UPPER = 10000
class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()
    def is_over(self):
        if self.redis.count() > POOL_UPPER:
            return False
        else:
            return False
    def run(self):
        print("获取器开始执行")
        if not self.is_over():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                print(callback)
                proxies = self.crawler.get_proxies(callback)
                print(proxies)
                for proxy in proxies:
                    self.redis.add(proxy)
