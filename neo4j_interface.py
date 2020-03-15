#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from py2neo import Graph, Node, Relationship,NodeMatcher

graph = Graph('http://localhost:7474', username='neo4j', password='zhongwei')

#matcher = NodeMatcher(graph)
# finded=matcher.match(name='佩奇').first()
# print(finded)
#dic={'n': (_117:pig {age: 10, name: '\u732a\u7238\u7238'})}
# buff=matcher.get(9)
# print(type(buff))

def creat_map(record):
    query_from_name=graph.run("Match (n: {}) where n.name ='{}' return n".format(record[2],record[1])).data()
    query_to_name=graph.run("Match (n: {}) where n.name ='{}' return n".format(record[5],record[4])).data()

    #print(query_to_name)
    # 两种方式都可以添加属性
    if not query_from_name:
        from_name = Node(record[2], name=record[1])
        graph.create(from_name)
    else:
        from_name=query_from_name[0]['n']
    if not query_to_name:
        to_name = Node(record[5], name=record[4])
        graph.create(to_name)
    else:
        to_name=query_to_name[0]['n']
    map_relation = Relationship(from_name, record[3], to_name)
    map_relation['original_text'] = record[6]
    map_relation['original_text_table'] = record[7]
    map_relation['original_text_table_id'] = record[8]
    graph.create(map_relation)