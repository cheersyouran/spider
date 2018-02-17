import random

class ProxyMiddleware(object):
    proxy_list = [
        'http://118.114.77.47:8080',
        "http://115.29.236.46:8090",
        'http://218.202.219.82:81',
        'http://119.28.50.37:82',
        'http://120.77.201.46:8080',
        'http://47.92.73.28080',
        'http://61.160.190.147:8090',
    ]
    def process_request(self, request, spider):
        ip = random.choice(self.proxy_list)
        request.meta['proxy'] = ip

    def process_response(self, request, response, spider):
        return response
