import scrapy
import os
import json
import random
import pandas as pd
import time
from collections import OrderedDict
from snowball.spiders.utils import agents
from snowball.spiders.config import *
from scrapy.cmdline import execute
from scrapy.crawler import CrawlerProcess

class stocklistsSpider(scrapy.Spider):
    name = "stocklist"
    allowed_domains = ["xueqiu.com"]
    start_urls = [STOCK_LIST_URL]
    first = True

    def start_requests(self):

        if os.path.exists(STOCK_LIST_FILE):
            os.remove(STOCK_LIST_FILE)

        request = scrapy.Request(url="https://xueqiu.com", meta={"cookiejar": 1})
        request.headers.setdefault('User-Agent', random.choice(agents))
        request.callback = self.visit_page
        return [request]

    def visit_page(self, response):
        for i, url in enumerate(self.start_urls):
            for num in range(1, 62):
                real_time = str(time.time()).replace('.', '')[0:-1]
                u = url.format(page=str(num), real_time=real_time)
                request = scrapy.Request(u, meta={'cookiejar': response.meta['cookiejar']})
                request.headers.setdefault('User-Agent', random.choice(agents))
                yield request

    def parse(self, response):
        stocks = json.loads(response.text)['stocks']
        current, name, symbol = [], [], []
        for stork in stocks:
            current.append(stork.get('current'))
            name.append(stork.get('name'))
            symbol.append(stork.get('symbol'))
        df = pd.DataFrame(OrderedDict({'name': name, 'symbol': symbol, 'current': current}))
        df.to_csv(STOCK_LIST_FILE, mode='a', header=False, index=False)

if __name__ == '__main__':
    print(os.getcwd())
    execute("scrapy crawl stocklist".split())
