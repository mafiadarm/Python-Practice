# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

import requests
from multiprocessing.dummy import Pool


class MztGet(object):
    """
    所有文件放在一个文件夹内
    """
    def __init__(self):
        self.conn = sqlite3.connect('meizitu.db')
        self.corr = self.conn.cursor()

    def close(self):
        self.corr.close()
        self.conn.close()

    def to_get(self):
        # self.corr.execute("select count(*) from MZT")  # 获取总行数
        self.corr.execute("select * from MZT")
        read = self.corr.fetchall()
        # print(read)
        # return
        self.queue_image(read)

    def queue_image(self, read):
        for page in read:
            image_file_name, image_url = page
            # pool.apply_async(self.save_img, args=(image_file_name, image_url,))
            self.save_img(image_file_name, image_url)

    def del_aready(self, image_file_name):
        self.corr.execute("DELETE FROM MZT WHERE name=?", (image_file_name,))
        self.conn.commit()
        print(image_file_name, "delete")

    def save_img(self, name, url):
        try:
            response = requests.get(url, headers=HEADERS, stream=True, timeout=10)
        except requests.ConnectionError:  # requests.ConnectTimeout被包含在里面
            print("图片无法下载")
            return
        except requests.exceptions.ReadTimeout:
            print("超时")
            return

        old_name = name
        name = name.replace("*", "").replace("?", "").replace("|", "")

        try:
            # 保存图片
            with open(name, 'wb') as handle:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
            print(name, "is ok")
            self.del_aready(old_name)
        except OSError:
            print("OSError", name, url)
            pass


if __name__ == '__main__':
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8",
    }

    pool = Pool()

    ww = MztGet()
    ww.to_get()
    ww.close()

    pool.close()
    pool.join()



