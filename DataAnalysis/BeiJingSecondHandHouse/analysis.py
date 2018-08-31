#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==============================
  Date:           08_31_2018  9:38
  File Name:      /Python-Practice/analysis
  Creat From:     PyCharm
  Python version: 3.6.2
- - - - - - - - - - - - - - - 
  Description:
     次为一个数据分析的初级项目，目的是通过项目了解如何使用Python进行简单的数据分析
     pycharm有比较多的问题
==============================
"""
# 首先导入要使用的科学计算包numpy,pandas,可视化matplotlib, seaborn,以及机器学习包sklearn
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl

import matplotlib.pyplot as plt
from IPython.display import display

from check_version import checkversion

plt.style.use("fivethirtyeight")
sns.set_style({'font.sans-serif': ['simhei', 'Arial']})
# # 如果可以 % matplotlib inline 就可以省掉plt.show()
# plt.show()

# 检查版本
checkversion()

# 导入链家二手房数据
lianjia_df = pd.read_csv('lianjia.csv', encoding="utf8")
display(lianjia_df.head(n=2))

# 检查缺失值情况
# lianjia_df.info()

# 特征的缺失值
# lianjia_df.describe()

# 添加新特征房屋均价
df = lianjia_df.copy()
df['PerPrice'] = lianjia_df['Price'] / lianjia_df['Size']

# 重新摆放列位置
columns = ['Region', 'District', 'Garden', 'Layout', 'Floor', 'Year', 'Size', 'Elevator', 'Direction', 'Renovation',
           'PerPrice', 'Price']
df = pd.DataFrame(df, columns=columns)

# 重新审视数据集
# display(df.head(n=2))

df_house_count = df.groupby('Region')['Price'].count().sort_values(ascending=False).to_frame().reset_index()
df_house_mean = df.groupby('Region')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index()

# f, [ax1, ax2, ax3] = plt.subplots(3, 1, figsize=(20, 15))
# sns.barplot(x='Region', y='PerPrice', palette="Blues_d", data=df_house_mean, ax=ax1)
# ax1.set_title('北京各大区二手房每平米单价对比', fontsize=15)
# ax1.set_xlabel('区域')
# ax1.set_ylabel('每平米单价')
#
# sns.barplot(x='Region', y='Price', palette="Greens_d", data=df_house_count, ax=ax2)
# ax2.set_title('北京各大区二手房数量对比', fontsize=15)
# ax2.set_xlabel('区域')
# ax2.set_ylabel('数量')
#
# sns.boxplot(x='Region', y='Price', data=df, ax=ax3)
# ax3.set_title('北京各大区二手房房屋总价', fontsize=15)
# ax3.set_xlabel('区域')
# ax3.set_ylabel('房屋总价')
#
# plt.show()


# f, [ax1,ax2] = plt.subplots(1, 2, figsize=(15, 5))
# # 建房时间的分布情况
# sns.distplot(df['Size'], bins=20, ax=ax1, color='r')
# sns.kdeplot(df['Size'], shade=True, ax=ax1)
# # 建房时间和出售价格的关系
# sns.regplot(x='Size', y='Price', data=df, ax=ax2)
# plt.show()

df = df[(df['Layout'] != '叠拼别墅') & (df['Size'] < 1000)]

# f, ax1= plt.subplots(figsize=(20,20))
# sns.countplot(y='Layout', data=df, ax=ax1)
# ax1.set_title('房屋户型',fontsize=15)
# ax1.set_xlabel('数量')
# ax1.set_ylabel('户型')
# plt.show()

# print(df['Renovation'].value_counts())

df['Renovation'] = df.loc[(df['Renovation'] != '南北'), 'Renovation']

# 画幅设置
# f, [ax1, ax2, ax3] = plt.subplots(1, 3, figsize=(20, 5))
# sns.countplot(df['Renovation'], ax=ax1)
# sns.barplot(x='Renovation', y='Price', data=df, ax=ax2)
# sns.boxplot(x='Renovation', y='Price', data=df, ax=ax3)
# plt.show()

# Elevator 特征分析
misn = len(df.loc[(df['Elevator'].isnull()), 'Elevator'])
print('Elevator缺失值数量为：' + str(misn))

# 由于存在个别类型错误，如简装和精装，特征值错位，故需要移除
df['Elevator'] = df.loc[(df['Elevator'] == '有电梯')|(df['Elevator'] == '无电梯'), 'Elevator']

# 填补Elevator缺失值
# df.loc[(df['Floor']>6)&(df['Elevator'].isnull()), 'Elevator'] = '有电梯'
# df.loc[(df['Floor']<=6)&(df['Elevator'].isnull()), 'Elevator'] = '无电梯'
#
# f, [ax1,ax2] = plt.subplots(1, 2, figsize=(20, 10))
# sns.countplot(df['Elevator'], ax=ax1)
# ax1.set_title('有无电梯数量对比',fontsize=15)
# ax1.set_xlabel('是否有电梯')
# ax1.set_ylabel('数量')
# sns.barplot(x='Elevator', y='Price', data=df, ax=ax2)
# ax2.set_title('有无电梯房价对比',fontsize=15)
# ax2.set_xlabel('是否有电梯')
# ax2.set_ylabel('总价')
# plt.show()

# Year 特征分析
# grid = sns.FacetGrid(df, row='Elevator', col='Renovation', palette='seismic',size=4)
# grid.map(plt.scatter, 'Year', 'Price')
# grid.add_legend()

# Floor 特征分析
# f, ax1= plt.subplots(figsize=(20,5))
# sns.countplot(x='Floor', data=df, ax=ax1)
# ax1.set_title('房屋户型',fontsize=15)
# ax1.set_xlabel('数量')
# ax1.set_ylabel('户型')
# plt.show()