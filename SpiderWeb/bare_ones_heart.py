# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_16_2018  18:42
   File Name:      /GitHub/崩崩崩
   Creat From:     PyCharm
   Python version: 3.6.4
- - - - - - - - - - - - - - -
   Description:
   抓取微博主要文字内容，分析词语，组成图片
   使用库
   jieba
   matplotlib
   numpy  依赖关系matplotlib
   pyparsing 依赖关系matplotlib
   requests
   scipy
   wordcloud
==============================
"""
import codecs
import logging
import jieba
import jieba.posseg as pseg
import jieba.analyse
import matplotlib
import matplotlib.pyplot as plt
import numpy
import pyparsing
import requests
import scipy
from scipy.misc import imread
from wordcloud import WordCloud


__author__ = 'Loffew'


logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

# word = "这是一个什么时间呢？"
# words = jieba.cut(word, cut_all=True)  # 全模式切词
# print("/".join(words))
# words = jieba.cut(word, cut_all=False)  # 精确模式
# print("/".join(words))
# words = jieba.cut(word)  # 默认是精确模式
# print("/".join(words))
# words = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print("/".join(words))
# words = pseg.cut(word)
# for word, flag in words:
#     print(word, flag)
# words = jieba.lcut(word, cut_all=True)
# print(words)
# words = jieba.lcut_for_search(word)
# print(words)

# with open("tt.txt", "r") as ff:
#     word = ff.readlines()
# "".join(word)
# ss.replace("\n", "")
# ss.replace(" ", "")
# print(ss[:100])

# 英文的分割词云
# [word]从txt用readlines导出来就是这样
# word = ['SEASON I Winter\n', '"Now is the winter of my discontent."\n', '\n', 'I\n', '\n', 'I have not had charge of my garden very long; and I am not sure that I should have undertaken such a charge had there been anyone else to do it. But there was no one else, and it so obviously needed doing.\n', '\n', 'Of course there was the gardener—I shall have to allude to him occasionally—but just now I will only mention the fact that his greatest admirer could not have accused him of taking care of the garden.\n', '\n', 'Then there was his Reverence; he was by way of being in charge of everything, me included, I suppose, and of course nominally[Pg 4] it was so. He had the parish and the church, and the rectory and his family, and the men-servants and the maid-servants, a horse and a pony and the garden! He managed most things well, I will say, and the kitchen garden gave some account of itself, but in the flower garden desolation cried aloud.\n']
# word = "".join(word)
# 词云分析
# wordcloud = WordCloud(background_color="white", width=800, height=400, margin=2).generate(word)
# 词云图片构成
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()
# 保存为图片
# wordcloud.to_file("test.png")

# 中文分词成图片
data = []
with open("kk.txt", "r") as ff:  # codecs.open() 这个转码的没整懂
    for i in ff.readlines():
        getwords = jieba.analyse.extract_tags(i, topK=10)  # 取权重[topK]最大的10个词，返回列表，i默认encode="utf-8"，也可以手动添加
        data.extend(getwords)  # extend相当于把列表append()
    data = " ".join(data)  # 要留空格，分词才能识别
    mask_img = imread("fuka.png", flatten=True, mode="F")
    wordcloud = WordCloud(background_color="white", font_path="msyh.ttc", mask=mask_img).generate(data)  # font_path中文需要指定字体
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
# 保存为图片
wordcloud.to_file("test.png")