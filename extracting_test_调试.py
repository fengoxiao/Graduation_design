#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from database_test import test_retrieve_neo4j
from EventTriplesExtraction.triple_extraction import TripleExtractor
from neo4j_interface import punctuation_remove

sql = "select triple_subject,triple_object from triple_culture   "
data=test_retrieve_neo4j(sql)
extractor = TripleExtractor()
sting="fdsaf'sdf"
sting2='fdsaf"sdf'
svo_subject = punctuation_remove(sting)
if not svo_subject:
    print('空白：',sting)
else:
    print('{}:'.format(sting), svo_subject)
svo_subject = extractor.punctuation_remove(sting2)
if not svo_subject:
    print('空白：',sting2)
else:
    print('{}:'.format(sting2), svo_subject)
for record in data:
    svo_subject = extractor.punctuation_remove(record[0])
    if not svo_subject:
        print('空白：',record[0])
    else:
        print('{}:'.format(record[0]), svo_subject)
    svo_object = extractor.punctuation_remove(record[1])
    if not svo_object:
        print('空白：', record[1])
    else:
        print('{}:'.format(record[1]), svo_object)


    #show_detail(svo_title[0])
    print('{}:'.format(record[1]), svo_object)
