# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from proxyspider.items import ProxyspiderItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/6']

    def parse(self, response):
        xpath_info=Selector(response=response).xpath('//p[@class="name"]/a/@href')
        for movie in xpath_info:
            #print(movie)
            movie=movie.extract().strip()
            #print(movie.extract_first().strip())
            movieurl=f'https://maoyan.com{movie}'
            print(movieurl)
            yield scrapy.Request(url=movieurl,callback=self.parse2)

    def parse2(self,response):
        try:
            #title=Selector(response=response).xpath('//h1[@class="name"]/text()')
            title = Selector(response=response).xpath('//div[@class="movie-brief-container"]/h1/text()')
            type=Selector(response=response) .xpath('//li[@class="ellipsis"]/a/text()')
            date=Selector(response=response).xpath('//li[@class="ellipsis"][last()]/text()')
            item = ProxyspiderItem()
            item['title'] = title.extract_first()
            item['type'] = type.extract_first()
            item['date'] = date.extract_first()
        except Exception as e:
            print(e)
        yield  item