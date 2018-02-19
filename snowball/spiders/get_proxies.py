import scrapy
import os
import pandas as pd
from collections import OrderedDict
from snowball.spiders.config import *
from scrapy.cmdline import execute

class getProxiesSpider(scrapy.Spider):
    name = "getproxies"
    allowed_domains = ["kuaidaili.com"]
    start_urls = [PROXY_URL]
    first = True

    def start_requests(self):
        if os.path.exists(PROXY_FILES):
            os.remove(PROXY_FILES)

        request = scrapy.Request(url="https://www.kuaidaili.com", meta={"cookiejar": 1})
        request.callback = self.visit_page
        return [request]

    def visit_page(self, response):
        for _, url in enumerate(self.start_urls):
            for page in reversed(range(1, 10)):
                u = url.format(page=str(page))
                request = scrapy.Request(u, meta={'cookiejar': response.meta['cookiejar']})
                yield request

    def parse(self, response):
        ip = response.selector.xpath('//td[contains(@data-title, "IP")]/text()').extract()
        port = response.selector.xpath('//td[contains(@data-title, "PORT")]/text()').extract()
        proxy = []
        for i, j in zip(ip, port):
            proxy.append('http://' + i + ':' + j)
        df = pd.DataFrame(OrderedDict({'PROXY': proxy}))
        df.to_csv(PROXY_FILES, mode='a', header=False, index=False)

if __name__ == '__main__':
    print(os.getcwd())
    execute("scrapy crawl getproxies".split())
