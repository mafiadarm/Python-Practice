#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           07_01_2018  16:31
  File Name:      /GitHub/character
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
  windows: pip install pillow  windows有问题
  linux:  需要在linux上实践
  sudo apt-get install tesseract-ocr
  sudo apt-get install libtesseract-dev

==============================
"""
from PIL import Image

__author__ = 'Loffew'


# image = Image.open("timg.jpg")
# image.show()
# im = image.convert("L")  # 灰度处理是R=G=B出来的一个彩色图像
# im.show()

# print(image.getbands())

# image = Image.new(("RGB"), (120, 120), "red")
# http://pillow.readthedocs.io/en/latest/handbook/concepts.html
# image = Image.new(("L"), (120, 120), "red")
# image.show()
# image.save("path.jpg")

# image = Image.open("timg.jpg")
# print(image.size)
# print(image.getpixel((120, 120)))  # 获取像素点的RGB  长，宽
# im = image.crop((0, 0, 100, 100))  # 切一个部分出来
# im.show()

# 二值化
def binarizing(img, threshold=127):  # 127这个中间值会比较合适
    """传入image对象进行灰度、二值处理"""
    img = img.convert("L")  # 转灰度
    pix_data = img.load()
    w, h = img.size  # 总的长宽
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            # 把像素点的值变成统一的一个值
            if pix_data[x, y] < threshold:  # pix_data[x, y]这个坐标的像素点的灰度值
                pix_data[x, y] = 0
            else:
                pix_data[x, y] = 255
    return img


# image = Image.open("timg.jpg")
# im = binarizing(image)
# im.show()


# 降噪
def depoint(img):
    """
        传入二值化后的图片进行降噪
        一个点黑周围全是白点，说明这就是噪点
        降噪为4邻域和8邻域，此例为4邻域
    """
    pix_data = img.load()
    w, h = img.size
    for y in range(1, h - 1):  # 去掉四个角
        for x in range(1, w - 1):
            count = 0
            # 245是阈值，自己做设定
            if pix_data[x, y - 1] > 245:  # 上
                count = count + 1
            if pix_data[x, y + 1] > 245:  # 下
                count = count + 1
            if pix_data[x - 1, y] > 245:  # 左
                count = count + 1
            if pix_data[x + 1, y] > 245:  # 右
                count = count + 1
            # 如果都是大于这个值的，count会=4，则这是一个噪点，就把它变成白色
            if count >= 3:
                pix_data[x, y] = 255
    return img


# im = depoint(im)
# im.show()

# 判断阈值
# 可以把所有像素的灰度值拿到以后，统计一下再做中间值的设定
# 或者直接分段，看每个段有多少

"""
    扩展pytesser3
    安装 pip install pytesser3
    下载tesseract.exe
    修改pytesser3包下面__init__文件内tesseract_exe_name的值为你的tesseract.exe的路径
    tesseract.log在error文件里面要改成with open("path", "a")
"""

# from pytesser3 import image_to_string
#
# image = Image.open("timg.jpg")
# image = binarizing(image)
# image = depoint(image)
# print(image_to_string(image))

# 生成验证码
import random
from PIL import ImageDraw, ImageFont


def rndchar():
    return chr(random.randint(55, 90))

def rndcolor():
    return random.randint(100, 175), random.randint(125, 200), random.randint(200, 255)

def tndcolor():
    return random.randint(25, 99), random.randint(10, 124), random.randint(40, 199)


width = 200
heith = 40
image = Image.new("RGB", (width, heith), (255, 255, 255))
font = ImageFont.truetype("arial.ttf", 30)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(heith):
        draw.point((x, y), fill=rndcolor())

for t in range(4):
    draw.text((50*t+13, 5), rndchar(), font=font, fill=tndcolor())

image.show()
