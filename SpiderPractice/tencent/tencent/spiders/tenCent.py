# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tenCent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        items = TencentItem()
        node_list = response.xpath("//*[@class='even']|//*[@class='odd']")
        if not node_list:
            return

        for node in node_list:
            items["name"] = node.xpath("./td[1]/a/text()").extract_first()  # extract_first 拿一条数据
            items["detailLink"] = node.xpath("./td[1]/a/@href").extract_first()
            items["positionInfo"] = node.xpath("./td[2]/text()").extract_first()
            items["peopleNumber"] = node.xpath("./td[3]/text()").extract_first()
            items["workLocation"] = node.xpath("./td[4]/text()").extract_first()
            items["publishTime"] = node.xpath("./td[5]/text()").extract_first()
            yield items

        url = response.xpath("//a[@id='next']/@href").extract_first()
        print("-"*50, url)

        yield scrapy.Request("https://hr.tencent.com/" + url, callback=self.parse)

