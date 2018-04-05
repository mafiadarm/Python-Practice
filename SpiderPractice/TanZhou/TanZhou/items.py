# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

"""
    第一步，明确目标，编写item
    创建一个项目
    在spider文件夹下， 创建爬虫文件：scrapy genspider “spider_name” “url”

"""
import scrapy


class TanzhouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 课程名称
    title = scrapy.Field()  # 调用的时候，这是键值对对象
    # 课程金额
    money = scrapy.Field()
