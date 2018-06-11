---
一些简单的爬虫
---

# SpiderWeb

#### oracle_test

给oracle做DNS测试，在我们自己的服务器上增加DNS，在条件转发器上增加

cbsw.fs.ap1.oraclecloud.com

​		203.198.7.66

​		202.45.84.59

​		202.45.84.58

cbsw-test.fs.ap1.oraclecloud.com

​		同上

oraclecloud.com

​		同上

挂在本地，看是否能成功获取香港地址

#### QQchat

用qqbot挂qq，根据对话内容返回信息，粗糙的爬了一个笑话网站，sqlite存着

24内必掉一次，必须手动启，放弃

#### wechat

用wxpy挂微信，把信息记录到文档，图片、音频、视频、表情等放到指定的文件夹

analyze文件夹内可以把文档导入到sqlite，jieba词云分析

#### beng3

爬取崩坏3官网的人物背景大图，requests，加user-agent

#### douban

爬取豆瓣网电影信息，requests，随机user-agent

#### tencent_hr

爬取腾讯招聘，requests，造header，随机user-agent

#### Tencent_hr_auto_page

相对tencent_hr增加一个自动翻页功能

#### zhilianzhaopin

爬取智联招聘指定职位，含区域，写入excel，造header，url+paras

#### zhilianzhaopin_threading

多线程爬取智联招聘，每秒近2000

#### 王者荣耀道具和铭文 王者荣耀皮肤

爬取王者荣耀的相关信息，初期练手