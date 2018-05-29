# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sqlite3
import datetime


class M23SwAllPipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect('fiction.db')
        self.corr = self.conn.cursor()
        self.corr.execute(
            """CREATE TABLE IF NOT EXISTS fictions (bookname text, book_number text, book_page_number text, title text, content text);"""
        )

    def process_item(self, item, spider):
        if spider.name == 'm23sw_rule':
            bookname = item.get("bookname")
            book_number = item.get("book_number")
            book_page_number = item.get("book_page_number")
            title = item.get("title")
            content = item.get("content")
            # print(content)
            self.corr.execute("INSERT INTO fictions VALUES ('{}','{}','{}','{}','{}');".format(bookname, book_number, book_page_number, title, content))

            return item

    def close_spider(self, spider):
        self.conn.commit()
        self.corr.close()
        self.conn.close()


class AreaPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'air':
            item["source"] = spider.name
            item["utctime"] = str(datetime.datetime.now())
            return item


class AreaJsonPipeline(object):
    def open_spider(self, spider):
        self.file = open("area.json", "w")

    def process_item(self, item, spider):
        if spider.name == 'air':
            content = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(content)
            return item

    def close_spider(self, spider):
        self.file.close()

