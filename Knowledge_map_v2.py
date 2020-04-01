#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from database_interface import select_triple_table_neo4j
from neo4j_interface import creat_map

#from EventTriplesExtraction.triple_extraction import TripleExtractor
#清空图
#match (n) detach delete n
#清空表
#truncate_table_neo4j("triple_{}".format('domestic'))
#extractor = TripleExtractor()
table_list=['domestic','culture','cbhg','economics','edu','international','mil','tech','trave']
#table_list=['trave']


#MATCH (n {name:"杰克"}) set n:animal return n
#根据三元组创建图
for table in table_list:
    table_name_triple = "triple_{}_v2".format(table)
    data=select_triple_table_neo4j(table_name_triple)
    for record in data:
        flag=creat_map(record)
        if  0==flag:
            print('创建失败:',record)
        elif 1==flag:
            print('写入一个关系')
    print('完成了{}表的图谱创建'.format(table))
print('end')

