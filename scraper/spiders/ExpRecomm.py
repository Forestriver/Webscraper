# -*- coding: utf-8 -*-
import scrapy


class ExprecommSpider(scrapy.Spider):
    name = 'ExpRecomm'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
