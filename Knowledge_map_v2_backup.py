#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from database_interface import select_triple_table_neo4j
from neo4j_interface import creat_map

def knowledge_map(table_list):
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

