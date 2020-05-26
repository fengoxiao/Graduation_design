#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
接口说明：
punctuation_remove(entity):去实体中除无意义的符号
duplicate_removal_svo(svo_list):去除三元组列表中重复的三元组
creat_map(record):将记录写入图中
user_name=用户名
pass_word=密码

'''
from py2neo import Graph, Node, Relationship,RelationshipMatcher
#NodeMatcher导入无用
import re
user_name='neo4j'
pass_word='zhongwei'
graph = Graph('http://localhost:7474', username=user_name, password=pass_word)

#matcher = NodeMatcher(graph)
# finded=matcher.match(name='佩奇').first()
# print(finded)
#dic={'n': (_117:pig {age: 10, name: '\u732a\u7238\u7238'})}
# buff=matcher.get(9)
# print(type(buff))
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
def select_node(node_label='',node_name='',node_limit=1):
    result=[]
    if not node_label:
        cql='Match (n) where n.name ="{}" return n,n.name  LIMIT {}'.format(node_name,node_limit)
    elif not node_name:
        cql='Match (n:{})  return n,n.name LIMIT {}'.format(node_label,node_limit)
    else:
        cql='Match (n:{}) where n.name ="{}" return n,n.name  LIMIT {}'.format(node_label,node_name,node_limit)
    data_list=graph.run(cql).data()
    if  data_list:
        for data in data_list:
            tip_string=','.join(data['n']._labels)+':'+data['n.name']
            result.append(tip_string)
    return result
#select_node(node_label='事件',node_limit=20)
'''
#model:默认为3，1：正向查询，2：反向查询，3：无方向查询，4：具体查询，5：查谓语
#node_label:实体标签
#object_label:宾语标签
#node_name:实体名称
#object_name:宾语名称
#relation:关系名称
#node_limit:输出数量，默认为5
返回二层列表
#示例：
data=select_relation(node_name='日本政府',relation='为主')
for record in data:
    for detail in record:
        print(detail)
#select_relation(model=4,node_label='机构',node_name='日本政府',object_name='以安防',object_label='名词',relation='为主')
'''
def select_relation(model=3,node_label='',node_name='',relation='',node_limit=5,object_label='',object_name=''):
    if relation : relation=':%s'%(relation)
    if node_label : node_label=':%s'%(node_label)
    if object_label : object_label=':%s'%(object_label)
    result = []
    if model==1:
        cql = 'Match (n%s)-[r%s]->(m) where n.name="%s" return type(r),r.original_text,r.original_text_table,r.original_text_table_id,n,m,m.name LIMIT %s' % (node_label,relation,node_name,node_limit)
        #print(cql)
        data_list = graph.run(cql).data()
        if  data_list:
            for data in data_list:
                buff=[]
                buff.append(data['r.original_text_table'])
                buff.append(data['r.original_text_table_id'])
                buff.append(data['r.original_text'])
                tip_string=','.join(data['n']._labels)+':'+node_name+' -- ['
                if not relation :
                    tip_string+=data['type(r)']
                else:
                    tip_string+=relation[1:]
                tip_string+='] -> '+','.join(data['m']._labels)+ ':'+ data['m.name']
                buff.append(tip_string)
                result.append(buff)
    elif model==2:
        cql = 'Match (n%s)<-[r%s]-(m) where n.name="%s" return type(r),r.original_text,r.original_text_table,r.original_text_table_id,m,n,m.name LIMIT %s' % (
        node_label, relation, node_name, node_limit)
        # print(Cypher_sql)
        data_list = graph.run(cql).data()
        if data_list:
            for data in data_list:
                buff = []
                buff.append(data['r.original_text_table'])
                buff.append(data['r.original_text_table_id'])
                buff.append(data['r.original_text'])
                tip_string = ','.join(data['n']._labels) + ':' + node_name + ' <- ['
                if not relation:
                    tip_string += data['type(r)']
                else:
                    tip_string += relation[1:]
                tip_string += '] -- ' + ','.join(data['m']._labels) + ':' + data['m.name']
                buff.append(tip_string)
                result.append(buff)
    elif model==3:
        cql = 'Match (n%s)-[r%s]-(m) where n.name="%s" return type(r),r.original_text,r.original_text_table,r.original_text_table_id,n,m,m.name LIMIT %s' % (
        node_label, relation, node_name, node_limit)
        # print(Cypher_sql)
        data_list = graph.run(cql).data()
        if data_list:
            for data in data_list:
                buff = []
                buff.append(data['r.original_text_table'])
                buff.append(data['r.original_text_table_id'])
                buff.append(data['r.original_text'])
                tip_string = ','.join(data['n']._labels) + ':' + node_name + ' -- ['
                if not relation:
                    tip_string += data['type(r)']
                else:
                    tip_string += relation[1:]
                tip_string += '] -- ' + ','.join(data['m']._labels) + ':' + data['m.name']
                buff.append(tip_string)
                result.append(buff)
    elif model==4:
        cql='Match (n%s)-[r%s]->(m%s) where n.name="%s"and m.name="%s" return r.original_text,r.original_text_table,r.original_text_table_id,m'%(node_label,relation,object_label,node_name,object_name)
        data_list = graph.run(cql).data()
        if data_list:
            relation = relation[1:]
            node_label = node_label[1:]
            object_label = object_label[1:]
            for data in data_list:
                buff = []
                buff.append(data['r.original_text_table'])
                buff.append(data['r.original_text_table_id'])
                buff.append(data['r.original_text'])
                tip_string=node_label+ ':'+ node_name+' -- ['+ relation+ '] -> '+ object_label+ ':'+object_name
                buff.append(tip_string)
                result.append(buff)
    elif model==5:
        cql = 'Match (n)-[r%s]-(m)  return type(r),r.original_text,r.original_text_table,r.original_text_table_id,n,n.name,m,m.name LIMIT %s' % (
        relation,  node_limit)
        # print(Cypher_sql)
        data_list = graph.run(cql).data()
        if  data_list:
            for data in data_list:
                buff = []
                buff.append(data['r.original_text_table'])
                buff.append(data['r.original_text_table_id'])
                buff.append(data['r.original_text'])
                tip_string = ','.join(data['n']._labels) + ':' + data['n.name'] + ' -- ['
                if not relation:
                    tip_string += data['type(r)']
                else:
                    tip_string += relation[1:]
                tip_string += '] -- ' + ','.join(data['m']._labels) + ':' + data['m.name']
                buff.append(tip_string)
                result.append(buff)
    return result
#select_relation(model=4,node_label='机构',node_name='日本政府',object_name='以安防',object_label='名词',relation='为主')
'''
data=select_relation(node_name='日本政府',relation='为主')
for record in data:
    for detail in record:
        print(detail)
'''
#select_relation(model=1,node_label='机构',node_name='日本政府')
#select_relation(model=5,node_label='机构',node_name='日本政府')



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