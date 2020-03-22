#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from database_test import select_triple_table,creat_triple_table,select_triple_table_neo4j,creat_table_neo4j,record_had_extracting,table_not_exists,truncate_table_neo4j
from EventTriplesExtraction.triple_extraction import TripleExtractor
from neo4j_interface import creat_map

#MATCH (n {name:"杰克"}) set n:animal return n
#match (n) detach delete n

extractor = TripleExtractor()
#table_list=['domestic','culture','cbhg','economics','edu','international','mil','tech','trave']
table_list=['trave']

#清空表
#truncate_table_neo4j("triple_{}".format('domestic'))

#表的创建
for table in table_list:#读取表，抽取三元组
    #sql = "select id,news_title,news_summary from sea_news_{}".format(table)
    attribute_columns=('id','news_title','news_summary')#属性列
    table_name="sea_news_{}".format(table)
    table_name_triple="triple_{}".format(table)
    if table_not_exists(table_name_triple):
        creat_table_neo4j(table_name_triple)
    data=select_triple_table(table_name,attribute_columns)
    for record in data:
        if record_had_extracting(table_name_triple,table_name,record[0]):
            continue
        original_text=record[1]
        svo_result_list = extractor.triples_main(original_text)#title
        if not svo_result_list:
            original_text=record[2]
            svo_result_list = extractor.triples_main(original_text)#summary
        for svo in svo_result_list:
            triple_subject=svo[0]
            triple_object=svo[2]
            triple_subject_label=extractor.entity_annotation(triple_subject)
            if triple_subject_label=='动作':
                continue
            dic_svo = {}
            dic_svo['triple_subject']=triple_subject#主语
            dic_svo['triple_object'] = triple_object#宾语
            #实体标签识别
            dic_svo['triple_subject_label']=triple_subject_label#主语标签
            dic_svo['triple_object_label']=extractor.entity_annotation(triple_object)#宾语标签
            dic_svo['triple_verb']=svo[1]#动词
            dic_svo['original_text']=original_text#原文
            dic_svo['original_text_table']=table_name#原文表
            dic_svo['original_text_table_id']=record[0]#原文表的id
            if creat_triple_table(table_name_triple,dic_svo):#写进实体表
                print('写入一条记录')
            else:
                print('写入失败')
    print('完成了{}表的抽取和存储'.format(table))

#根据三元组创建图
for table in table_list:
    table_name_triple = "triple_{}".format(table)
    data=select_triple_table_neo4j(table_name_triple)
    for record in data:
        flag=creat_map(record)
        if  0==flag:
            print('创建失败:',record)
        elif 1==flag:
            print('写入一个关系')
    print('完成了{}表的图谱创建'.format(table))
print('end')

