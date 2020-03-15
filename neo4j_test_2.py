#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql
from database_test import creat_triple_table
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='zw6262099', db='neo4j', charset='utf8')
cursor = db.cursor()
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
# cursor.execute(sql, tuple(data.values()))
# sql="select * from {table} where {id} =%s and pig_age=%s".format(table='pig',id='id')
# cursor.execute(sql,(1,10))
# data = cursor.fetchall()
# for record in data:
#     print(record)
data = {
  'pig_name': 'Lily',
  'pig_age': 24
}
table = 'pig'
creat_triple_table(table,data)
'''
cursor.execute(sql)
data = cursor.fetchall()
for record in data:
    print(record)
'''
'''
sql = "INSERT INTO %s(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) VALUES(%s,%s,%s,%s,%s,%s,%s)"
try:
    cursor.execute(sql,(a,b,c,d,e,f,g))
    data = cursor.fetchone()
    #print(data)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
    result=False
# # 关闭数据库
# db.close()
'''