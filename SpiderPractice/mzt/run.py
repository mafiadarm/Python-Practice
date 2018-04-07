#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           04_07_2018  18:01
  File Name:      /SpiderPractice/run
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  替换在cmd里面输入scrapy crawl project_name
  运行这个文件就行，多个spider可以同时启用，但仅限在一个项目里面
==============================
"""

from mzt.spiders.meizitu import MeizituSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


__author__ = 'Loffew'


setting = get_project_settings()
process = CrawlerProcess(settings=setting)

process.crawl(MeizituSpider)
# process.crawl(Other)

process.start()
