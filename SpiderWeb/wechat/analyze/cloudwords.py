#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           04_28_2018  9:51
    File Name:      /wechat/cloudwords
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""


import logging
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy
from analyze.PATH_SETTING import *

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def make_picture(word_list, name):
    data = []
    for word in word_list:
        getwords = jieba.analyse.extract_tags(word, topK=10)  # 取权重[topK]最大的10个词，返回列表，i默认encode="utf-8"，也可以手动添加
        # print(getwords)
        data.extend(getwords)  # extend相当于把列表append()

    data = " ".join(data)  # 要留空格，分词才能识别

    # 自定义背景图
    background = Image.open(r"img_face.jpg")
    graph = numpy.array(background)

    # 产生词云图
    wordcloud = WordCloud(
        background_color="white",
        font_path="msyh.ttc",
        max_font_size=50,
        mask=graph,
    ).generate(data)  # font_path中文需要指定字体

    # 绘制颜色以背景图颜色为参考
    colors = ImageColorGenerator(graph, default_color=(0, 0, 0))
    wordcloud.recolor(color_func=colors)
    wordcloud.to_file(f"{CLOUDWORDS}{name}.png")

    # 直接显示图片
    # plt.figure("cc")
    # plt.imshow(wordcloud)
    # plt.axis("off")
    # plt.show()



