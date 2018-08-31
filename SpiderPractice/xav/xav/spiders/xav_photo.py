# -*- coding: utf-8 -*-
import re

import os
import requests
import scrapy
from multiprocessing.dummy import Pool
from xav import settings
from xav.items import XavItem


class XavPhotoSpider(scrapy.Spider):
    name = 'xav_photo'
    allowed_domains = ['2018x.men']
    base_url = 'http://2018x.men/'
    start_urls = [base_url]

    def parse(self, response):
        urls = response.xpath('//*[@id="category_8"]//dt/a/@href').extract()  # 列表中只拿第一个链接
        for url in urls:
            yield scrapy.Request(url=self.base_url + url, callback=self.page)

    def page(self, response):
        tail = "extra=page%3D1"
        regx = re.compile(r"forum.php\?mod=viewthread&tid=\d+")
        urls = regx.findall(response.text)
        for url in urls:
            url_to = self.base_url + url + tail
            yield scrapy.Request(url_to, callback=self.photo_url)

        next_page = response.xpath('//*[@class="nxt"]/@href').extract_first()
        if not next_page:
            return

        yield scrapy.Request(self.base_url + next_page, callback=self.page)

    def photo_url(self, response):
        check_all = response.xpath('//*[@class="page-all"]/@href').extract_first()
        if check_all:
            yield scrapy.Request(self.base_url + check_all, callback=self.photo_url)
        else:
            # pool = Pool()
            title = response.xpath('//*[@id="thread_subject"]/text()').extract_first()
            srcs = response.xpath('//*[@class="zoom"]/@src').extract()

            # if not os.path.exists(save_path):
            #     os.makedirs(save_path)

            save_path = "E:/photo/" + title.replace("'", "").replace('"', '') + "/"
            for src in srcs:
                item = XavItem()
                item["file"] = save_path + src.split("/")[-1]
                item["url"] = src
                yield item
                # pool.apply_async(self.save_image, args=(src, title))
            # pool.close()
            # pool.join()

    # def save_image(self, url, name):
    #     save_path = "E:/photo/" + name + "/"
    #     if not os.path.exists(save_path):
    #         os.makedirs(save_path)
    #
    #     image_file_name = save_path + url.split("/")[-1]
    #     with open(image_file_name, 'wb') as handle:
    #         response = requests.get(url, headers=settings.HEADERS, stream=True)
    #         for block in response.iter_content(1024):
    #             if not block:
    #                 break
    #             handle.write(block)

