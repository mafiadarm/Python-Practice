# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

import requests
from . import settings
import os


class MztPipeline(object):
    """
    所有文件放在一个文件夹内
    """
    def open_spider(self, start_requests):
        self.conn = sqlite3.connect('meizitu.db')
        self.corr = self.conn.cursor()
        self.corr.execute(
            """CREATE TABLE IF NOT EXISTS MZT (name text, url text);"""
        )

    def process_item(self, item, spider):
        if 'image_urls' in item:

            if not os.path.exists(settings.IMAGES_STORE):
                os.makedirs(settings.IMAGES_STORE)

            for image_url in item['image_urls']:
                # 构建文件路径
                us = image_url.split('/')[5:]
                image_file_name = os.path.join(settings.IMAGES_STORE, item['name']) + '_'.join(us)
                # 如果文件路径存在则跳过，避免重复
                if os.path.exists(image_file_name):
                    continue
                # 保存图片
                # with open(image_file_name, 'wb') as handle:
                #     response = requests.get(image_url, headers=settings.HEADERS, stream=True)
                #     for block in response.iter_content(1024):
                #         if not block:
                #             break
                #         handle.write(block)

                self.corr.execute("INSERT INTO MZT(name, url) VALUES ('{}', '{}');".format(image_file_name, image_url))
        self.conn.commit()
        return item

    def close_spider(self):
        self.corr.close()
        self.conn.close()



