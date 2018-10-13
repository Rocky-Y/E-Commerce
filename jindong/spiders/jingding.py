#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Rocky-Y
# @Email   : 1347634801@qq.com

from scrapy import Spider,Request
from selenium import webdriver

class JingdongSpider(Spider):
    name = 'jingdong'
    def __init__(self):

        SERVICE_ARGS = ['--load-images=false', '--disk-cache=true', '--ignore-ssl-errors=true']
        self.browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
        self.browser.set_page_load_timeout(30)

    def closed(self,spider):
        print("spider closed")
        self.browser.close()

    def start_requests(self):
        start_urls = ['https://search.jd.com/Search?keyword=python&enc=utf-8&wq=python&pvid=3db6e8a4252a453d9cddf59d4c140b93'.format(str(i)) for i in range(1,10,2)]
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        selector = response.xpath('//ul[@class="gl-warp clearfix"]/li')
        print(len(selector))
        print('-------------------')

