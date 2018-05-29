# -*- coding: utf-8 -*-
import scrapy
from qianchengwuyou.items import QianchengwuyouItem


class QcSpider(scrapy.Spider):
    name = 'qc'
    allowed_domains = ['www.51job.com']
    base_url = "https://search.51job.com/list/090200,000000,0000,00,9,99,%2B,2,1.html?"
    start_urls = [base_url]

    def parse(self, response):
        node_list = response.xpath("//div/[@class='el']")  # 取节点
        for node in node_list:
            item = QianchengwuyouItem()
            item["work_name"] = node.xpath("./p/span/a/@title").extract_first()
            item["company"] = node.xpath("./span/a/@title").extract_first()
            item["work_position"] = node.xpath("./span[@class='t3']/text()").extract_first()
            item["salary"] = node.xpath("./span[@class='t4']/text()").extract_first()
            item["publishTime"] = node.xpath("./span[@class='t5']/text()").extract_first()

            detail_href = node.xpath("./p/span/a/@href").extract_first()
            if not detail_href:
                continue

            yield scrapy.Request(detail_href, callback=self.detail, meta={"item": item})

    def detail(self, response):
        item = response.meta["item"]
        content1 = response.xpath("//div[@class='bmsg job_msg inbox']/*/text()").extract()
        content2 = response.xpath("//div[@class='bmsg job_msg inbox']/*/*/text()").extract()
        if len(content1) > len(content2):
            item["content"] = "".join(content1)
        else:
            item["content"] = "".join(content2)

        item["content"] = "".join(response.xpath("div[@class='bmsg job_msg inbox']/p/text()").extract()).strip()
        yield item
