#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           09_24_2018  21:52
  File Name:      /Practice/data_view
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
==============================
"""
import logging

import pandas
import numpy
import matplotlib.pyplot as plt
import matplotlib
from pyecharts import Geo, Style, Bar, Overlap
from wordcloud import WordCloud, ImageColorGenerator
from os import path
from pylab import mpl
import jieba

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)

__author__ = 'Loffew'


def pp_dbg(*args):
    return logging.debug(*args)


def look_around():
    """
    数据预览
    :return:
    """
    moon = open(r"月饼好不好吃.txt", encoding="utf-8")
    cake = pandas.read_csv(moon, sep=",", names=["title", "price", "sales", "location"])
    # print(cake.describe())
    return cake


def character_view_picture(data):
    # backgroud_Image = plt.imread('1.jpg')  # 有背景就用，没背景就不用
    picture = WordCloud(
        # mask=backgroud_Image,
        width=1024, height=768,
        background_color='white',
        font_path="C:\simhei.ttf",
        max_font_size=400,
        random_state=50
    )
    picture = picture.fit_words({x[0]: x[1] for x in data.head(100).values})
    plt.imshow(picture, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    base_path = path.dirname(__file__)
    picture.to_file(path.join(base_path, "yuebing.png"))


def character_data():
    """
    数据分析可视化_数据
    :return:
    """
    moon = open(r"月饼好不好吃.txt", encoding="utf-8")
    cake = pandas.read_csv(moon, sep=",", names=["title", "price", "sales", "location"])
    title = cake.title.values.tolist()  # 把title变成列表
    # print(title)

    # 对每个标题进行分词
    title_s = []

    for line in title:
        cut = jieba.lcut(line)
        title_s.extend(cut)

    # 停用词表
    stopwords = ["月饼", "礼品", "口味", "礼盒", "包邮", "【", "】", "送礼", "大",
                 "中秋节", "中秋月饼", "2", "饼", "蓉", "多", "个", "味", "斤", "送", " ", "老",
                 "北京", "云南", "网红老", "中秋"]

    # 剔除停用词表
    while set(title_s) & set(stopwords):
        for word in title_s:
            if word in stopwords:
                title_s.remove(word)

    # 进行去重
    # words_set = list(set(title_s))

    # 对词语进行汇总统计
    words = pandas.DataFrame({'allwords': title_s})
    word_count = words.allwords.value_counts().reset_index()
    word_count.columns = ['word', 'count']

    return cake, title, word_count


def histogram(title, attr_list, value_list):
    bar = Bar(title)
    bar.add("关键词", attr_list, value_list, is_stack=True, xaxis_rotate=30, yaxix_min=4.2,
            xaxis_interval=0, is_splitline_show=False)
    overlap = Overlap()
    overlap.add(bar)
    overlap.render(f'{title}.html')


def character_view_sales():
    """
    关键词word对应的sales之和的统计分析
    :return:
    """
    word_conut = []
    for word in word_data.word:  # data.word的排列是从高到低的，所以结果也是从高到底的
        i, sal = 0, 0
        for tit in title_data:  # 遍历title，有就增加一份
            if word in tit:
                sal += form_data.sales[i]
        word_conut.append(sal)

    histogram("月饼关键词销量分布图", word_data.word[:30], word_conut[:30])


def interval_price_view():
    moon = look_around()
    # print(moon.sort_values(by='price'))
    price_info = moon[['price', 'location']]
    bins = [0, 10, 50, 100, 150, 200, 300, 500, 1000, 5000, 8000]
    level = ['0-10', '10-50', '50-100', '100-150', '150-200', '200-500', '500-1000', '1000-5000', '5000-8000', '8000以上']
    price_stage = pandas.cut(price_info['price'], bins=bins, labels=level).value_counts().sort_index()
    # print(price_stage)

    histogram("价格区间&月饼种类数量分布", price_stage.index, price_stage.values)


def interval_sales_view():
    moon = look_around()
    # print(moon.sort_values(by='sales'))
    sales_info = moon[['sales', 'location']]
    bins = [0, 500, 1000, 3000, 5000, 10000, 30000, 50000, 100000, 200000, 300000]
    level = ['0-500', '500-1000', '1000-3000', '3000-5000', '5000-10000', '10000-30000', '30000-50000', '50000-100000',
             '100000-200000', '200000以上']
    sales_stage = pandas.cut(sales_info['sales'], bins=bins, labels=level).value_counts().sort_index()
    # print(sales_stage)

    histogram("销售区间&月饼种类数量分布", sales_stage.index, sales_stage.values)


if __name__ == '__main__':
    form_data, title_data, word_data = character_data()
    # print(word_data)
    character_view_picture(word_data)
    character_view_sales()
    interval_price_view()
    interval_sales_view()
