# spider

雪球网爬虫————爬取所有股票代码和股票评论
运行方式：
  1.IDE中运行run.py
  2.Terminal中运行scrapy crawl stocklist 和 scrapy crawl comments
  
结果保存在result文件夹中。

BUG:雪球网反爬虫导致400请求——访问过于频繁，设置代理并未很好地解决。下一步打算用爬虫模拟浏览器爬取。
