#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from py2neo import Graph, Node, Relationship
#NodeMatcher导入无用
import re
graph = Graph('http://localhost:7474', username='neo4j', password='zhongwei')

#matcher = NodeMatcher(graph)
# finded=matcher.match(name='佩奇').first()
# print(finded)
#dic={'n': (_117:pig {age: 10, name: '\u732a\u7238\u7238'})}
# buff=matcher.get(9)
# print(type(buff))

def creat_map(record):
    subject_name=record[1]
    original_subject_label = record[2]
    relation_verb=record[3]
    object_name = record[4]
    original_object_label = record[5]
    try:
        query_from_name=graph.run('Match (n) where n.name ="{}" return n'.format(subject_name)).data()
        query_to_name=graph.run('Match (n) where n.name ="{}" return n'.format(object_name)).data()
    except:
        # print(subject_name)
        # print(subject_name)
        return 0
    #print(query_to_name)
    # 两种方式都可以添加属性
    if not query_from_name:
        from_name = Node(original_subject_label, name=subject_name)
        graph.create(from_name)
    else:
        from_name=query_from_name[0]['n']
        if not from_name.has_label(original_subject_label):
            from_name.add_label(original_subject_label)  # 增加label

    if not query_to_name:
        to_name = Node(original_object_label, name=object_name)
        graph.create(to_name)
    else:
        to_name=query_to_name[0]['n']
        if not to_name.has_label(original_object_label):
            to_name.add_label(original_object_label)  # 增加label
    try:
        Cypher_sql='Match (n:%s)-[:%s]->(m:%s) where n.name="%s"and m.name="%s" return m'%(original_subject_label,relation_verb,original_object_label,subject_name,object_name)
        # print(Cypher_sql)
        relation_exist=graph.run(Cypher_sql).data()
    except:
        return 0
    if  not relation_exist:
        map_relation = Relationship(from_name, relation_verb, to_name)
        map_relation['original_subject_label'] = original_subject_label
        map_relation['original_object_label'] = original_object_label
        map_relation['original_text'] = record[6]
        map_relation['original_text_table'] = record[7]
        map_relation['original_text_table_id'] = record[8]
        graph.create(map_relation)
        return 1
    return 2

def duplicate_removal_svo(svo_list):
    #svo_list = [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'd']]
    result = []
    for svo_i in svo_list:
        flag = True
        for svo in result:
            if svo[1] == svo_i[1] and svo[0] == svo_i[0] and svo[2] == svo_i[2]:
                flag = False
                break
        if flag:
            result.append(svo_i)
    return result

def punctuation_remove(entity):
    return re.sub(r'[^\w\s]', '',entity)