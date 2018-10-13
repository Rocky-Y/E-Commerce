#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Rocky-Y
# @Email   : 1347634801@qq.com

import scrapy
from ..items import DangdangItem
from scrapy.http import Request


class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://dangdang.com/']

    def parse(self, response):
        item=DangdangItem()
        item["title"]=response.xpath("//a[@class='pic']/@title").extract()
        item["link"] =response.xpath("//a[@class='pic']/@href").extract()
        item["comment"] =response.xpath("//a[@name='p_pl']/text()").extract()
        yield item

        for i in range(1,101):
            url="http://search.dangdang.com/?key=python&act=input&page_index="+str(i)
            yield Request(url,callback=self.parse() )
