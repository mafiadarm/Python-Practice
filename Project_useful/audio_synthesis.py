#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           07_02_2018  9:09
    File Name:      /GitHub/audio_synthesis
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
==============================
"""
from pydub import AudioSegment

__author__ = 'Loffew'

enPath = "C:\\Users\\lo\\Desktop\\fff\\西谷非学员群_森林_180702-072427.mp3"
cnPath = "C:\\Users\\lo\\Desktop\\fff\\西谷非学员群_森林_180702-072512.mp3"
targetPath = "C:\\Users\\lo\\Desktop\\fff\\result.mp3" #合并文件的路径
#加载MP3文件
song1 = AudioSegment.from_mp3(enPath)
song2 = AudioSegment.from_mp3(cnPath)
#取得两个MP3文件的声音分贝
db1 = song1.dBFS
db2 = song2.dBFS
song1 = song1[300:] #从300ms开始截取英文MP3
#调整两个MP3的声音大小，防止出现一个声音大一个声音小的情况
dbplus = db1 - db2
if dbplus < 0: # song1的声音更小
    song1+=abs(dbplus)
elif dbplus > 0: #song2的声音更小
    song2+=abs(dbplus)
#拼接两个音频文件
song = song1 + song2
#导出音频文件
song.export(targetPath, format="mp3") #导出为MP3格式