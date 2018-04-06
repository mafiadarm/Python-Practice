# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZlzpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    money = scrapy.Field()
    release_date = scrapy.Field()
    experience = scrapy.Field()
    recruiting = scrapy.Field()
    workplace = scrapy.Field()
    job_nature = scrapy.Field()
    education = scrapy.Field()
    position = scrapy.Field()
    description_job = scrapy.Field()
    description_com = scrapy.Field()


