# -*- coding: utf-8 -*-
import scrapy
from area.items import AreaItem


class AreaSpiderSpider(scrapy.Spider):
    name = 'area_spider'
    allowed_domains = ['aqistudy.cn']
    base_url = 'https://www.aqistudy.cn/historydata/'
    start_urls = [base_url]

    def parse(self, response):
        print("正在爬取城市信息......")
        url_list = response.xpath("//div[@class='all']/div[@class='bottom']/ul/div[2]/li/a/@href").extract()
        city_list = response.xpath("//div[@class='all']/div[@class='bottom']/ul/div[2]/li/a/text()").extract()
        for Url, city in zip(url_list, city_list):
            url = self.base_url + Url
            # print(url, city)
            yield scrapy.Request(url=url, meta={"city": city}, callback=self.parse_month)

    def parse_month(self, response):
        print("正在爬取城市月份......")
        Url_list = response.xpath("//tbody/tr/td/a/@href").extract()
        for Url in Url_list:
            url = self.base_url + Url
            yield scrapy.Request(url=url, meta={"city": response.meta["city"]}, callback=self.parse_month)

    def parse_day(self, response):
        print("正在爬取最终数据......")
        item = AreaItem()
        node_list = response.xpath("//tr")

        node_list.pop(0)

        for node in node_list:
            item["date"] = node.xpath("./td[1]/text()").extract_first()
            item["city"] = response.meta["city"]
            item["aqi"] = node.xpath("./td[2]/text()").extract_first()
            item["level"] = node.xpath("./td[3]//text()").extract_first()
            item["pm2_5"] = node.xpath("./td[4]/text()").extract_first()
            item["pm10"] = node.xpath("./td[5]/text()").extract_first()
            item["so2"] = node.xpath("./td[6]/text()").extract_first()
            item["co"] = node.xpath("./td[7]/text()").extract_first()
            item["no2"] = node.xpath("./td[8]/text()").extract_first()
            item["o3"] = node.xpath("./td[9]/text()").extract_first()
