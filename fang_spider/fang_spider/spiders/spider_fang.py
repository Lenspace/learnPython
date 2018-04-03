# -*- coding: utf-8 -*-
import scrapy


class SpiderFangSpider(scrapy.Spider):
    name = 'spider_fang'
    allowed_domains = ['fang.com']
    start_urls = ['http://fang.com/']

    def parse(self, response):
        pass
