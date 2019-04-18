#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           04_16_2019  19:00
  File Name:      /Python-Practice/黑吧云点播
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging
import requests
import re
import os
from multiprocessing.dummy import Pool

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


# def pp_dbg(*args):
#     return logging.debug(*args)

def error_log(url, name):
    with open("error.log", "a", encoding="utf-8") as ww:
        content = f"{url} {name}\n"
        ww.write(content)

'''
http://tv.myhack58.com/?jk=http://www.vipjiexi.com/yun.php?url=&url=https://www.iqiyi.com/v_19rrnt8u2k.html?vfm=m_294_wgtv
先进第一层iframe，看到src= http://www.vipjiexi.com/yun.php?url=&url=https://www.iqiyi.com/v_19rrnt8u2k.html?vfm=m_294_wgtv
    访问这个url，看到跳转到 http://wq114.org:88/yun.php?url=&url=https://www.iqiyi.com/v_19rrnt8u2k.html?vfm=m_294_wgtv
    域名变了，说明有伪装，此处姑且认为wq114.org:88为可用域名，以省略获取伪装域名的这一步骤（可以手动测试获取）
    不过在拿src的时候，可以直接通过元素定位拿到，所以这个伪装可有可无

再查看元素，看到视频这层iframe的src=  /x3/tong.php?url=https://hot.jingpin88.com/20180312/he87L1IN/index.m3u8
    可看到结尾为m3u8，这个是视频格式，可用直接下载用的，那么拼接上可用url  [wq114.org:88]  再访问
    访问后，开始播放电影

查看元素（先点F12再访问url）没有iframe套层了，抓包信息也是直接开始缓存，说明成功

下载m3u8格式的文件，访问主url后会返回一张列表，拼接列表里面的url，逐个加载到文件即可
http://wq114.org:88/x3/tong.php?url=https://hot.jingpin88.com/20180312/he87L1IN/index.m3u8
实际上是返回一张列表
    #EXTM3U
    #EXT-X-VERSION:3
    #EXT-X-TARGETDURATION:14
    #EXT-X-MEDIA-SEQUENCE:0
    #EXTINF:11.32,
    /20180312/he87L1IN/1000kb/hls/9l10boat8477000.ts  需要拼接的部分
    ... ...

所以步骤即是：
    用 http://tv.myhack58.com/?jk=http://www.vipjiexi.com/yun.php?url=&url= 拼接视频地址
    进入第一层，再通过id定位，获取第二层iframe的src
    访问拼接的url，下载m3u8格式的视频
'''

class DownloadSrc:
    def __init__(self, movie_name):
        """
            从主站获取信息，所以CLOUD_URL定死，如果有变动，直接修改此处就行
        """
        # self.CLOUD_URL = "http://wq114.org:88/yun.php?url=&url="
        self.CLOUD_URL = "http://tv.myhack58.com/?jk=http://www.vipjiexi.com/yun.php?url=&url="
        self.pool = Pool()
        self.FILE_SAVE = f"E:\迅雷下载\{movie_name}"
        self.movie_name = movie_name
        self.headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }

        # self.check_path(self.FILE_SAVE)

    @staticmethod
    def check_path(path):
        if not os.path.exists(path):
            os.mkdir(path)

    @staticmethod
    def set_selenium():
        """
            设置selenium --> 使用Chrome浏览器
            创建selenium 对象
        :return:
        """
        opt = webdriver.ChromeOptions()  # 创建chrome参数对象

        prefs = {  # 设置flash自动开启，不然要手动去点，很悲剧
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
        }
        opt.add_experimental_option('prefs', prefs)
        selenium_diver = webdriver.Chrome(options=opt)  # 创建
        return selenium_diver

    def selenium_get_src(self, target_url, flag=None):
        """
            拼接url后，从iframe里面获取src信息，但是要首先进入第一层，再通过id去获取
            定位以后，因为iframe是一个单独的web属性，所以不需要遍历
            直接获取属性即可
        :param flag:
        :param target_url:
        :return:
        """
        iframe = self.set_selenium()
        iframe.get(self.CLOUD_URL + target_url)
        iframe.switch_to.frame(0)

        try:
            wait_flag = (By.ID, "player")  # 设置等待，不然取不到元素
            WebDriverWait(iframe, 20, 0.5).until(expected_conditions.presence_of_all_elements_located(wait_flag))

            if flag:
                iframe.switch_to.frame(0)
                time.sleep(5)
                src = iframe.find_element_by_xpath('//*[@class="dplayer-video dplayer-video-current"]')
            else:
                src = iframe.find_element_by_xpath(r'//*[@id="player"]')

            url = src.get_attribute("src")
            return url if url else None
        except Exception as ex:
            print(ex)
            error_log(target_url, self.movie_name)
        finally:
            iframe.quit()

    @staticmethod
    def m3u8_head(url):
        """
        :param url:m3u8 控制列表的链接
        :return:
        """
        headers = {
            'Referer': url,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'X-Requested-With': 'ShockwaveFlash/32.0.0.171',
        }
        return headers

    @staticmethod
    def get_m3u8_url(str_url):
        """
            传入的是一段str
            用正则获取域名和m3u8 的地址
        :param str_url:
        :return: 返回 m3u8地址 和 域名
        """
        index_rule = re.compile(r".*?url=(.*?\.m3u8)")
        domain_rule = re.compile(r".*?url=(.*?\.com/)")
        index_url = index_rule.findall(str_url)
        index_url = index_url[0] if index_url else None
        domain = domain_rule.findall(str_url)
        domain = domain[0] if domain else None
        return index_url, domain

    @staticmethod
    def get_m3u8_list(content):
        """
            获取列表后，是字符串信息，要从这些信息里面单独提取碎片下载地址
            传入m3u8 的链接列表信息，用正则取出
        :param content:
        :return: 返回这个列表
        """
        path_rule = re.compile(r"(/.*?\.ts)")
        ts_list = path_rule.findall(content)
        return ts_list

    def get_m3u8_index_list(self, url):
        """
            传入iframe里面的src，访问这个url 会获取到m3u8 的真实地址
            从这个真实地址获取m3u8 的切片列表
            提取后，拼接并用线程下载，保存到指定位置
        :param url: 从iframe 获取 src
        :return:
        """
        if not url: return
        print(url)

        session = requests.session()
        header = self.m3u8_head(url)
        m3u8_url, domain = self.get_m3u8_url(url)

        if not m3u8_url or not domain:
            print("Can not find anything!")
            return

        m3u8_index = session.get(m3u8_url, headers=header)
        real_path = m3u8_index.content.decode().split("\n")[2]
        movie_list_url = domain + real_path

        m3u8_list = session.get(movie_list_url, headers=header)
        ts_list = self.get_m3u8_list(m3u8_list.content.decode())

        name = 0
        for ts in ts_list:
            ts_url = domain + ts
            # name = ts.split("/")[-1]
            name += 1
            self.pool.apply_async(self.save_file, args=("%05d.ts" %name, ts_url, session, header, True))

    def save_file(self, name, url, header, flag=None):
        """
            保存m3u8 为 mp4 格式文件
        :param flag:
        :param name:
        :param url:
        :param header:
        :return:
        """
        if not name or not url:
            return

        file = f"{self.FILE_SAVE}\{name}" if flag else f"{self.FILE_SAVE}.mp4"
        with open(file, "wb") as ww:
            stream = requests.get(url, stream=True, timeout=10, headers=header)

            for block in stream.iter_content(1024):  # 分段写入
                if not block:
                    break
                ww.write(block)

    def merge_and_delete(self):
        """
            合并ts文件为mp4文件
            删除ts文件
            删除文件夹
        :return:
        """
        merge = f"copy /d {self.FILE_SAVE}\* {self.FILE_SAVE}.mp4"
        os.system(merge)
        delete_ts = f"del /Q {self.FILE_SAVE}"
        os.system(delete_ts)
        delete_folder = f"rd {self.FILE_SAVE}"
        os.system(delete_folder)


def main_small(movie, movie_name):
    """
        启动实例
        获取src
        下载m3u8
        守护线程
        删除.ts文件
    :return:
    """
    src = DownloadSrc(movie_name)
    movie_url = src.selenium_get_src(movie)
    print(f"MOVIE_URL is {movie_url}")
    src.save_file(movie_name, movie_url, src.headers)

def main_big(movie, movie_name):
    src = DownloadSrc(movie_name)
    movie_url = src.selenium_get_src(movie)
    print(f"MOVIE_URL is {movie_url}")

    src.get_m3u8_index_list(movie_url)
    src.pool.close()
    src.pool.join()
    src.merge_and_delete()


if __name__ == '__main__':
    main_small("小猪配齐", "https://www.iqiyi.com/v_19rrl6d4as.html")
    # cmd --> copy /d *.ts <filename>.mp4
    # pass


    