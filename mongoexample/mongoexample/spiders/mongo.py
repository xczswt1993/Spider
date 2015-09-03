# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from mongoexample.items import MongoexampleItem


class MongoSpider(scrapy.Spider):
    name = "mongo"
    allowed_domains = ["stackoverflow.com"]
    start_urls = (
        'http://www.stackoverflow.com/questions?pagesize=50&sort=newest',
    )

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
        for question in questions:
            item = MongoexampleItem()
            item['title'] = question.xpath('a/text()').extract()
            item['url'] = question.xpath('a/@href').extract()
            yield item
