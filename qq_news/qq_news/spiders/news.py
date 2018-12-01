# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['qq.com']
    start_urls = ['http://news.qq.com/']

    def parse(self, response):
    	#print(response.body)
    	# print(response.xpath('//div[@class="item major"]//a[@class="linkto"]/@href').extract())
    	for href in response.xpath('//div[@class="item major"]//a[@class="linkto"]/@href').extract():
    		print('href: ', href)
    	pass