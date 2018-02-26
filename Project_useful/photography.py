# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_23_2018  16:34
   File Name:      /GitHub/photography
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

__author__ = 'Loffew'

import logging
from PIL import ImageColor
from PIL import Image

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

# 查看颜色代码
pp_dbg(ImageColor.getcolor("red", "RGBA"))  # ImageColor文件最后有colormap

# 打开已有的
catIm = Image.open("mengqi.jpg")
pp_dbg(catIm.size)
pp_dbg(catIm.filename)
pp_dbg(catIm.format_description)
catIm.save("mengqi.jpg")  # 可以重新命名保存

# 新建
im = Image.new("RGBA", (100, 100), "purple")  # 颜色可以不填，默认为黑色
im.save("purpleImage.png")

# 剪裁
croppedIm = catIm.crop((335, 345, 565, 560))
croppedIm.save("cropped.png")

# 复制
catIm = Image.open("mengqi.jpg")
catCopyIm = catIm.copy()

# 粘贴
faceIm = catIm.crop((335, 345, 565, 560))
pp_dbg(faceIm.size)
catCopyIm.paste(faceIm, (0, 0))
catCopyIm.paste(faceIm, (400, 500))
catCopyIm.save("pasted.png")

# 平铺
catImWidth, catImHeight = catIm.size
faceImWidth, faceImHeight = faceIm.size
catCopyTwo = catIm.copy()
for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))
catCopyTwo.save("tiled.png")

# 调整图像大小
width, height = catIm.size
quartersizedIm = catIm.resize((int(width/2), int(height/2)))
quartersizedIm.save("quartersized.png")
svelteIm = catIm.resize((width, height + 300))
svelteIm.save("svelte.png")

# 旋转
catIm.rotate(90).save("rotated90.png")
catIm.rotate(180).save("rotated180.png")
catIm.rotate(270).save("rotated270.png")

# 镜像反转
catIm.transpose(Image.FLIP_LEFT_RIGHT).save("horizontal_flip.png")
catIm.transpose(Image.FLIP_TOP_BOTTOM).save("vertical_flip.png")

# 更改单个像素
im = Image.new("RGBA", (100, 100))
im.getpixel((0, 0))
for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (210, 210, 210))

for i in range(100):
    for j in range(50, 100):
        im.putpixel((i, j), ImageColor.getcolor("darkgray", "RGBA"))

im.getpixel((0, 0))
im.getpixel((0, 50))
im.save("putPixel.png")