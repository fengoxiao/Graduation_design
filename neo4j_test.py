# coding:utf-8
from py2neo import Graph, Node, Relationship,NodeMatcher
import pymysql
#连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='zw6262099', db='neo4j', charset='utf8')
##连接neo4j数据库，输入地址、用户名、密码
graph = Graph('http://localhost:7474', username='neo4j', password='zhongwei')

#清空数据库
#match (n) detach delete n

#创建游标
cursor = db.cursor()
sql="select * from pig"
cursor.execute(sql)
data = cursor.fetchall()
for record in data:
    pig_node = Node("pig", name=record[1],age=record[2])
    graph.create(pig_node)
sql="select * from relationship"
cursor.execute(sql)
data = cursor.fetchall()
matcher = NodeMatcher(graph)
# finded=matcher.match(name='佩奇').first()
# print(finded)
#dic={'n': (_117:pig {age: 10, name: '\u732a\u7238\u7238'})}
# buff=matcher.get(9)
# print(type(buff))

for record in data:
    from_name=graph.run("Match (n: pig) where n.name ='{}' return n".format(record[1])).data()[0]['n']
    to_name=graph.run("Match (n: pig) where n.name ='{}' return n".format(record[3])).data()[0]['n']

    # 两种方式都可以添加属性
    pig_relation = Relationship(from_name, record[2], to_name,name=record[3])
    pig_relation['count'] = 1
    graph.create(pig_relation)

db.close()
print('end')
'''
# 创建关系
# 分别建立了test_node_1指向test_node_2和test_node_2指向test_node_1两条关系，关系的类型为"丈夫、妻子"，两条关系都有属性count，且值为1。
node_1_zhangfu_node_1 = Relationship(test_node_1, '丈夫', test_node_2)
node_1_zhangfu_node_1['count'] = 1
node_2_qizi_node_1 = Relationship(test_node_2, '妻子', test_node_1)
node_2_munv_node_1 = Relationship(test_node_2, '母女', test_node_3)

node_2_qizi_node_1['count'] = 1


##创建关系
# 分别建立了test_node_1指向test_node_2和test_node_2指向test_node_1两条关系，关系的类型为"丈夫、妻子"，两条关系都有属性count，且值为1。
node_1_zhangfu_node_1 = Relationship(test_node_1, '丈夫', test_node_2)
node_1_zhangfu_node_1['count'] = 1
node_2_qizi_node_1 = Relationship(test_node_2, '妻子', test_node_1)
node_2_munv_node_1 = Relationship(test_node_2, '母女', test_node_3)

node_2_qizi_node_1['count'] = 1

graph.create(node_1_zhangfu_node_1)
graph.create(node_2_qizi_node_1)
graph.create(node_2_munv_node_1)

print(graph)
print(test_node_1)
print(test_node_2)
print(node_1_zhangfu_node_1)
print(node_2_qizi_node_1)
print(node_2_munv_node_1)
'''