# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spider2.items import Spider2Item


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/6']

    def parse(self, response):
        xpath_info=Selector(response=response).xpath('//p[@class="name"]')
        for movieurl in xpath_info:
            movieurl=movieurl.xpath('./a/@href').extract_first().strip()
            movieurl=(f'https://maoyan.com{movieurl}')
            print(movieurl)
            yield scrapy.Request(url=movieurl,callback=self.parse2)

    def parse2(self,response):
        title = Selector(response=response).xpath('//div[@class="movie-brief-container"]/h1/text()')
        type = Selector(response=response).xpath('//li[@class="ellipsis"]/a/text()')
        movie_date = Selector(response=response).xpath('//li[@class="ellipsis"][last()]/text()')
        item = Spider2Item()
        item['title'] = title.extract_first().strip()
        item['type'] = type.extract_first().strip()
        item['movie_date'] = movie_date.extract_first().strip()
        #print('------------')
        yield item
