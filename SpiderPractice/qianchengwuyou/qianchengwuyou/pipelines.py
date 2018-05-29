# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime

import pymongo as pymongo
import pymysql


class QianchengwuyouPipeline(object):
    def process_item(self, item, spider):
        item["source"] = spider.name
        item["utc_time"] = str(datetime.utcnow())

        return item

class QianchengwuyouJsonPipeline:
    def open_spider(self, spider):
        self.file = open("q51.json", "a", encoding="utf-8")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()

class QcMongoPipeline:
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host="localhost", port=27017)
        self.collction = self.client["qc"]["qc"]
    def process_item(self, item, spider):
        self.collction.insert(dict(item))
        return item
    def close_spider(self, spider):
        self.client.close()


class QcMongoPipeline:
    def open_spider(self, spider):
        self.con = pymysql.connect(host="localhost", port=3306, database="qiancheng", user="root", password="", charset="utf8")
        self.cur = self.con.cursor()
    def process_item(self, item, spider):
        sql = ("insert into qiancheng (source, utcTime, workName, company, workPosition, salary, publishTime, content, contact) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, )")
        list_item = [item["source"], item["utc_time"], item["work_name"], item["company"], item["work_position"], item["salary"], item["publishTime"], item["content"], item["contact"], ]
        self.cur.execute(sql, list_item)
        self.con.commit()
        return item
    def close_spider(self, spider):
        self.cur.close()
        self.con.close()