import itchat
import re
import jieba
from pandas import DataFrame
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)[0:]

# 初始化计数器
male = female = other = 0
# friends[0]是自己的信息，所以要从friends[1]开始
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# 计算朋友总数
total = len(friends[1:])
# 打印出自己的好友性别比例
print("男性好友： %.2f%%" % (float(male) / total * 100) + "\n" + "女性好友： %.2f%%" % (
        float(female) / total * 100) + "\n" + "不明性别好友： %.2f%%" % (float(other) / total * 100))

'''
再仔细观察friends列表，发现里面还包含了好友昵称、省份、城市、个人简介等等的数据，刚好可以用来分析好友城市分布，最好的方
式是定义一个函数把数据都爬下来，存到数据框里，再进行分析。
'''
# 定义一个函数，用来爬取各个变量
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


# 调用函数得到各变量，并把数据存到csv文件中，保存到桌面
NickName = get_var("NickName")
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')

# from pandas import DataFrame

data = {'NickName': NickName, 'Sex': Sex, 'Province': Province,
        'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('data.csv', index=True)

# import re
'''
先把原先爬下来的个性签名（Signature）打印出来，发现有很多本来是表情的，变成了emoji、span、class等等这些无关紧要的词，需
要先替换掉，另外，还有类似<>/= 之类的符号，也需要写个简单的正则替换掉，再把所有拼起来，得到text字串。
'''
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile(r"1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)

# import jieba

wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)


'''
可以根据自己想要的图片、形状、颜色画出相似的图形（在这里，我使用的是我的头像，当然，为了颜色可以更加鲜艳使最后画出的词云
图更加好看易辨，我先对自己的头像用PS做了一点小处理）。为此，我们需要把matplotlib、wordcloud、numpy、PIL等包搞进来。
'''
'''
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
'''

coloring = np.array(Image.open("C:/Users/lo/Desktop/wechat.jpg"))
my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=coloring, max_font_size=60, random_state=42, scale=2, font_path="C:/Program Files/Python36/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/cmtt10.ttf").generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

# 词频统计范例
'''
# -*- coding: utf-8 -*-
# coding=utf-8

import random
import collections
import string

#str1 = '赵钱孙李周吴郑王'
str1 = string.ascii_uppercase  # 大写 ABCDEFGHIJKLMNOPQRSTUVWXYZ
#str1 = string.ascii_lowercase # 小写 abcdefghijklmnopqrstuvwxyz
#str1 = string.ascii_letters   # 大写和小写 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
mylist = [random.choice(str1) for i in range(100)]
mycount = collections.Counter(mylist)
for key, val in mycount.most_common(10):  # 有序
    print(key, val)
'''