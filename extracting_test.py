#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from database_test import test_retrieve
from EventTriplesExtraction.triple_extraction import TripleExtractor

sql = "select news_title,news_summary from sea_news_domestic limit 5  "
data=test_retrieve(sql)
extractor = TripleExtractor()

pig_text = '''
    猪爷爷的年龄是15岁。猪奶奶的年龄是14岁。猪爸爸的年龄是10岁。猪妈妈的年龄是9岁。乔治的年龄是2岁。佩奇的年龄是1岁。
    猪爸爸和猪妈妈和乔治是家人。猪爷爷和猪奶奶的关系是夫妻。乔治和佩奇是姐弟。猪爷爷和猪爸爸是父子。猪爸爸和佩奇是父子。
    '''
pig_svo_list = extractor.triples_main(pig_text)
for pig_svo in pig_svo_list:
    print(pig_svo)
    #show_detail(pig_svo[0])
for count,record in enumerate(data):
    svo_title = extractor.triples_main(record[0])
    svo_summary = extractor.triples_main(record[1])
    print('{}:\n'.format(record[0]), svo_title)
    #show_detail(svo_title[0])
    print('{}:\n'.format(record[1]), svo_summary)
