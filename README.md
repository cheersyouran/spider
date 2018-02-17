# spider

雪球网爬虫————爬取所有股票代码和股票评论

运行方式：
  1. IDE中运行run.py
  2. Terminal中运行scrapy crawl stocklist 和 scrapy crawl comments
  
结果保存在result文件夹下。

[BUG]：雪球网反爬虫导致400错误。如下：
'{"error_description":"您的请求过于频繁，请稍后再试","error_uri":"/statuses/search.json","error_code":"22612"}'

检查了HTTP header格式和Cookie都没问题。设置代理也并未很好地解决。猜测雪球网前后台进行了api访问验证，检测访问的一系列动作看是否是"真人"。在HTTP报文中发现last_id和Trace_id字段，猜想可能与此有关。

下一步打算用爬虫模拟浏览器行为爬取。
