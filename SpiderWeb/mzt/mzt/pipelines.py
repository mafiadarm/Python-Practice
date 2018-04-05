# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
from . import settings
import os


class MztPipeline(object):

    def process_item(self, item, spider):
        if 'image_urls' in item:

            dir_path = os.path.join(settings.IMAGES_STORE, item['name'][0])

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            for image_url in item['image_urls']:
                # 文件名
                us = image_url.split('/')[3:]
                image_file_name = '_'.join(us)
                # 文件路径
                file_path = os.path.join(dir_path, image_file_name)
                # 如果文件路径存在则跳过，避免重复
                if os.path.exists(file_path):
                    continue
                # 保存图片
                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, headers=settings.HEADERS, stream=True)
                    for block in response.iter_content(1024):
                        if not block:
                            break

                        handle.write(block)

        return item
