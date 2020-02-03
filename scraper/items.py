# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Publisher = scrapy.Field()
    Article_name = scrapy.Field()
    Publish_date = scrapy.Field()
    Article_URL = scrapy.Field()
    Scraping_date = scrapy.Field()
    
