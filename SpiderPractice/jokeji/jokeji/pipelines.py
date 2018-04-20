# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class JokejiPipeline(object):
    def open_spider(self, start_requests):
        self.conn = sqlite3.connect('joker.db')
        self.corr = self.conn.cursor()
        self.corr.execute(
            """CREATE TABLE IF NOT EXISTS JOKES (content text);"""
        )

    def process_item(self, item, spider):
        content = item["content"]
        # print(content)
        self.corr.execute("INSERT INTO JOKES(content) VALUES ('{}');".format(content))
        self.conn.commit()
        return item

    def close_spider(self):
        self.corr.close()
        self.conn.close()
