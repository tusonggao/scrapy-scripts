# -*- coding: utf-8 -*-
import scrapy

class VideoDescSpider(scrapy.Spider):
    name = 'video_desc'
    allowed_domains = ['amazon.com']
    page_num = 1
    start_urls = ['https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=mobile+phone']

    # https://www.amazon.com/s/ref=sr_pg_2?fst=p90x%3A1%2Cas%3Aon&rh=n%3A2335752011%2Ck%3Amobile+phone&page=2&keywords=mobile+phone&ie=UTF8&qid=1543706897
    # https://www.amazon.com/gp/search/ref=sr_pg_3?fst=p90x%3A1%2Cas%3Aon&rh=n%3A2335752011%2Ck%3Amobile+phone&page=3&keywords=mobile+phone&ie=UTF8&qid=1543706940

    def parse(self, response):
        # if response.url=='http://www.zealer.com/list/'：
        #print(response.body)
        #print(response.xpath('//p[@class="series_subTitle"]').extract())

        product_titles = response.xpath('//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]/text()').extract()
        product_urls = response.xpath('//a[@class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/@href').extract()
        product_price1 = response.xpath('//span[@class="sx-price-whole"]').extract()
        product_price2 = response.xpath('//sup[@class="sx-price-fractional"]').extract()

        print('response.url is', response.url)
        print('product_titles is', product_titles)
        print('len of four', len(product_titles), len(product_urls),
            len(product_price1), len(product_price2))

        print()

        if self.page_num>1:
            return

        url_next_page = response.xpath('//a[@id="pagnNextLink"]/@href').extract_first()
        url_next_page = 'https://www.amazon.com/' + url_next_page
        #print('url_next_page is: ', url_next_page)
        yield scrapy.Request(url_next_page, callback=self.parse)

        self.page_num += 1
