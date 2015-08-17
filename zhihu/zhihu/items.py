# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     url = scrapy.Field()
     title = scrapy.Field()
     descrpition = scrapy.Field()
     answer = scrapy.Field()
     name = scrapy.Field()
