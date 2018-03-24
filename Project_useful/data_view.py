#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
    Date:           03_08_2018  11:04
    File Name:      /GitHub/data_view
    Creat From:     PyCharm
    Python version: 3.6.2  
- - - - - - - - - - - - - - - 
    Description:
    http://blog.csdn.net/youzhouliu/article/details/78361503
    drawing use Plotly
    document: http://pyecharts.org/#/zh-cn/charts
==============================
"""

import logging
import datetime
import random
import math
from random import randint
from pyecharts import Bar
from pyecharts import EffectScatter
from pyecharts import Funnel
from pyecharts import Gauge
from pyecharts import Geo
from pyecharts import Graph
from pyecharts import Line
from pyecharts import Liquid
from pyecharts import Map
from pyecharts import Parallel
from pyecharts import Pie
from pyecharts import Polar
from pyecharts import Radar
from pyecharts import Scatter
from pyecharts import WordCloud
from pyecharts import Page  # 一页按顺序展示多图
from pyecharts import Bar3D
from pyecharts import HeatMap
from pyecharts import Kline
from pyecharts import Line3D
from pyecharts import Sankey
from pyecharts import Scatter3D
from pyecharts import ThemeRiver
from pyecharts import Grid  # 组合图
from pyecharts import Overlap  # 叠加多张图在一起
from pyecharts import Timeline

__author__ = 'Loffew'

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)

def singeObjectView(title, subhead, icon_name, obj_name=list, obj_data=list):
    """
    单项目柱状图
    :param title: 主题
    :param subhead: 副主题
    :param icon_name: 图标名称
    :param obj_name: 项目名称
    :param obj_data: 项目名称对应的项目值
    :return: 生成render.html 在当前目录
    """
    bar = Bar(title, subhead)
    bar.add(icon_name, obj_name, obj_data)
    bar.show_config()
    bar.render()

def barChart():
    """
    chart1 柱状图/chart2 条形图
    :return:
    """
    attr = ["obj1", "obj2", "obj3", "obj4", "obj5"]
    v1 = [14, 26, 22, 30, 7]
    v2 = [4, 33, 20, 25, 18]

    bar = Bar("标记线和标记点示例")
    bar.add("商家A", attr, v1, mark_point=["average"])
    bar.add("商家B", attr, v2, mark_line=["min", "max"])
    bar.render(path="C:/Users\lo\Desktop\html/bar_chart1.html")

    bar = Bar("x 轴和 y 轴交换")
    bar.add("商家A", attr, v1)
    bar.add("商家B", attr, v2, is_convert=True)
    bar.render(path="C:/Users\lo\Desktop\html/bar_chart2.html")

    attr = ["{}月".format(i) for i in range(1, 13)]
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    bar = Bar("柱状图示例")
    bar.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
    bar.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"])
    bar.show_config()
    bar.render(path="C:/Users\lo\Desktop\html/bar_chart3.html")

def effectScatter():
    """
    带有涟漪特效动画的散点图
    :return:
    """
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [25, 20, 15, 10, 60, 33]
    es = EffectScatter("动态散点图示例")
    es.add("effectScatter", v1, v2)
    es.render(path="C:/Users\lo\Desktop\html/effectScatter1.html")

    es = EffectScatter("动态散点图各种图形示例")
    es.add("", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
    es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4, symbol="rect")
    es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5, symbol="roundRect")
    es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill', symbol="diamond")
    es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3, symbol="arrow")
    es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3, symbol="triangle")
    es.render(path="C:/Users\lo\Desktop\html/effectScatter2.html")

    data = [
        [random.randint(0, 100),
         random.randint(0, 100),
         random.randint(0, 100)] for _ in range(80)
    ]
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    scatter3D.render(path="C:/Users\lo\Desktop\html/effectScatter3.html")

def funnelMap():
    """
    漏斗图
    :return:
    """
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value = [20, 40, 60, 80, 100, 120]
    funn = Funnel("漏斗图示例")
    funn.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
    funn.render(path="C:/Users\lo\Desktop\html/funnel.html")

def wheelGauge():
    """
    仪表盘
    :return:
    """
    gauge = Gauge("仪表盘示例")
    gauge.add("业务指标", "完成率", 42.66)
    # gauge.show_config()
    gauge.render(path="C:/Users\lo\Desktop\html/gauge.html")

def geographyHotPoint():
    """
    地图热点
    Here is a list of map extensions from pyecharts dev team:
    1.World countries include China map and World map: echarts-countries-pypkg (1.9MB)
    2.Chinese provinces and regions: echarts-china-provinces-pypkg (730KB)
    3.Chinese cities: echarts-china-cities-pypkg (3.8MB)

    In order to install them, you can try one of them or all:
    $ pip install echarts-countries-pypkg
    $ pip install echarts-china-provinces-pypkg
    $ pip install echarts-china-cities-pypkg

    type="effectScatter"：是否有涟漪动画效果。
    effect_scale=5：涟漪的多少。
    symbol="circle"：标记的形状（circle，pin，rect，diamon，roundRect，arrow，triangle）
    symbol_size=20：标记大小
    symbol_color="FF0000"：标记颜色
    geo_normal_color="#006edd"：地图颜色
    border_color="#ffffff"：地图线条颜色
    geo_emphasis_color="#0000ff"：鼠标放在地图上的颜色
    is_label_show=True：显示标签
    label_text_color="#00FF00"：标签颜色，本例是绿色
    label_pos="inside"：标签位置（inside，top，bottom，left，right）
    is_visualmap=True：显示图例条
    visual_range=[0, 300]：图例条范围
    visual_text_color='#fff'：图例条颜色
    :return:
    """
    data = [('三亚市', '10'), ('海口市', '13'), ('汕尾市', '15'), ('汕头市', '15'), ('三明市', '15'), ('惠州市', '15'), ('东莞市', '15'), ('潮州市', '15'), ('二连浩特市', '16'), ('揭阳市', '16'), ('中山市', '16'), ('河源市', '17'), ('深圳市', '18'), ('衢州市', '18'), ('江门市', '18'), ('广州市', '18'), ('香格里拉', '19'), ('肇庆市', '19'), ('南平市', '19'), ('阳江市', '20'), ('龙岩市', '20'), ('北海市', '21'), ('湛江市', '22'), ('梅州市', '22'), ('黄山市', '22'), ('佛山市', '22'), ('巢湖市', '22'), ('漳州市', '23'), ('云浮市', '23'), ('厦门市', '23'), ('泉州市', '23'), ('莆田市', '23'), ('南宁市', '23'), ('韶关市', '24'), ('茂名市', '25'), ('丽水市', '25'), ('阿里', '25'), ('香港特别行政区', '25'), ('温州市', '26'), ('柳州市', '26'), ('福州市', '26'), ('那曲', '26'), ('兴安盟', '27'), ('珠海市', '27'), ('鹰潭市', '27'), ('台州市', '27'), ('南昌市', '27'), ('上饶市', '28'), ('九江市', '28'), ('金华市', '28'), ('诸暨市', '29'), ('义乌市', '29'), ('通辽市', '29'), ('呼伦贝尔市', '29'), ('盘锦市', '29'), ('朝阳市', '29'), ('重庆市', '29'), ('承德市', '30'), ('忻州市', '30'), ('锦州市', '30'), ('阜新市', '30'), ('景德镇市', '30'), ('抚州市', '30'), ('瓦房店市', '31'), ('临安市', '32'), ('莱州市', '32'), ('丹东市', '32'), ('宜春市', '32'), ('绍兴市', '32'), ('萍乡市', '32'), ('日喀则', '32'), ('泸州市', '32'), ('甘孜', '32'), ('张家口市', '33'), ('秦皇岛市', '33'), ('赤峰市', '33'), ('葫芦岛市', '33'), ('杭州市', '33'), ('滨州市', '33'), ('昌都', '33'), ('桂林市', '34'), ('东营市', '34'), ('拉萨市', '34'), ('迪庆', '34'), ('寿光市', '35'), ('株洲市', '35'), ('衡阳市', '35'), ('常德市', '35'), ('内江市', '35'), ('林芝', '35'), ('阿坝', '35'), ('乳山市', '36'), ('阿拉善盟', '36'), ('遵义市', '36'), ('昭通市', '36'), ('山南', '36'), ('曲靖市', '36'), ('荣成市', '37'), ('呼和浩特市', '37'), ('铁岭市', '37'), ('大庆市', '37'), ('大连市', '37'), ('舟山市', '37'), ('永州市', '37'), ('长沙市', '37'), ('安庆市', '37'), ('克拉玛依市', '37'), ('巴中市', '37'), ('鄂尔多斯市', '38'), ('娄底市', '38'), ('吉安市', '38'), ('文山', '38'), ('乐山市', '38'), ('齐齐哈尔市', '39'), ('牡丹江市', '39'), ('吉林市', '39'), ('攀枝花市', '39'), ('沈阳市', '40'), ('湘潭市', '40'), ('宁波市', '40'), ('赣州市', '40'), ('恩施', '40'), ('沧州市', '41'), ('营口市', '41'), ('益阳市', '41'), ('遂宁市', '41'), ('胶州市', '42'), ('平度市', '42'), ('新余市', '42'), ('铜陵市', '42'), ('六安市', '42'), ('宜宾市', '42'), ('怒江傈', '42'), ('丽江市', '42'), ('广元市', '42'), ('即墨市', '43'), ('蓬莱市', '43'), ('招远市', '43'), ('邵阳市', '43'), ('眉山市', '43'), ('富阳市', '44'), ('文登市', '44'), ('黄冈市', '44'), ('哈尔滨市', '45'), ('潍坊市', '45'), ('泰安市', '45'), ('达州市', '45'), ('淄博市', '46'), ('烟台市', '46'), ('雅安市', '46'), ('包头市', '47'), ('黄石市', '47'), ('玉溪市', '47'), ('大理', '47'), ('保山市', '47'), ('莱西市', '48'), ('朔州市', '48'), ('张家界市', '49'), ('神农架', '50'), ('威海市', '50'), ('德州市', '50'), ('自贡市', '50'), ('红河哈尼族', '50'), ('成都市', '50'), ('章丘市', '51'), ('天津市', '51'), ('辽阳市', '51'), ('芜湖市', '51'), ('鄂州市', '51'), ('临沧市', '51'), ('晋中市', '52'), ('南充市', '52'), ('嘉峪关市', '52'), ('胶南市', '53'), ('咸宁市', '53'), ('十堰市', '53'), ('延安市', '53'), ('昆明市', '53'), ('吕梁市', '54'), ('鞍山市', '54'), ('岳阳市', '54'), ('青岛市', '54'), ('济宁市', '54'), ('郴州市', '54'), ('凉山', '54'), ('广安市', '54'), ('衡水市', '55'), ('锡林郭勒盟', '55'), ('宣城市', '55'), ('贵阳市', '55'), ('长春市', '56'), ('池州市', '56'), ('德宏', '56'), ('廊坊市', '57'), ('日照市', '57'), ('合肥市', '57'), ('楚雄', '57'), ('资阳市', '57'), ('抚顺市', '58'), ('本溪市', '58'), ('济南市', '58'), ('乌海市', '59'), ('大同市', '59'), ('莱芜市', '59'), ('金昌市', '59'), ('临汾市', '60'), ('临沂市', '60'), ('连云港市', '61'), ('嘉兴市', '61'), ('聊城市', '62'), ('德阳市', '63'), ('唐山市', '65'), ('湖州市', '65'), ('乌鲁木齐市', '65'), ('石嘴山市', '65'), ('银川市', '66'), ('菏泽市', '67'), ('北京市', '68'), ('荆州市', '68'), ('太原市', '69'), ('随州市', '69'), ('武汉市', '70'), ('铜川市', '70'), ('巴彦淖尔市', '71'), ('商丘市', '71'), ('清远市', '71'), ('鹤壁市', '71'), ('上海市', '72'), ('孝感市', '72'), ('绵阳市', '72'), ('咸阳市', '73'), ('宜昌市', '74'), ('济源', '75'), ('濮阳市', '75'), ('淮南市', '75'), ('亳州市', '75'), ('仙桃', '79'), ('渭南市', '80'), ('西安市', '81'), ('邢台市', '82'), ('荆门市', '82'), ('溧阳市', '83'), ('宜兴市', '84'), ('淮北市', '84'), ('西双版纳', '84'), ('吴江市', '86'), ('运城市', '86'), ('郑州市', '87'), ('焦作市', '87'), ('阜阳市', '87'), ('信阳市', '89'), ('滁州市', '89'), ('澳门', '91'), ('阳泉市', '92'), ('长治市', '92'), ('开封市', '92'), ('马鞍山市', '93'), ('潜江', '94'), ('邯郸市', '94'), ('保定市', '94'), ('洛阳市', '96'), ('枣庄市', '97'), ('许昌市', '98'), ('昆山市', '99'), ('盐城市', '99'), ('西宁市', '100'), ('无锡市', '101'), ('石家庄市', '102'), ('宝鸡市', '102'), ('兰州市', '103'), ('蚌埠市', '106'), ('安阳市', '107'), ('南京市', '109'), ('苏州市', '110'), ('周口市', '110'), ('海门市', '114'), ('淮安市', '122'), ('宿州市', '126'), ('句容市', '127'), ('驻马店市', '128'), ('三门峡市', '129'), ('徐州市', '130'), ('太仓市', '132'), ('南通市', '134'), ('平顶山市', '138'), ('宿迁市', '139'), ('金坛市', '141'), ('江阴市', '150'), ('常州市', '153'), ('常熟市', '156'), ('泰州市', '160'), ('张家港市', '171'), ('扬州市', '175'), ('漯河市', '175'), ('晋城市', '177'), ('南阳市', '181'), ('襄阳市', '191'), ('镇江市', '192'), ('库尔勒', '415')]
    geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
    geo.show_config()
    geo.render(path="C:/Users\lo\Desktop\html/geographyHotPoint1.html")

    data = [("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
    geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
    geo.show_config()
    geo.render(path="C:/Users\lo\Desktop\html/geographyHotPoint2.html")


def relateGraph():
    """
    关系图
    :return:
    """
    nodes = [{"name": "结点1", "symbolSize": 8}, {"name": "结点2", "symbolSize": 4}, {"name": "结点3", "symbolSize": 2},
             {"name": "结点4", "symbolSize": 4}, {"name": "结点5", "symbolSize": 5}, {"name": "结点6", "symbolSize": 4},
             {"name": "结点7", "symbolSize": 3}, {"name": "结点8", "symbolSize": 2}]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get('name'), "target": j.get('name')})
    graph = Graph("关系图-环形布局示例")
    graph.add("", nodes, links, is_label_show=True, repulsion=8000, layout='circular', label_text_color=None)
    # graph.show_config()
    graph.render(path="C:/Users\lo\Desktop\html/Graph.html")

    # with open("..jsonweibo.json", "r", encoding="utf-8") as f:
    #     j = json.load(f)
    #     nodes, links, categories, cont, mid, userl = j
    # graph = Graph("微博转发关系图", width=1200, height=600)
    # graph.add("", nodes, links, categories, label_pos="right", repulsion=50, is_legend_show=False, line_curve=0.2, label_text_color=None)
    # # graph.show_config()
    # graph.render(path="C:/Users\lo\Desktop\html/Graph_weibo.html")

def brokenLine():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]
    line = Line("折线图示例")
    line.add("商家A", attr, v1, mark_point=["average"])
    line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
    line.show_config()
    line.render(path="C:/Users\lo\Desktop\html/brokenLine1.html")

    line = Line("折线图-阶梯图示例")
    line.add("商家A", attr, v1, is_step=True, is_label_show=True)
    line.show_config()
    line.render(path="C:/Users\lo\Desktop\html/brokenLine2.htm")

    line = Line("折线图-面积图示例")
    line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
    line.add("商家B", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
    line.show_config()
    line.render(path="C:/Users\lo\Desktop\html/brokenLine3.htm")

    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日', ]
    line = Line("折线图示例")
    line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"], mark_line=["average"], yaxis_formatter="°C")
    line.show_config()
    line.render(path="C:/Users\lo\Desktop\html/brokenLine4.htm")

    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日', ]
    line = Line("折线图示例")
    line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"], mark_line=["average"], yaxis_formatter="°C")
    line.show_config()
    line.render(path="C:/Users\lo\Desktop\html/brokenLine5.htm")

def waterBall():
    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6])
    liquid.show_config()
    liquid.render(path="C:/Users\lo\Desktop\html/liquid1.htm")

    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
    liquid.show_config()
    liquid.render(path="C:/Users\lo\Desktop\html/liquid2.htm")

    liquid = Liquid("水球图示例")
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
    liquid.show_config()
    liquid.render(path="C:/Users\lo\Desktop\html/liquid3.htm")

    shape = ("path://M367.855,428.202c-3.674-1.385-7.452-1.966-11.146-1"
             ".794c0.659-2.922,0.844-5.85,0.58-8.719 c-0.937-10.407-7."
             "663-19.864-18.063-23.834c-10.697-4.043-22.298-1.168-29.9"
             "02,6.403c3.015,0.026,6.074,0.594,9.035,1.728 c13.626,5."
             "151,20.465,20.379,15.32,34.004c-1.905,5.02-5.177,9.115-9"
             ".22,12.05c-6.951,4.992-16.19,6.536-24.777,3.271 c-13.625"
             "-5.137-20.471-20.371-15.32-34.004c0.673-1.768,1.523-3.423"
             ",2.526-4.992h-0.014c0,0,0,0,0,0.014 c4.386-6.853,8.145-14"
             ".279,11.146-22.187c23.294-61.505-7.689-130.278-69.215-153"
             ".579c-61.532-23.293-130.279,7.69-153.579,69.202 c-6.371,"
             "16.785-8.679,34.097-7.426,50.901c0.026,0.554,0.079,1.121,"
             "0.132,1.688c4.973,57.107,41.767,109.148,98.945,130.793 c58."
             "162,22.008,121.303,6.529,162.839-34.465c7.103-6.893,17.826"
             "-9.444,27.679-5.719c11.858,4.491,18.565,16.6,16.719,28.643 "
             "c4.438-3.126,8.033-7.564,10.117-13.045C389.751,449.992,"
             "382.411,433.709,367.855,428.202z")
    liquid = Liquid("水球图示例", width=1000, height=600)
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], shape=shape, is_liquid_outline_show=False)
    liquid.render(path="C:/Users\lo\Desktop\html/liquid4.htm")

def mapHotPoint():
    """
    地图块显示
    Map 结合 VisualMap 示例
    :return: 
    """
    value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
    attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
    mapp = Map("全国地图示例", width=1200, height=600)
    mapp.add("", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')
    mapp.show_config()
    mapp.render(path="C:/Users\lo\Desktop\html/mapHotPoint1.htm")

    value = [20, 190, 253, 77, 65]
    attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
    mapp = Map("广东地图示例", width=1200, height=600)
    mapp.add("", attr, value, maptype='广东', is_visualmap=True, visual_text_color='#000')
    mapp.show_config()
    mapp.render(path="C:/Users\lo\Desktop\html/mapHotPoint2.htm")

    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ["China", "Canada", "Brazil", "Russia", "United States"]
    mapp = Map("世界地图示例", width=1200, height=600)
    mapp.add("", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000', is_map_symbol_show=False)
    mapp.render(path="C:/Users\lo\Desktop\html/mapHotPoint3.htm")

def parallelCoordinates():
    """
    平行坐标系
    :return:
    """
    c_schema = [{"dim": 0, "name": "data"}, {"dim": 1, "name": "AQI"}, {"dim": 2, "name": "PM2.5"},
                {"dim": 3, "name": "PM10"}, {"dim": 4, "name": "CO"}, {"dim": 5, "name": "NO2"},
                {"dim": 6, "name": "CO2"},
                {"dim": 7, "name": "等级", "type": "category", "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}]
    data = [[1, 91, 45, 125, 0.82, 34, 23, "良"], [2, 65, 27, 78, 0.86, 45, 29, "良"], [3, 83, 60, 84, 1.09, 73, 27, "良"],
            [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"], [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
            [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"], [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
            [8, 89, 65, 78, 0.86, 51, 26, "良"], [9, 53, 33, 47, 0.64, 50, 17, "良"], [10, 80, 55, 80, 1.01, 75, 24, "良"],
            [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"], [12, 99, 71, 142, 1.1, 62, 42, "良"],
            [13, 95, 69, 130, 1.28, 74, 50, "良"], [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]]
    parallel = Parallel("平行坐标系-用户自定义指示器")
    parallel.config(c_schema=c_schema)
    parallel.add("parallel", data)
    parallel.show_config()
    parallel.render(path="C:/Users\lo\Desktop\html/parallel.htm")

def cookiePie():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    pie = Pie("饼图示例")
    pie.add("", attr, v1, is_label_show=True)
    pie.show_config()
    pie.render(path="C:/Users\lo\Desktop\html/cookiePie1.htm")

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    v2 = [19, 21, 32, 20, 20, 33]
    pie = Pie("饼图-玫瑰图示例", title_pos='center', width=900)
    pie.add("商品A", attr, v1, center=[15, 50], is_random=True, radius=[30, 75], rosetype='radius')
    pie.add("商品B", attr, v2, center=[65, 50], is_random=True, radius=[30, 75], rosetype='area', is_legend_show=False, is_label_show=True)
    pie.show_config()
    pie.render(path="C:/Users\lo\Desktop\html/cookiePie2.htm")

    pie = Pie("饼图嵌套示例", title_pos='center', width=1000, height=600)
    pie.add("", ['A', 'B', 'C', 'D', 'E', 'F'], [335, 321, 234, 135, 251, 148], radius=[40, 55], is_label_show=True)
    pie.add("", ['H', 'I', 'J'], [335, 679, 204], radius=[0, 30], legend_orient='vertical', legend_pos='left')
    pie.show_config()
    pie.render(path="C:/Users\lo\Desktop\html/cookiePie3.htm")

    attr = ['A', 'B', 'C', 'D', 'E', 'F']
    pie = Pie("饼图示例", width=1000, height=600)
    pie.add("", attr, [random.randint(0, 100) for _ in range(6)], radius=[50, 55], center=[25, 50], is_random=True)
    pie.add("", attr, [random.randint(20, 100) for _ in range(6)], radius=[0, 45], center=[25, 50], rosetype='area')
    pie.add("", attr, [random.randint(0, 100) for _ in range(6)], radius=[50, 55], center=[65, 50], is_random=True)
    pie.add("", attr, [random.randint(20, 100) for _ in range(6)], radius=[0, 45], center=[65, 50], rosetype='radius')
    pie.show_config()
    pie.render(path="C:/Users\lo\Desktop\html/cookiePie4.htm")

    pie = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
    pie.add("", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, legend_pos='left')
    pie.add("", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["冒险", ""], [27, 73], center=[90, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["喜剧", ""], [54, 46], center=[30, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["悬疑", ""], [25, 75], center=[70, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
    pie.add("", ["犯罪", ""], [28, 72], center=[90, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, is_legend_show=True, legend_top="center")
    pie.show_config()
    pie.render(path="C:/Users\lo\Desktop\html/cookiePie5.htm")

def polarCoordinates():
    """
    极坐标系
    :return:
    """
    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
    polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
    polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
    polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
    polar.show_config()
    polar.render(path="C:/Users\lo\Desktop\html/polar1.htm")

    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
    polar.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barAngle', is_stack=True)
    polar.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barAngle', is_stack=True)
    polar.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barAngle', is_stack=True)
    polar.show_config()
    polar.render(path="C:/Users\lo\Desktop\html/polar2.htm")

    data = []
    for i in range(5):
        for j in range(101):
            theta = j / 100 * 360
            alpha = i * 360 + theta
            r = math.pow(math.e, 0.003 * alpha)
            data.append([r, theta])
    polar = Polar("极坐标系示例")
    polar.add("", data, symbol_size=0, symbol='circle', start_angle=-25, is_radiusaxis_show=False, area_color="#f3c5b3", area_opacity=0.5, is_angleaxis_show=False)
    polar.show_config()
    polar.render(path="C:/Users\lo\Desktop\html/polar3.htm")

    data = [(i, random.randint(1, 100)) for i in range(101)]
    polar = Polar("极坐标系-散点图示例")
    polar.add("", data, boundary_gap=False, type='scatter', is_splitline_show=False, area_color=None, is_axisline_show=True)
    polar.render(path="C:/Users\lo\Desktop\html/polar4.htm")

    data_1 = [(10, random.randint(1, 100)) for i in range(300)]
    data_2 = [(11, random.randint(1, 100)) for i in range(300)]
    polar = Polar("极坐标系-散点图示例", width=1200, height=600)
    polar.add("", data_1, type='scatter')
    polar.add("", data_2, type='scatter')
    polar.render(path="C:/Users\lo\Desktop\html/polar5.htm")

    data = [(i, random.randint(1, 100)) for i in range(10)]
    polar = Polar("极坐标系-动态散点图示例", width=1200, height=600)
    polar.add("", data, type='effectScatter', effect_scale=10, effect_period=5)
    polar.render(path="C:/Users\lo\Desktop\html/polar6.htm")


def radarCycle():
    schema = [("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
    v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    radar = Radar()
    radar.config(schema)
    radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
    radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
    radar.show_config()
    radar.render(path="C:/Users\lo\Desktop\html/radar1.htm")

    value_bj = [[55, 9, 56, 0.46, 18, 6, 1], [25, 11, 21, 0.65, 34, 9, 2], [56, 7, 63, 0.3, 14, 5, 3], [33, 7, 29, 0.33, 16, 6, 4], [42, 24, 44, 0.76, 40, 16, 5], [82, 58, 90, 1.77, 68, 33, 6], [74, 49, 77, 1.46, 48, 27, 7], [78, 55, 80, 1.29, 59, 29, 8], [267, 216, 280, 4.8, 108, 64, 9], [185, 127, 216, 2.52, 61, 27, 10], [39, 19, 38, 0.57, 31, 15, 11], [41, 11, 40, 0.43, 21, 7, 12], [64, 38, 74, 1.04, 46, 22, 13], [108, 79, 120, 1.7, 75, 41, 14], [108, 63, 116, 1.48, 44, 26, 15], [33, 6, 29, 0.34, 13, 5, 16], [94, 66, 110, 1.54, 62, 31, 17], [186, 142, 192, 3.88, 93, 79, 18], [57, 31, 54, 0.96, 32, 14, 19], [22, 8, 17, 0.48, 23, 10, 20], [39, 15, 36, 0.61, 29, 13, 21], [94, 69, 114, 2.08, 73, 39, 22], [99, 73, 110, 2.43, 76, 48, 23], [31, 12, 30, 0.5, 32, 16, 24], [42, 27, 43, 1, 53, 22, 25], [154, 117, 157, 3.05, 92, 58, 26], [234, 185, 230, 4.09, 123, 69, 27], [160, 120, 186, 2.77, 91, 50, 28], [134, 96, 165, 2.76, 83, 41, 29], [52, 24, 60, 1.03, 50, 21, 30]]
    value_sh = [[91, 45, 125, 0.82, 34, 23, 1], [65, 27, 78, 0.86, 45, 29, 2], [83, 60, 84, 1.09, 73, 27, 3], [109, 81, 121, 1.28, 68, 51, 4], [106, 77, 114, 1.07, 55, 51, 5], [109, 81, 121, 1.28, 68, 51, 6], [106, 77, 114, 1.07, 55, 51, 7], [89, 65, 78, 0.86, 51, 26, 8], [53, 33, 47, 0.64, 50, 17, 9], [80, 55, 80, 1.01, 75, 24, 10], [117, 81, 124, 1.03, 45, 24, 11], [99, 71, 142, 1.1, 62, 42, 12], [95, 69, 130, 1.28, 74, 50, 13], [116, 87, 131, 1.47, 84, 40, 14], [108, 80, 121, 1.3, 85, 37, 15], [134, 83, 167, 1.16, 57, 43, 16], [79, 43, 107, 1.05, 59, 37, 17], [71, 46, 89, 0.86, 64, 25, 18], [97, 71, 113, 1.17, 88, 31, 19], [84, 57, 91, 0.85, 55, 31, 20], [87, 63, 101, 0.9, 56, 41, 21], [104, 77, 119, 1.09, 73, 48, 22],  [87, 62, 100, 1, 72, 28, 23], [168, 128, 172, 1.49, 97, 56, 24], [65, 45, 51, 0.74, 39, 17, 25], [39, 24, 38, 0.61, 47, 17, 26], [39, 24, 39, 0.59, 50, 19, 27], [93, 68, 96, 1.05, 79, 29, 28], [188, 143, 197, 1.66, 99, 51, 29], [174, 131, 174, 1.55, 108, 50, 30]]
    c_schema = [{"name": "AQI", "max": 300, "min": 5}, {"name": "PM2.5", "max": 250, "min": 20}, {"name": "PM10", "max": 300, "min": 5}, {"name": "CO", "max": 5}, {"name": "NO2", "max": 200}, {"name": "SO2", "max": 100}]
    radar = Radar()
    radar.config(c_schema=c_schema, shape='circle')
    radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
    radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None, legend_selectedmode='single')
    radar.show_config()
    radar.render(path="C:/Users\lo\Desktop\html/radar2.htm")

    radar = Radar()
    radar.config(c_schema=c_schema, shape='circle')
    radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
    radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None)
    radar.render(path="C:/Users\lo\Desktop\html/radar3.htm")

def scatterPoint():
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    scatter = Scatter("散点图示例")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2)
    scatter.show_config()
    scatter.render(path="C:/Users\lo\Desktop\html/scatter1.htm")

    # scatter = Scatter("散点图示例")
    # v1, v2 = scatter.draw("../images/pyecharts-0.png")
    # scatter.add("pyecharts", v1, v2, is_random=True)
    # scatter.show_config()
    # scatter.render(path="C:/Users\lo\Desktop\html/scatter2.htm")

def wordCloud():
    name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A',
            'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton',
            'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament',
            'Point Break']
    value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273,
             265]
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[20, 100])
    wordcloud.show_config()
    wordcloud.render(path="C:/Users\lo\Desktop\html/wordCloud1.htm")

    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[30, 100], shape='diamond')
    wordcloud.show_config()
    wordcloud.render(path="C:/Users\lo\Desktop\html/wordCloud2.htm")

def threeDBar():
    bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
    x_axis = [
        "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
        "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
    y_axis = [
        "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
    data = [
        [0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0],
        [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2],
        [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3], [0, 16, 4], [0, 17, 6],
        [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
        [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0],
        [1, 6, 0], [1, 7, 0], [1, 8, 0], [1, 9, 0], [1, 10, 5], [1, 11, 2],
        [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
        [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2],
        [2, 0, 1], [2, 1, 1], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0],
        [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3], [2, 11, 2],
        [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5],
        [2, 18, 5], [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4],
        [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0],
        [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4],
        [3, 12, 7], [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5],
        [3, 18, 5], [3, 19, 10], [3, 20, 6], [3, 21, 4], [3, 22, 4], [3, 23, 1],
        [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
        [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4],
        [4, 12, 2], [4, 13, 4], [4, 14, 4], [4, 15, 14], [4, 16, 12], [4, 17, 1],
        [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3], [4, 23, 0],
        [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0],
        [5, 6, 0], [5, 7, 0], [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1],
        [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11], [5, 17, 6],
        [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0],
        [6, 0, 1], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0],
        [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1], [6, 11, 0],
        [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0],
        [6, 18, 0], [6, 19, 0], [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]
    ]
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data],
              is_visualmap=True, visual_range=[0, 20],
              visual_range_color=range_color, grid3d_width=200, grid3d_depth=80,
              is_grid3d_rotate=True, grid3d_rotate_speed=65)  # 最后两个是旋转参数项
    bar3d.render(path="C:/Users\lo\Desktop\html/3D_bar.html")

def dataHot():
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [[str(begin + datetime.timedelta(days=i)),
             random.randint(1000, 25000)] for i in range((end - begin).days + 1)]
    heatmap = HeatMap("日历热力图示例", "这是一个副标题", width=1100)
    heatmap.add("", data, is_calendar_heatmap=True,
                visual_text_color='#000', visual_range_text=['', ''],
                visual_range=[1000, 25000], calendar_cell_size=['auto', 30],
                is_visualmap=True, calendar_date_range="2017",
                visual_orient="horizontal", visual_pos="left",
                visual_top="80%", is_piecewise=True)
    heatmap.render(path="C:/Users\lo\Desktop\html/data_hot.html")

def kLine():
    v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
          [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
          [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
          [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
          [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
          [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
          [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
          [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
          [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
          [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
          [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
          [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
          [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
          [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
          [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
          [2255.77, 2270.28, 2253.31, 2276.22]]
    kline = Kline("K 线图示例")
    kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1)
    kline.render(path="C:/Users\lo\Desktop\html/k_line1.html")

    kline = Kline("K 线图示例")
    kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, mark_point=["max"], is_datazoom_show=True)
    kline.render(path="C:/Users\lo\Desktop\html/k_line2.html")

    kline = Kline("K 线图示例")
    kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, mark_point=["max"], is_datazoom_show=True, datazoom_orient='vertical')
    kline.render(path="C:/Users\lo\Desktop\html/k_line3.html")

    kline = Kline("K 线图示例")
    kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, mark_line=["max"], mark_line_symbolsize=0, datazoom_orient='vertical', mark_line_valuedim='close')
    kline.render(path="C:/Users\lo\Desktop\html/k_line4.html")

def threeDLine():
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("3D 折线图示例", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True, visual_range_color=range_color,
               visual_range=[0, 30], grid3d_rotate_sensitivity=5)
    line3d.render(path="C:/Users\lo\Desktop\html/line3D.html")

def sanKey():
    nodes = [
        {'name': 'category1'}, {'name': 'category2'}, {'name': 'category3'},
        {'name': 'category4'}, {'name': 'category5'}, {'name': 'category6'},
    ]

    links = [
        {'source': 'category1', 'target': 'category2', 'value': 10},
        {'source': 'category2', 'target': 'category3', 'value': 15},
        {'source': 'category3', 'target': 'category4', 'value': 20},
        {'source': 'category5', 'target': 'category6', 'value': 25}
    ]
    sankey = Sankey("桑基图示例", width=1200, height=600)
    sankey.add("sankey", nodes, links, line_opacity=0.2,
               line_curve=0.5, line_color='source',
               is_label_show=True, label_pos='right')
    sankey.render(path="C:/Users\lo\Desktop\html/sankey1.html")

    # with codecs.open(os.path.join("fixtures", "energy.json"), "r", encoding="utf-8") as f:
    #     j = json.load(f)
    # sankey = Sankey("桑基图示例", width=1200, height=600)
    # sankey.add("sankey", nodes=j['nodes'], links=j['links'],
    #            line_opacity=0.2, line_curve=0.5, line_color='source',
    #            is_label_show=True, label_pos='right')
    # sankey.render(path="C:/Users\lo\Desktop\html/sankey2.html")

def theRiver():
    data = [
        ['2015/11/08', 10, 'DQ'], ['2015/11/09', 15, 'DQ'], ['2015/11/10', 35, 'DQ'],
        ['2015/11/14', 7, 'DQ'], ['2015/11/15', 2, 'DQ'], ['2015/11/16', 17, 'DQ'],
        ['2015/11/17', 33, 'DQ'], ['2015/11/18', 40, 'DQ'], ['2015/11/19', 32, 'DQ'],
        ['2015/11/20', 26, 'DQ'], ['2015/11/21', 35, 'DQ'], ['2015/11/22', 40, 'DQ'],
        ['2015/11/23', 32, 'DQ'], ['2015/11/24', 26, 'DQ'], ['2015/11/25', 22, 'DQ'],
        ['2015/11/08', 35, 'TY'], ['2015/11/09', 36, 'TY'], ['2015/11/10', 37, 'TY'],
        ['2015/11/11', 22, 'TY'], ['2015/11/12', 24, 'TY'], ['2015/11/13', 26, 'TY'],
        ['2015/11/14', 34, 'TY'], ['2015/11/15', 21, 'TY'], ['2015/11/16', 18, 'TY'],
        ['2015/11/17', 45, 'TY'], ['2015/11/18', 32, 'TY'], ['2015/11/19', 35, 'TY'],
        ['2015/11/20', 30, 'TY'], ['2015/11/21', 28, 'TY'], ['2015/11/22', 27, 'TY'],
        ['2015/11/23', 26, 'TY'], ['2015/11/24', 15, 'TY'], ['2015/11/25', 30, 'TY'],
        ['2015/11/26', 35, 'TY'], ['2015/11/27', 42, 'TY'], ['2015/11/28', 42, 'TY'],
        ['2015/11/08', 21, 'SS'], ['2015/11/09', 25, 'SS'], ['2015/11/10', 27, 'SS'],
        ['2015/11/11', 23, 'SS'], ['2015/11/12', 24, 'SS'], ['2015/11/13', 21, 'SS'],
        ['2015/11/14', 35, 'SS'], ['2015/11/15', 39, 'SS'], ['2015/11/16', 40, 'SS'],
        ['2015/11/17', 36, 'SS'], ['2015/11/18', 33, 'SS'], ['2015/11/19', 43, 'SS'],
        ['2015/11/20', 40, 'SS'], ['2015/11/21', 34, 'SS'], ['2015/11/22', 28, 'SS'],
        ['2015/11/14', 7, 'QG'], ['2015/11/15', 2, 'QG'], ['2015/11/16', 17, 'QG'],
        ['2015/11/17', 33, 'QG'], ['2015/11/18', 40, 'QG'], ['2015/11/19', 32, 'QG'],
        ['2015/11/20', 26, 'QG'], ['2015/11/21', 35, 'QG'], ['2015/11/22', 40, 'QG'],
        ['2015/11/23', 32, 'QG'], ['2015/11/24', 26, 'QG'], ['2015/11/25', 22, 'QG'],
        ['2015/11/26', 16, 'QG'], ['2015/11/27', 22, 'QG'], ['2015/11/28', 10, 'QG'],
        ['2015/11/08', 10, 'SY'], ['2015/11/09', 15, 'SY'], ['2015/11/10', 35, 'SY'],
        ['2015/11/11', 38, 'SY'], ['2015/11/12', 22, 'SY'], ['2015/11/13', 16, 'SY'],
        ['2015/11/14', 7, 'SY'], ['2015/11/15', 2, 'SY'], ['2015/11/16', 17, 'SY'],
        ['2015/11/17', 33, 'SY'], ['2015/11/18', 40, 'SY'], ['2015/11/19', 32, 'SY'],
        ['2015/11/20', 26, 'SY'], ['2015/11/21', 35, 'SY'], ['2015/11/22', 4, 'SY'],
        ['2015/11/23', 32, 'SY'], ['2015/11/24', 26, 'SY'], ['2015/11/25', 22, 'SY'],
        ['2015/11/26', 16, 'SY'], ['2015/11/27', 22, 'SY'], ['2015/11/28', 10, 'SY'],
        ['2015/11/08', 10, 'DD'], ['2015/11/09', 15, 'DD'], ['2015/11/10', 35, 'DD'],
        ['2015/11/11', 38, 'DD'], ['2015/11/12', 22, 'DD'], ['2015/11/13', 16, 'DD'],
        ['2015/11/14', 7, 'DD'], ['2015/11/15', 2, 'DD'], ['2015/11/16', 17, 'DD'],
        ['2015/11/17', 33, 'DD'], ['2015/11/18', 4, 'DD'], ['2015/11/19', 32, 'DD'],
        ['2015/11/20', 26, 'DD'], ['2015/11/21', 35, 'DD'], ['2015/11/22', 40, 'DD'],
        ['2015/11/23', 32, 'DD'], ['2015/11/24', 26, 'DD'], ['2015/11/25', 22, 'DD']
    ]
    tr = ThemeRiver("主题河流图示例图")
    tr.add(['DQ', 'TY', 'SS', 'QG', 'SY', 'DD'], data, is_label_show=True)
    tr.render(path="C:/Users\lo\Desktop\html/river.html")

def multiphoto():
    """
    用page 类，实现一页多图
    用is_more_utils=True 实现多工具
    :return:
    """
    p = Page()
    attr = ["obj1", "obj2", "obj3", "obj4", "obj5"]
    v1 = [14, 26, 22, 30, 7]
    v2 = [4, 33, 20, 25, 18]

    bar = Bar("标记线和标记点示例", width=1200)
    bar.add("商家A", attr, v1, mark_point=["average"],  is_more_utils=True)
    bar.add("商家B", attr, v2, mark_line=["min", "max"], is_more_utils=True)
    p.add(bar)

    bar = Bar("x 轴和 y 轴交换")
    bar.add("商家A", attr, v1, is_more_utils=True)
    bar.add("商家B", attr, v2, is_convert=True, is_more_utils=True)
    p.add(bar)
    p.render(path="C:/Users\lo\Desktop\html/multi_bar.html")

def onePageGroup():
    """
    自定义结合 Line/Bar/Kline/Scatter/EffectScatter/Pie/HeatMap/Boxplot 图表，将不同类型图表画在多张图上。第一个图需为 有 x/y 轴的图，即不能为 Pie，其他位置顺序任意
    :return:
    """
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图示例", height=720)
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True)
    line = Line("折线图示例", title_top="50%")
    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"], mark_line=["average"], legend_top="50%")

    grid = Grid()
    grid.add(bar, grid_bottom="60%")
    grid.add(line, grid_top="60%")
    grid.render(path="C:/Users\lo\Desktop\html/guid1.html")

    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    scatter = Scatter(width=1200)
    scatter.add("散点图示例", v1, v2, legend_pos="70%")
    es = EffectScatter()
    es.add("动态散点图示例", [11, 11, 15, 13, 12, 13, 10], [1, -2, 2, 5, 3, 2, 0], effect_scale=6, legend_pos="20%")

    grid = Grid()
    grid.add(scatter, grid_left="60%")
    grid.add(es, grid_right="60%")
    grid.render(path="C:/Users\lo\Desktop\html/guid2.html")

    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图示例", height=720, width=1200, title_pos="65%")
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True, legend_pos="80%")
    line = Line("折线图示例")
    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"], mark_line=["average"], legend_pos="20%")
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    scatter = Scatter("散点图示例", title_top="50%", title_pos="65%")
    scatter.add("scatter", v1, v2, legend_top="50%", legend_pos="80%")
    es = EffectScatter("动态散点图示例", title_top="50%")
    es.add("es", [11, 11, 15, 13, 12, 13, 10], [1, -2, 2, 5, 3, 2, 0], effect_scale=6, legend_top="50%", legend_pos="20%")

    grid = Grid()
    grid.add(bar, grid_bottom="60%", grid_left="60%")
    grid.add(line, grid_bottom="60%", grid_right="60%")
    grid.add(scatter, grid_top="60%", grid_left="60%")
    grid.add(es, grid_top="60%", grid_right="60%")
    grid.render(path="C:/Users\lo\Desktop\html/guid3.html")

    line = Line("折线图示例", width=1200)
    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"], mark_line=["average"], legend_pos="20%")
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    pie = Pie("饼图示例", title_pos="55%")
    pie.add("", attr, v1, radius=[45, 65], center=[65, 50], legend_pos="80%", legend_orient='vertical')

    grid = Grid()
    grid.add(line, grid_right="55%")
    grid.add(pie, grid_left="60%")
    grid.render(path="C:/Users\lo\Desktop\html/guid4.html")

    line = Line("折线图示例", width=1200)
    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],  mark_point=["max", "min"], mark_line=["average"], legend_pos="20%")
    v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
          [2300, 2291.3, 2288.26, 2308.38],
          [2295.35, 2346.5, 2295.35, 2345.92],
          [2347.22, 2358.98, 2337.35, 2363.8],
          [2360.75, 2382.48, 2347.89, 2383.76],
          [2383.43, 2385.42, 2371.23, 2391.82],
          [2377.41, 2419.02, 2369.57, 2421.15],
          [2425.92, 2428.15, 2417.58, 2440.38],
          [2411, 2433.13, 2403.3, 2437.42],
          [2432.68, 2334.48, 2427.7, 2441.73],
          [2430.69, 2418.53, 2394.22, 2433.89],
          [2416.62, 2432.4, 2414.4, 2443.03],
          [2441.91, 2421.56, 2418.43, 2444.8],
          [2420.26, 2382.91, 2373.53, 2427.07],
          [2383.49, 2397.18, 2370.61, 2397.94],
          [2378.82, 2325.95, 2309.17, 2378.82],
          [2322.94, 2314.16, 2308.76, 2330.88],
          [2320.62, 2325.82, 2315.01, 2338.78],
          [2313.74, 2293.34, 2289.89, 2340.71],
          [2297.77, 2313.22, 2292.03, 2324.63],
          [2322.32, 2365.59, 2308.92, 2366.16],
          [2364.54, 2359.51, 2330.86, 2369.65],
          [2332.08, 2273.4, 2259.25, 2333.54],
          [2274.81, 2326.31, 2270.1, 2328.14],
          [2333.61, 2347.18, 2321.6, 2351.44],
          [2340.44, 2324.29, 2304.27, 2352.02],
          [2326.42, 2318.61, 2314.59, 2333.67],
          [2314.68, 2310.59, 2296.58, 2320.96],
          [2309.16, 2286.6, 2264.83, 2333.29],
          [2282.17, 2263.97, 2253.25, 2286.33],
          [2255.77, 2270.28, 2253.31, 2276.22]]
    kline = Kline("K 线图示例", title_pos="60%")
    kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, legend_pos="80%")

    grid = Grid()
    grid.add(line, grid_right="60%")
    grid.add(kline, grid_left="55%")
    grid.render(path="C:/Users\lo\Desktop\html/guid5.html")

    x_axis = [
        "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
        "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
    y_axis = [
        "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    heatmap = HeatMap("热力图示例", height=700)
    heatmap.add("热力图直角坐标系", x_axis, y_axis, data, is_visualmap=True,
                visual_top="45%", visual_text_color="#000",
                visual_orient='horizontal')
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图示例", title_top="52%")
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True, legend_top="50%")

    grid = Grid()
    grid.add(heatmap, grid_bottom="60%")
    grid.add(bar, grid_top="60%")
    grid.render(path="C:/Users\lo\Desktop\html/guid6.html")

    line = Line("折线图示例", width=1200, height=700)
    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
             mark_point=["max", "min"], mark_line=["average"])
    line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],
             mark_point=["max", "min"], legend_top="50%", mark_line=["average"],
             # 设置 dataZoom 控制索引为 0,1 的 x 轴，即第一个和第二个
             is_datazoom_show=True, datazoom_xaxis_index=[0, 1])

    v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
          [2300, 2291.3, 2288.26, 2308.38],
          [2295.35, 2346.5, 2295.35, 2345.92],
          [2347.22, 2358.98, 2337.35, 2363.8],
          [2360.75, 2382.48, 2347.89, 2383.76],
          [2383.43, 2385.42, 2371.23, 2391.82],
          [2377.41, 2419.02, 2369.57, 2421.15],
          [2425.92, 2428.15, 2417.58, 2440.38],
          [2411, 2433.13, 2403.3, 2437.42],
          [2432.68, 2334.48, 2427.7, 2441.73],
          [2430.69, 2418.53, 2394.22, 2433.89],
          [2416.62, 2432.4, 2414.4, 2443.03],
          [2441.91, 2421.56, 2418.43, 2444.8],
          [2420.26, 2382.91, 2373.53, 2427.07],
          [2383.49, 2397.18, 2370.61, 2397.94],
          [2378.82, 2325.95, 2309.17, 2378.82],
          [2322.94, 2314.16, 2308.76, 2330.88],
          [2320.62, 2325.82, 2315.01, 2338.78],
          [2313.74, 2293.34, 2289.89, 2340.71],
          [2297.77, 2313.22, 2292.03, 2324.63],
          [2322.32, 2365.59, 2308.92, 2366.16],
          [2364.54, 2359.51, 2330.86, 2369.65],
          [2332.08, 2273.4, 2259.25, 2333.54],
          [2274.81, 2326.31, 2270.1, 2328.14],
          [2333.61, 2347.18, 2321.6, 2351.44],
          [2340.44, 2324.29, 2304.27, 2352.02],
          [2326.42, 2318.61, 2314.59, 2333.67],
          [2314.68, 2310.59, 2296.58, 2320.96],
          [2309.16, 2286.6, 2264.83, 2333.29],
          [2282.17, 2263.97, 2253.25, 2286.33],
          [2255.77, 2270.28, 2253.31, 2276.22]]
    kline = Kline("K 线图示例", title_top="50%")
    kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, is_datazoom_show=True)

    grid = Grid()
    grid.add(line, grid_top="60%")
    grid.add(kline, grid_bottom="60%")
    grid.render(path="C:/Users\lo\Desktop\html/guid7.html")

    attr = ['{}天'.format(i) for i in range(1, 31)]
    line_top = Line("折线图示例", width=1200, height=700)
    line_top.add("最高气温", attr, [random.randint(20, 100) for i in range(30)],
                 mark_point=["max", "min"], mark_line=["average"], legend_pos='38%')
    line_bottom = Line()
    line_bottom.add("最低气温", attr, [random.randint(20, 100) for i in range(30)],
                    mark_point=["max", "min"], mark_line=["average"],
                    is_yaxis_inverse=True, xaxis_pos='top')

    grid = Grid()
    grid.add(line_top, grid_bottom='60%')
    grid.add(line_bottom, grid_top='50%')
    grid.render(path="C:/Users\lo\Desktop\html/guid8.html")

    attr = ["{}月".format(i) for i in range(1, 13)]
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

    bar = Bar(width=1200, height=600, title="Overlap+Grid 示例", title_pos="40%")
    bar.add("蒸发量", attr, v1)
    bar.add("降水量", attr, v2, yaxis_formatter=" ml", yaxis_max=250,
            legend_pos="85%", legend_orient="vertical", legend_top="45%")
    line = Line()
    line.add("平均温度", attr, v3, yaxis_formatter=" °C")
    overlap = Overlap()
    overlap.add(bar)
    overlap.add(line, is_add_yaxis=True, yaxis_index=1)

    grid = Grid()
    grid.add(overlap, grid_right='20%')
    grid.render(path="C:/Users\lo\Desktop\html/guid9.html")

def overLap():
    attr = ['A', 'B', 'C', 'D', 'E', 'F']
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [38, 28, 58, 48, 78, 68]
    bar = Bar("Line - Bar 示例")
    bar.add("bar", attr, v1)
    line = Line()
    line.add("line", attr, v2)

    overlap = Overlap()
    overlap.add(bar)
    overlap.add(line)
    overlap.render(path="C:/Users\lo\Desktop\html/over_lap.html")

def timeLine():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    bar_1 = Bar("2012 年销量", "数据纯属虚构")
    bar_1.add("春季", attr, [randint(10, 100) for _ in range(6)])
    bar_1.add("夏季", attr, [randint(10, 100) for _ in range(6)])
    bar_1.add("秋季", attr, [randint(10, 100) for _ in range(6)])
    bar_1.add("冬季", attr, [randint(10, 100) for _ in range(6)])

    bar_2 = Bar("2013 年销量", "数据纯属虚构")
    bar_2.add("春季", attr, [randint(10, 100) for _ in range(6)])
    bar_2.add("夏季", attr, [randint(10, 100) for _ in range(6)])
    bar_2.add("秋季", attr, [randint(10, 100) for _ in range(6)])
    bar_2.add("冬季", attr, [randint(10, 100) for _ in range(6)])

    bar_3 = Bar("2014 年销量", "数据纯属虚构")
    bar_3.add("春季", attr, [randint(10, 100) for _ in range(6)])
    bar_3.add("夏季", attr, [randint(10, 100) for _ in range(6)])
    bar_3.add("秋季", attr, [randint(10, 100) for _ in range(6)])
    bar_3.add("冬季", attr, [randint(10, 100) for _ in range(6)])

    bar_4 = Bar("2015 年销量", "数据纯属虚构")
    bar_4.add("春季", attr, [randint(10, 100) for _ in range(6)])
    bar_4.add("夏季", attr, [randint(10, 100) for _ in range(6)])
    bar_4.add("秋季", attr, [randint(10, 100) for _ in range(6)])
    bar_4.add("冬季", attr, [randint(10, 100) for _ in range(6)])

    bar_5 = Bar("2016 年销量", "数据纯属虚构")
    bar_5.add("春季", attr, [randint(10, 100) for _ in range(6)])
    bar_5.add("夏季", attr, [randint(10, 100) for _ in range(6)])
    bar_5.add("秋季", attr, [randint(10, 100) for _ in range(6)])
    bar_5.add("冬季", attr, [randint(10, 100) for _ in range(6)], is_legend_show=True)

    timeline = Timeline(is_auto_play=True, timeline_bottom=0)
    timeline.add(bar_1, '2012 年')
    timeline.add(bar_2, '2013 年')
    timeline.add(bar_3, '2014 年')
    timeline.add(bar_4, '2015 年')
    timeline.add(bar_5, '2016 年')
    timeline.render(path="C:/Users\lo\Desktop\html/time_line1.html")

    attr = ["{}月".format(i) for i in range(1, 7)]
    bar = Bar("1 月份数据", "数据纯属虚构")
    bar.add("bar", attr, [randint(10, 50) for _ in range(6)])
    line = Line()
    line.add("line", attr, [randint(50, 80) for _ in range(6)])
    overlap = Overlap()
    overlap.add(bar)
    overlap.add(line)

    bar_1 = Bar("2 月份数据", "数据纯属虚构")
    bar_1.add("bar", attr, [randint(10, 50) for _ in range(6)])
    line_1 = Line()
    line_1.add("line", attr, [randint(50, 80) for _ in range(6)])
    overlap_1 = Overlap()
    overlap_1.add(bar_1)
    overlap_1.add(line_1)

    bar_2 = Bar("3 月份数据", "数据纯属虚构")
    bar_2.add("bar", attr, [randint(10, 50) for _ in range(6)])
    line_2 = Line()
    line_2.add("line", attr, [randint(50, 80) for _ in range(6)])
    overlap_2 = Overlap()
    overlap_2.add(bar_2)
    overlap_2.add(line_2)

    bar_3 = Bar("4 月份数据", "数据纯属虚构")
    bar_3.add("bar", attr, [randint(10, 50) for _ in range(6)])
    line_3 = Line()
    line_3.add("line", attr, [randint(50, 80) for _ in range(6)])
    overlap_3 = Overlap()
    overlap_3.add(bar_3)
    overlap_3.add(line_3)

    bar_4 = Bar("5 月份数据", "数据纯属虚构")
    bar_4.add("bar", attr, [randint(10, 50) for _ in range(6)])
    line_4 = Line()
    line_4.add("line", attr, [randint(50, 80) for _ in range(6)])
    overlap_4 = Overlap()
    overlap_4.add(bar_4)
    overlap_4.add(line_4)

    timeline = Timeline(timeline_bottom=0)
    timeline.add(overlap, '1 月')
    timeline.add(overlap_1, '2 月')
    timeline.add(overlap_2, '3 月')
    timeline.add(overlap_3, '4 月')
    timeline.add(overlap_4, '5 月')
    timeline.render(path="C:/Users\lo\Desktop\html/time_line2.html")

if __name__ == '__main__':
    barChart()
    effectScatter()
    funnelMap()
    wheelGauge()
    geographyHotPoint()
    relateGraph()
    brokenLine()
    waterBall()
    mapHotPoint()
    parallelCoordinates()
    cookiePie()
    polarCoordinates()
    radarCycle()
    scatterPoint()
    wordCloud()
    multiphoto()
    threeDBar()
    dataHot()
    threeDLine()
    sanKey()
    theRiver()
    onePageGroup()
    overLap()
    timeLine()