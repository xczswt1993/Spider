#-*- coding:utf-8 -*-
__author__ = 'stone'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import FormRequest, Request
from zhihu.items import ZhihuItem


class ZhihuSpider(CrawlSpider):
    name = 'zhihu'
    allow_dmains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com']
    rules = (Rule(SgmlLinkExtractor(allow=('/question/\d+#.*?')), callback='parse_page', follow=True),
             Rule(SgmlLinkExtractor(allow=('/question/\d+')), callback='parse_page', follow= True))

    headers = {
       'Accept': '*/*',
        'Accept-Encoding' :'gzip, deflate',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Cache-Control' :'no-cache',
        'Connection' :'keep-alive',
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer' :'http://www.zhihu.com/',
        'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0',
    }

    def start_requests(self):
        return [Request('http://www.zhihu.com/#signin', meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        print 'preparing login'

        xsrf = Selector(response).xpath(
            '//input[@name="_xsrf"]/@value').extract()[0]
        return [FormRequest.from_response(response, 'http://www.zhihu.com',
                                          meta={
                                              'cookiejar': response.meta['cookiejar']},
                                          headers=self.headers,
                                          formdata={
                                              '_xsrf': xsrf,
                                              'email': '326688269@qq.com',
                                              'password': 'swt1169876840',
                                          },
                                          callback=self.after_login,
                                          dont_filter=True
                                          )]

    def after_login(self,response):
    	for url in self.start_urls:
    		yield self.make_requests_from_url(url)

    def parse_page(self,response):
    	problem = Selector(response)
    	item = ZhihuItem()
    	item['url'] = response.url
    	item['name'] =  problem.xpath('//h3[@class="zm-item-answer-author-wrap"]/a').extract()
    	item['title'] = problem.xpath('//h2/text()').extract()
    	return item