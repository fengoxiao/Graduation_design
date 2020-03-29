#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 有用的代码
from crawler.database_test_total import table_not_exists_v2,creat_table_v2,select_sea_add_news

table_list = ['domestic', 'culture', 'cbhg', 'economics', 'edu', 'international', 'mil', 'tech', 'trave']
for table in table_list:
    table1 = "sea_news_{}".format(table)  # 原表
    table2 = "sea_news_{}_v2".format(table)  # 创建v2表
    if table_not_exists_v2(table2):
        creat_table_v2(table2)
        print('创建{}表成功'.format(table2))
    select_sea_add_news(table1, table2)

