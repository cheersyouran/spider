# snowball-spider

爬取雪球网所有股票代码和股票评论

运行方式：
  1. IDE中运行run.py
  2. Terminal中运行scrapy crawl stocklist 和 scrapy crawl comments
  
结果保存在result文件夹下。

----

[BUG]：雪球网反爬虫导致400错误。如下：
'{"error_description":"您的请求过于频繁，请稍后再试","error_uri":"/statuses/search.json","error_code":"22612"}'

检查了HTTP header格式和Cookie都没问题。设置代理也并未很好地解决。
在HTTP报文中发现last_id和Trace_id字段，猜想可能与此有关。

下一步打算用爬虫模拟浏览器行为爬取。

---
2018.02.17更新

把代理关了，设置download_delay=8s，Upgrade-Insecure-Requests=1， 竟然好用了。。
不过下载数据量大ip应该还是要被封。等有钱了买点ip用。