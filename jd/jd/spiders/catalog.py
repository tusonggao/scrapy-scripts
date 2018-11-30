# -*- coding: utf-8 -*-
import scrapy


class CatalogSpider(scrapy.Spider):
    # name = 'catalog1'
    # allowed_domains = ['3.cn']
    # start_urls = ['https://dc.3.cn/category/get']

    # def parse(self, response):
    # 	print(response.body)

    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
