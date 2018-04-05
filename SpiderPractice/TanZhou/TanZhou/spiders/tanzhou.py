# -*- coding: utf-8 -*-
import scrapy
import time
from TanZhou.items import TanzhouItem


class TanzhouSpider(scrapy.Spider):
    """
    新建一个spider [scrapy genspider "tanzhou" tanzhoudu.com]
    """
    name = 'tanzhou'  # 唯一标示
    offset = 0
    base_url = "http://www.tanzhoudu.com/mall/course/initAllCourse?params.offset=" + str(offset) + \
               "&params.num=20&keyword=&_=" + str(int(time.time() * 1000))
    allowed_domains = ['tanzhoudu.com']  # 可选的取值范围，可有可无，只能在这个域名下面的才能被取值
    start_urls = [base_url]  # 可以为元组，可以为列表

    def parse(self, response):
        items = TanzhouItem()
        node_list = response.xpath("//div[@id='newCourse']/div/div/ul/li")
        for node in node_list:
            items["title"] = node.xpath("./a/@title").extract_first()
            items["money"] = node.xpath("./div/span/text()").extract_first()
            yield items  # 用yield返回给管道 pipelines
        self.offset += 20  # 自动翻页偏移量
        if not node_list:
            return
        yield scrapy.Request(url="http://www.tanzhoudu.com/mall/course/initAllCourse?params.offset=" + str(self.offset)
                                 + "&params.num=20&keyword=&_=" + str(int(time.time() * 1000)), callback=self.parse)  # 丢到调度器，入列

