#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from crawler_total_v2_backup import crawler_total
from creat_triple_table_v2_backup import creat_triple
from Knowledge_map_v2_backup import knowledge_map
from neo4j_interface import select_node,select_relation
news_total={'domestic':{'News':{'2':['国内资讯',121]}},
            'international':{'News':{'3':['国际资讯',121]}},
            'cbhg':{'cbhg':{'news':['船舶海工',29],'news/1':['船舶海工',23]}},
            'culture':{'Culture':{'1':['历史文化',121]}},
            'economics':{'Economics':{'1':['蓝色经济',100]}},
            'edu':{'Edu':{'1':['教育资讯',62],'2':['海洋高校',41]}},
            'mil':{'Mil':{'1':['海洋军事',67],'4':['海洋军事',66]}},
            'tech':{'Tech':{'1':['海洋通讯',12],'3':['互联网+海洋',6],'4':['高新技术',84],'5':['生物技术',10]}},
            'trave':{'Trave':{'2':['海洋旅游',100]}}
            }
table_list=['todayhot','domestic','culture','cbhg','economics','edu','international','mil','tech','trave']
#更新爬取新闻
crawler_total(news_total)

#三元组抽取
creat_triple(table_list)

#图谱绘制
knowledge_map(table_list)
#实体查询
'''
#node_label:实体标签
#node_name:实体名称
#node_limit:输出数量，默认为1
返回字符串列表
#示例：
data=select_node(node_label='事件',node_limit=20)
for record in data:
    print(record)
'''
select_node(node_label='事件',node_limit=20)

#关系查询
'''
#model:默认为3，1：正向查询，2：反向查询，3：无方向查询，4：具体查询，5：查谓语
#node_label:实体标签
#object_label:宾语标签
#node_name:实体名称
#object_name:宾语名称
#relation:关系名称
#node_limit:输出数量，默认为5
#示例：
select_relation(model=4,node_label='机构',node_name='日本政府',object_name='以安防',object_label='名词',relation='为主')
'''
select_relation(model=1,node_label='机构',node_name='日本政府',relation='为主')
