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
            request = scrapy.Request(link, callback=self.parse_item)
            yield request  # 返回请求

        # 获取 下一页 的link 实现翻页
        next_page = sel.xpath("//*[@id='wp_page_numbers']/ul/li/a[contains(text(),'下一页')]/@href").extract_first()
        print(next_page)

        if not next_page:
            return

        next_page = next_page.replace('/a/', '')  # 图片连接=page_link（a替换成空）处理首页
        print('pages: %s' % next_page)  # 打印页码

        request = scrapy.Request('http://www.meizitu.com/a/' + next_page, callback=self.parse)
        yield request  # 返回请求

    def parse_item(self, response):
        # 用ItemLoader载入MeizituItem()
        ll = ItemLoader(item=MztItem(), response=response)
        # 名字
        ll.add_xpath('name', '//h2/a/text()')
        # 标签  //*[@id="maincontent"]/div[1]/div[1]/p
        ll.add_xpath('tags', "//div[@id='maincontent']/div[@class='postmeta  clearfix']/div[@class='metaRight']/p/text()")
        # 图片连接 //*[@id="picture"]/p/img[1]
        ll.add_xpath('image_urls', "//div[@id='picture']/p/img/@src", Identity())
        # url
        ll.add_value('url', response.url)
        # 返回的值到pipelines进行处理
        return ll.load_item()
