# -*- coding: utf-8 -*-
import scrapy


class MobileSpider(scrapy.Spider):
    name = 'mobile'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=mobile+phone']

    def parse(self, response):
        print(response.body)
        titles = response.xpath('//ul[@class="s-results-list-atf"]/li//h2/text()').extract()
        print('titles is ', titles)
