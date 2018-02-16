import scrapy
import os
import random
import pandas as pd
import time
import json
from collections import OrderedDict
from lxml import html
from snowball.spiders.utils import agents
from snowball.spiders.config import *
from scrapy.cmdline import execute

class commentsSpider(scrapy.Spider):
    name = "comments"
    allowed_domains = ["xueqiu.com"]
    start_urls = [STOCK_COMMENTS_URL]
    stocks = None

    def start_requests(self):

        if os.path.exists(STOCK_COMMENTS_FILE):
            os.remove(STOCK_COMMENTS_FILE)

        self.stocks = pd.read_csv(STOCK_LIST_FILE)

        request = scrapy.Request(url="https://xueqiu.com", meta={"cookiejar": 1})
        request.headers.setdefault('User-Agent', random.choice(agents))
        request.callback = self.visit_page
        return [request]

    def visit_page(self, response):
        for _, url in enumerate(self.start_urls):
            for _, stock in self.stocks.sample(1).iterrows():
                for page in range(1, 101):
                    real_time = str(time.time()).replace('.', '')[0:-1]
                    u = url.format(symbol=stock.iloc[1], page=str(page), real_time=real_time)
                    request = scrapy.Request(u, meta={'cookiejar': response.meta['cookiejar'], 'symbol': stock.iloc[1], 'name': stock.iloc[0]})
                    request.headers.setdefault('User-Agent', random.choice(agents))
                    yield request

    def parse(self, response):
        print('start parsing...')
        stocks_comment = json.loads(response.text)['list']
        # page = json.loads(response.text)['maxPage']
        comment, user_id, user, title, comment_id, stock_name, stock_code = [], [], [], [], [], [], []
        for stork in stocks_comment:
            text = stork.get('text').strip()
            selector = html.fromstring(text)
            comment.append(selector.xpath('string(.)'))
            user_id.append(stork.get('user_id'))
            user.append(stork.get('user'))
            title.append(stork.get('title'))
            comment_id.append(stork.get('id'))
            stock_name.append(response.meta['name'])
            stock_code.append(response.meta['symbol'])

            df = pd.DataFrame(OrderedDict({'stock_name': stock_name,
                                       'stock_code': stock_code,
                                       'comment': comment,
                                       'user': user,
                                       'title': title}))
        df.to_csv(STOCK_COMMENTS_FILE, mode='a', header=False, index=False)


if __name__ == '__main__':
    print(os.getcwd())
    execute("scrapy crawl comments".split())
