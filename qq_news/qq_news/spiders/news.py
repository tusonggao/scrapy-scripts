# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['qq.com']
    start_urls = ['http://news.qq.com/']

    def parse(self, response):
        pass
