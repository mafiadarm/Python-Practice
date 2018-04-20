# -*- coding: utf-8 -*-
import re

import scrapy
from ..items import JokejiItem


class JokeSpider(scrapy.Spider):
    name = 'joke'
    offset = 1
    allowed_domains = ['www.jokeji.cn']
    baseUrl = 'http://www.jokeji.cn'
    start_urls = [baseUrl]

    def parse(self, response):
        urls = response.xpath("//*[@class='joketype l_left']/ul/li/a/@href").extract()
        for url in urls:
            start_url = self.baseUrl + url
            yield scrapy.Request(url=start_url, callback=self.parse_list)

    def parse_list(self, response):
        ii = response.xpath("//*[@class='next_page']/a[last()]/@href").extract_first()

        get_page = re.compile("._(\d+)\.htm")
        all_page = get_page.findall(ii)[0]

        next_page = response.url.replace("_1", "_%s")
        for num in range(1, int(all_page)+1):
            url = next_page % num
            yield scrapy.Request(url=url, callback=self.parse_finally_page)

    def parse_finally_page(self, response):
        urls = response.xpath("//*[@class='list_title']/ul/li/b/a/@href").extract()
        for url in urls:
            yield scrapy.Request(url=self.baseUrl + url, callback=self.parse_content)

    def parse_content(self, response):
        item = JokejiItem()
        content = response.xpath("//*[@id='text110']/p/text()").extract()
        read = ""
        for i in content:
            i = i.replace("<p>", "").replace("<br>", "\n").replace("</p>", "\n")
            read += i

        select = re.compile(r"\d+、(.*?)\d+")
        select_get = select.findall(read)
        for sel in select_get:
            item["content"] = sel
            yield item

