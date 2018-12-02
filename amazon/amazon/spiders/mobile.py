# -*- coding: utf-8 -*-
import scrapy

# https://www.bilibili.com/video/av30493305


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=mobile+phone']

    def parse(self, response):
        print('response.url is ', response.url)
        titles = response.xpath('//ul[@id="s-results-list-atf"]/li//h2/text()').extract()
        print('titles is ', titles)
        print('len of titles is', len(titles))
