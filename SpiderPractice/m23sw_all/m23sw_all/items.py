# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class M23SwAllItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookname = scrapy.Field()
    book_number = scrapy.Field()
    book_page_number = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()


class ChinaareaItem(scrapy.Item):
    city = scrapy.Field()  # 城市
    date = scrapy.Field()  # 日期
    aqi = scrapy.Field()  # 空气质量指数
    level = scrapy.Field()  # 空气质量等级
    pm25 = scrapy.Field()  # PM2.5
    pm10 = scrapy.Field()  # PM10
    so2 = scrapy.Field()    # 二氧化硫
    co = scrapy.Field()  # 一氧化碳
    no2 = scrapy.Field()  # 二氧化氮
    o3 = scrapy.Field()  # 臭氧
    source = scrapy.Field()  # 数据源
    utctime = scrapy.Field()  # 时间