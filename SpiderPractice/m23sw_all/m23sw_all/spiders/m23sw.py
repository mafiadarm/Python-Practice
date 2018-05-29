# -*- coding: utf-8 -*-
import re

import scrapy
from m23sw_all.items import M23SwAllItem


class M23swSpider(scrapy.Spider):
    name = 'm23sw'
    allowed_domains = ['m.23sw.net']
    offset = 1
    start_urls = ['http://m.23sw.net/sort/1_1/']

    def parse(self, response):
        """
        书目录
        """
        book_url = response.xpath("//*[@class='content']/h6/a/@href").extract()
        book_url = [url.replace("xxs", "xxss") for url in book_url]
        end_flag = response.xpath("//*[@class='page']/a[last()-1]/text()").extract_first()  # 结束标记

        for url in book_url:
            yield scrapy.Request(url=url, callback=self.middle_page)

        # yield scrapy.Request(url="http://m.23sw.net/xxss-59784/", callback=self.middle_page)  # 单页测试
        print(f'http://m.23sw.net/sort/1_{self.offset}/', len(book_url))

        self.offset += 1
        if end_flag == "首页":
            return

        yield scrapy.Request(url=f'http://m.23sw.net/sort/1_{self.offset}/', callback=self.parse)

    def middle_page(self, response):
        """
        小说目录页
        """
        enter_url = response.xpath("//*[@class='chapters']/li/a/@href").extract()  # 每章节链接
        name = response.xpath("//*[@class='currency_head']/h1/a/text()").extract_first()  # 小说名

        next_page = response.xpath("//*[@class='page']/a[last()-1]/@href").extract_first()  # 下一页链接
        end_flag = response.xpath("//*[@class='page']/a[last()-1]/text()").extract_first()  # 结束标记
        # end_page = response.xpath("//*[@class='page']/a/@href").extract()[-1]  # 尾页链接

        print(name, next_page)

        for url in enter_url:  # 每章节下载
            item = M23SwAllItem()
            item["bookname"] = name
            yield scrapy.Request(url=url, callback=self.content, meta=item)

        if end_flag == "首页":
            return
        yield scrapy.Request(url='http://m.23sw.net'+next_page, callback=self.middle_page)  # 返回下一页目录

    def content(self, response):
        """
        小说章节页的数据
        """
        rr = re.compile(r"http://m.23sw.net/\w+-(\d+)-(\d+)/")
        number = rr.findall(response.url)[0]
        title = response.xpath('//*[@id="chaptertitle"]/text()').extract_first()
        context = response.xpath("//*[@id='novelcontent']/text()|//*[@id='novelcontent']/p/text()").extract()

        context_i = []
        for i in context:
            i = i.replace("&nbsp;", "").replace("WWW.23sw.net", "").replace(" ", "").replace("'", "")
            context_i.append(i)

        item = response.meta

        item["book_number"] = number[0]  # 书编号
        item["book_page_number"] = number[1]  # 章节编号
        item["title"] = title  # 章节名
        item["content"] = "".join(context)  # 内容
        return item
