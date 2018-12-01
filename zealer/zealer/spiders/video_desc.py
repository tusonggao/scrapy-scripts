# -*- coding: utf-8 -*-
import scrapy


class VideoDescSpider(scrapy.Spider):
    name = 'video_desc'
    allowed_domains = ['zealer.com']
    start_urls = ['http://www.zealer.com/list/']

    def parse(self, response):
    	# if response.url=='http://www.zealer.com/list/'：
    	#print(response.body)
    	#print(response.xpath('//p[@class="series_subTitle"]').extract())
    	
    	print(response.xpath('//p[@class="nav_inner clear"]/a/text()').extract())
    	print(response.xpath('//p[@class="nav_inner clear"]/a/@href').extract())
