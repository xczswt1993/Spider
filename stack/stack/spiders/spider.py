#-*- coding;utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem


class StackSpider(Spider):

    """docstring for StackSpider"""
    name = 'stack'
    allow_domains = ['stackoverfow.com']
    start_urls = ['http://stackoverflow.com/questions?pagesize=50&sort=newest']

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath('a/text()').extract()
            item['url'] = question.xpath('a/@href').extract()
            yield item
