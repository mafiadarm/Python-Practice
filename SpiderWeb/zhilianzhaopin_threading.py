# -*- coding: utf-8 -*-
"""
==============================
   Date:           02_23_2018  10:00
   File Name:      /GitHub/zhilianzhaopin
   Creat From:     PyCharm
   Python version: 3.6.2
- - - - - - - - - - - - - - - 
   Description:
   1 用线程池抓取信息
   2 获取智联招聘的职位信息，默认是30天内[可调节]
   3 表格抬头：职位网址，职位名称，反馈率，公司网址，公司名称，最低薪，最高薪，地点，公司性质，公司规模，学历

   主流程：
   get_one_page     获取网页，返回text
   parse_one_page   解析text
   finally_list     清洗数据，加入infoList
==============================
"""

import logging
import re
import requests
from urllib.parse import urlencode
from multiprocessing.dummy import Pool
import time
from requests.exceptions import RequestException
import xlsxwriter
import os

__author__ = 'Loffew'

# logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]
#
#
# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


def head_get():
    return {  # 用COMMON.CopyAndFormat洗好格式
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/63.0.3239.132Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }


def paras_get(city, keyword, page, sg=None):
    """
    'sf': 最低工资
    'st': 最高工资 发布时间
    'sm': 0,  # 页面展示方式 0是隐藏详细内容 1是全部展示
    'isadv': 0,  # 页面展示方式 0隐藏选项 1展示选项
    'isfilter': 1,  # 如果要加pd 此项必要
    'pd': 30,  # 发布时间: -1 不限 1 今天 3 最近3天 7 最近一周 30 最近一月
    :param city: 城市
    :param keyword: 关键字
    :param page: 页数
    :param sg: MD5
    :return: paras
    """
    # paras 构造查询内容
    if not sg:
        return {
            'jl': city,
            'kw': keyword,
            'p': page,
        }
    else: return {
        'jl': city,
        'kw': keyword,
        'sg': sg,
        'p': page,
    }


def get_one_page(city, keyword, page, sg=None):
    """
    获取网页html内容并返回
    response 可以不加头也可以过，有了verify就可以认证成功，不会报错了
    response.close() 访问后关闭，防止长时间连接
    :param city: 城市
    :param keyword: 关键字
    :param page: 页数
    :param sg: MD5
    :return:
    """
    header = head_get()
    paras = paras_get(city, keyword, page, sg)
    www = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
    url = www + urlencode(paras)

    try:
        # 获取网页内容，返回html数据
        response = requests.get(url, verify=True, headers=header, timeout=500)
        # 通过状态码判断是否获取成功
        if response.status_code == 200:
            text = response.text
            response.close()
            return text
        else: get_one_page(city, keyword, page, sg)
    except RequestException as e:
        print(e)


def particular(items):
    """
    再次清洗详细项目
    :param items: 关于岗位的详细信息
    :return: 清洗后的列表
    """
    regx_5 = re.compile(r'<span>(.*?)</span>')
    rr = regx_5.findall(items)

    p_dic = {}
    for ob in rr:
        ff = ob.split("：")
        p_dic[ff[0]] = ff[1]

    add = p_dic.get('地点', "")
    if "-" in add:
        add_a, add_b = add.split("-")
    else: add_a, add_b = [add, ""]

    return [add_a, add_b,
            p_dic.get('公司性质', ""),
            p_dic.get('公司规模', ""),
            p_dic.get('经验', ""),
            p_dic.get('学历', ""),
            ]  # p_dic.get('职位月薪', "") 因为前面有了，这里就不要了


def money(item):
    """
    分开最高薪和最低新
    :param item: 薪金的项
    :return: list[min, max]
    """
    if "-" in item:
        return item.split("-")
    elif "元以下" in item:
        mon = item.split("元以下")
        return [0, mon[0]]
    elif "元以上" in item:
        mon = item.split("元以上")
        return [mon[0], mon[0]*10]
    else: return ["面议", "面议"]


def finally_list(items):
    """
    处理单页上已经获得的数据，添加到infoList
    :param items: 用正则抓取的内容
    :return: None
    """
    global infoList
    www = "http://jobs.zhaopin.com/"
    for item in items:
        job_name = item[1]
        job_name = job_name.replace('<b>', '')
        job_name = job_name.replace('</b>', '')  # 清洗name

        mon = money(item[5])  # 拆分出最高月薪和最低月薪

        # 职位网址，job_name职位名称， item[6]反馈率，item[2]公司网址，item[3]公司名称，mm[0]最低薪，mm[1]最高薪
        ll = [www + item[0] + ".htm", job_name, item[2], item[3], item[4], mon[0], mon[1]]
        # item[5]地点，公司性质，公司规模，学历
        par = particular(item[6])  # 最后这部分再次清洗处理，返回列表
        ll.extend(par)  # 增加到最终列表里面
        infoList.add(tuple(ll))


def parse_one_page(html):
    """
    解析HTML代码，提取从get_one_page获取的text信息
    :param html: 整个网页string
    :return: 正则匹配
    """
    # 正则表达式进行解析
    regx = re.compile(
        r'<a style=.*? href="http://jobs.zhaopin.com/(.*?)\.htm" target="_blank">(.*?)</a>.*?'  # 匹配职位介绍的链接、职位信息
        r'<td style=.*?<span>(.*?)</span>.*?'  # 反馈率
        r'<td class="gsmc"><a href="(.*?)" target="_blank">(.*?)</a>.*?'  # 匹配公司网址和公司名称
        r'<td class="zwyx">(.*?)</td>.*?'  # 匹配月薪
        r'.*?<li class="newlist_deatil_two">(.*?)<li class="newlist_deatil_last">.*?',  # 招聘的详细信息： 地点 公司性质 公司规模 经验 学历 职位月薪
        re.S)

    # 返回匹配所有符合条件的内容
    return regx.findall(html)


def all_cities():
    """
    所有省的信息及版面展示的国家信息
    :return: dict
    """
    return {
        548: '广东', 546: '湖北', 556: '陕西', 552: '四川', 535: '辽宁', 536: '吉林', 539: '江苏', 544: '山东', 540: '浙江', 549: '广西',
        541: '安徽', 532: '河北', 533: '山西', 534: '内蒙', 537: '黑龙江', 542: '福建', 543: '江西', 545: '河南', 547: '湖南', 550: '海南',
        553: '贵州', 554: '云南', 555: '西藏', 557: '甘肃', 558: '青海', 559: '宁夏', 560: '新疆', 530: '北京', 538: '上海', 531: '天津',
        551: '重庆', 561: '香港', 562: '澳门', 563: '台湾省', 481: '阿根廷', 482: '澳大利亚', 483: '奥地利', 484: '白俄罗斯', 485: '比利时',
        486: '巴西', 487: '保加利亚', 488: '加拿大', 490: '塞浦路斯', 491: '捷克', 492: '丹麦', 493: '埃及', 494: '芬兰', 495: '法国',
        496: '德国', 497: '希腊', 498: '匈牙利', 499: '冰岛', 500: '印度', 501: '印度尼西亚', 502: '爱尔兰', 503: '以色列', 504: '意大利',
        505: '日本', 506: '韩国', 507: '科威特', 508: '马来西亚', 509: '荷兰', 510: '新西兰', 511: '挪威', 513: '巴基斯坦', 514: '波兰',
        515: '葡萄牙', 516: '俄罗斯联邦', 517: '沙特阿拉伯', 518: '新加坡', 519: '南非', 520: '西班牙', 521: '瑞典', 522: '瑞士', 523: '泰国',
        524: '土耳其', 525: '乌克兰', 526: '阿联酋', 527: '英国', 528: '美国', 529: '越南', 913: '安哥拉', 914: '加纳', 915: '尼日利亚',
        916: '坦桑尼亚', 917: '乌干达', 918: '阿尔及利亚', 919: '塞内加尔', 930: '柬埔寨', 512: '其他'
    }


def city_get(city):
    """
    根据值返回包含对应城市信息的列表
    :param city: 一个或多个城市及国家，如果是 all 则单独处理
    :return: list
    """
    if city == "all": return [k for j, k in all_cities().items() if 530 <= j <= 563]
    else: return city.split(",")


def page_MD5_get(html):
    """
    获取搜索的信息一共有多少页
    :param html:
    :return:
    """
    regx = re.compile(r'<button type="button" class="nextpagego-btn" .*?,(.*?),\'\',\'(.*?)\'\)"></button>')
    try:
        page, MD5 = regx.findall(html)[0]
    except IndexError:
        page, MD5 = 1, None
    return int(page), MD5


def page_MD5_add(city, position):
    """
    把页数和MD5信息加到列表，等待调用
    :param city:
    :param position:
    :return: None
    """
    global parasList
    ss = get_one_page(city, position, 1)
    page, MD5 = page_MD5_get(ss)
    for pp in range(page):
        parasList.add((city, position, pp+1, MD5))


def main_cache(city, keyword, page, sg):
    """
    提取信息
    :param city:
    :param keyword:
    :param page:
    :param sg:
    :return: None
    """
    ss = get_one_page(city, keyword, page, sg)
    if ss is None:
        print("wait A moment")
        time.sleep(2)
        main_cache(city, keyword, page, sg)
    else:
        ii = parse_one_page(ss)
        finally_list(ii)


def write_in_excel():
    """
    把整理过的数据放到excel中
    :return: None
    """
    writeSet = infoList
    if not os.path.exists("智联招聘"):
        os.mkdir("智联招聘")
    # 写到excel里面 可以用数据库代替
    file_name = str(int(time.time()))

    workbook = xlsxwriter.Workbook('智联招聘/%s%s.xlsx' % (positions, file_name))

    for i in range(len(writeSet) // 30000 + 1):
        cacheSet = set()
        worksheet = workbook.add_worksheet(positions + str(i))

        title = ("职位链接", "职位名称", "反馈率", "公司链接", "公司名称", "最低薪", "最高薪",
                 "工作区域", "工作地点", "企业性质", "公司规模", "经验", "学历")
        for title_index, title_value in enumerate(title):
            worksheet.write(0, title_index, title_value)

        for row, tt in enumerate(writeSet, 1):  # 整行的内容
            cacheSet.add(tt)
            for index, value in enumerate(tt):  # 每一单元格的内容
                worksheet.write(row, index, value)
            if row == 30000: break

        writeSet = writeSet - cacheSet

    workbook.close()

def main():
    """
    用线程池处理数据，并写入excel
    """
    for cc in city_get(cities):
        pool_para.apply_async(page_MD5_add, args=(cc, positions,))
    pool_para.close()
    pool_para.join()

    for ct, pos, pg, gg in parasList:
        pool_info.apply_async(main_cache, args=(ct, pos, pg, gg,))
    pool_info.close()
    pool_info.join()

    print("共计", len(infoList))
    write_in_excel()

if __name__ == '__main__':
    a1 = time.time()
    pool_info = Pool()   # 加入线程池，让速度飞起来
    pool_para = Pool()
    s = requests.Session()
    s.verify = "/path/to/certfile"  # 把verify保持在会话中

    cities = input("Which city would you want [all]: ")
    positions = input("Which position would you want [or more keywords]: ")

    infoList = set()
    parasList = set()

    main()
    print("花费", time.time()-a1, "秒")
    input()