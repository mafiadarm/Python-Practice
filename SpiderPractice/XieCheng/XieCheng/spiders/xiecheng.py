# -*- coding: utf-8 -*-
import scrapy


class XiechengSpider(scrapy.Spider):
    name = 'xiecheng'
    allowed_domains = ['ctrip.com']
    start_urls = ['http://www.ctrip.com//']

    def parse(self, response):
        pass
