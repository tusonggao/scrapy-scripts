# -*- coding: utf-8 -*-
import scrapy


class VideoDescSpider(scrapy.Spider):
    name = 'video_desc'
    allowed_domains = ['http://www.zealer.com/list']
    start_urls = ['http://http://www.zealer.com/list/']

    def parse(self, response):
        pass
