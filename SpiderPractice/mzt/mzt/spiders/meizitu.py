# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.loader import ItemLoader, Identity
from ..items import MztItem


class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['meizitu.com']
    start_urls = [
        'http://www.meizitu.com/'
    ]

    def parse(self, response):
        sel = Selector(response)
        # 获取link
        for link in sel.xpath('//*[@class="wp-item"]/div/div/a/@href').extract():
            # 获取到的二级连接传送给self.parse_item
            yield scrapy.Request(link, callback=self.parse_item)  # 返回请求

        # 获取 下一页 的link 实现翻页
        next_page = sel.xpath("//*[@id='wp_page_numbers']/ul/li/a[contains(text(),'下一页')]/@href").extract_first()

        if not next_page:
            return

        next_page = next_page.replace('/a/', '')  # 图片连接=page_link（a替换成空）处理首页
        print("-" * 10, "THE NEXT PAGE IS: ", next_page)

        yield scrapy.Request('http://www.meizitu.com/a/' + next_page, callback=self.parse)  # 返回请求

    def parse_item(self, response):
        ll = MztItem()
        ll["name"] = response.xpath('//h2/a/text()').extract_first()
        ll["tags"] = response.xpath("//div[@id='maincontent']/div/div[@class='metaRight']/p/text()").extract_first()
        ll["url"] = response.url
        ll["image_urls"] = response.xpath("//div[@id='picture']/p/img/@src").extract()
        yield ll

        # 用ItemLoader载入MeizituItem()
        # ll = ItemLoader(item=MztItem(), response=response)
        # for img in imgs:
        #     # 名字
        #     ll.add_xpath('name', '//h2/a/text()')
        #     # 标签  //*[@id="maincontent"]/div[1]/div[1]/p
        #     ll.add_xpath('tags', "//div[@id='maincontent']/div/div[@class='metaRight']/p/text()")
        #     # 图片连接 //*[@id="picture"]/p/img[1]
        #     ll.add_xpath('image_urls', img, Identity())
        #     # url
        #     ll.add_value('url', response.url)
        #     # 返回的值到pipelines进行处理
        #     return ll.load_item()
