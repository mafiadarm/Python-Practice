# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from m23sw_all.items import M23SwAllItem


class M23swRuleSpider(CrawlSpider):
    name = 'm23sw_rule'
    allowed_domains = ['m.23sw.net']
    start_urls = ['http://m.23sw.net/sort/1_1/']

    menu = LinkExtractor(allow=r'sort/\d+_\d+')  # http://m.23sw.net/sort/3_1/
    book = LinkExtractor(allow=r'xxs-\d+/')  # http://m.23sw.net/xxs-35353/
    page = LinkExtractor(allow=r'xxss-\d+-\d+/')  # http://m.23sw.net/xxss-35353-31882366/

    rules = (
        Rule(menu, follow=True),
        Rule(book, follow=True),
        Rule(page, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        """
        小说章节页的数据
        """
        # print(response.url)

        rr = re.compile(r"http://m.23sw.net/\w+-(\d+)-(\d+)/")
        number = rr.findall(response.url)[0]

        hh = re.compile(r".*?是(.*?)最新更新章节.*?")
        head = hh.findall(response.xpath("//*/title/text()").extract_first())[0]
        head = head.replace(">", "").replace("<", "").replace("'", "_")

        title = response.xpath('//*[@id="chaptertitle"]/text()').extract_first()
        title = title.replace("'", "_")

        context = response.xpath("//*[@id='novelcontent']/text()|//*[@id='novelcontent']/p/text()").extract()
        context_i = []
        for i in context:
            i = i.replace("&nbsp;", "").replace("WWW.23sw.net", "").replace("'", "_")
            context_i.append(i)
        content = "".join(context_i)

        item = M23SwAllItem()
        item["bookname"] = head  # 书名
        item["book_number"] = number[0]  # 书编号
        item["book_page_number"] = number[1]  # 章节编号
        item["title"] = title  # 章节名
        item["content"] = content  # 内容
        return item


