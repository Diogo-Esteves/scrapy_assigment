# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy_projectItem(scrapy.Item):
    logo = scrapy.Field()
    phones = scrapy.Field()
    website = scrapy.Field()
