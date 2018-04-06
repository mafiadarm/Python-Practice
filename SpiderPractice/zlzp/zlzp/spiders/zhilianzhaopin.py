# -*- coding: utf-8 -*-
import scrapy

"""
分析二级链接
    1 special.zhaopin.com
        找到新入口 进入addr + jobs.html[或者从关键字 招聘职位 中抓取]
        寻找class = "jobitem"下的a/@href
    2 jobs.zhaopin.com
        进入后直接采集
        
分析职位、区域

"""


class ZhilianzhaopinSpider(scrapy.Spider):
    name = 'zhilianzhaopin'
    allowed_domains = ['http://sou.zhaopin.com/', "http://special.zhaopin.com/"]
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?/']

    def parse(self, response):
        pass

    def usually(self, response):
        pass

    def special(self, response):
        pass

    def parse_item(self, response):
        pass
