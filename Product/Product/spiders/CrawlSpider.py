#-*- coding:utf-8 -*-
__author__ = 'stone'

import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import  LinkExtractor

class Myspider(CrawlSpider):
	name = ''
	allowed_domains = ['']
	start_urls = []

	rules = (
		Rule(LinkExtractor(allow=('category\.php'),deny=('subsection\.php'))),
		Rule(LinkExtractor(allow=('item\.php')),callback='parse_item')
		)
	def parse_item(self,response):
		self.logger.info('hi ,this is an item page! %s',response.url)
		item = Product()
		item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
