import random
import os
import pandas as pd
from snowball.spiders.config import *

class ProxyMiddleware(object):

    def process_request(self, request, spider):

        if spider.name != 'getproxies':
            proxies = pd.read_csv(PROXY_FILES, header=None)
            # request.meta['proxy'] = proxies.sample(1).values[0][0]

    def process_response(self, request, response, spider):
        return response
