#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from database_test import select_triple_table,creat_triple_table,select_triple_table_neo4j
from EventTriplesExtraction.triple_extraction import TripleExtractor
from neo4j_interface import creat_map

extractor = TripleExtractor()
table_list=['domestic']
for table in table_list:#读取表，抽取三元组
    #sql = "select id,news_title,news_summary from sea_news_{}".format(table)
    attribute_columns=('id','news_title','news_summary')#属性列
    table_name="sea_news_{}".format(table)
    table_name_triple="triple_{}".format(table)
    data=select_triple_table(table_name,attribute_columns)
    for record in data:
        original_text=record[1]
        svo_result_list = extractor.triples_main(original_text)#title
        if not svo_result_list:
            original_text=record[2]
            svo_result_list = extractor.triples_main(original_text)#summary
        for svo in svo_result_list:
            dic_svo = {}
            dic_svo['triple_subject']=svo[0]
            dic_svo['triple_object'] = svo[2]
            #实体标签识别
            dic_svo['triple_subject_label']='entity'
            dic_svo['triple_object_label']='entity'
            dic_svo['triple_verb']=svo[1]
            dic_svo['original_text']=original_text
            dic_svo['original_text_table']=table_name
            dic_svo['original_text_table_id']=record[0]
            creat_triple_table(table_name_triple,dic_svo)#写进实体表


#根据三元组创建图
for table in table_list:
    table_name_triple = "triple_{}".format(table)
    data=select_triple_table_neo4j(table_name_triple)
    for record in data:
        creat_map(record)

print('end')

