from scrapy.crawler import CrawlerProcess
from snowball.spiders.stocklist import stocklistsSpider
from snowball.spiders.comments import commentsSpider
from snowball.spiders.get_proxies import getProxiesSpider
import os

if __name__ == '__main__':
    print(os.getcwd())
    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
    process.crawl(stocklistsSpider)
    process.start()

    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
    process.crawl(commentsSpider)
    process.start()

    process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
    process.crawl(getProxiesSpider)
    process.start()