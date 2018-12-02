# -*- coding: utf-8 -*-
import scrapy


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    allowed_domains = ['amazon.com']
    start_urls = ['http://www.amazon.com/']

    def parse(self, response):
        pass
