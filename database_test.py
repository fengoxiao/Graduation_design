#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql
#连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='zw6262099', db='HelloSea', charset='utf8')
db_neo4j = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='zw6262099', db='neo4j', charset='utf8')

#truncate table 表名
#创建游标
cursor = db.cursor()
cursor_neo4j = db_neo4j.cursor()

def creat_triple_table(table,data):
    result=True
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
        cursor_neo4j.execute(sql, tuple(data.values()))
        db_neo4j.commit()
    except:
        result=False
        db_neo4j.rollback()
    return result

def select_triple_table(table,keys):
    sql = "select {keys} from {table} limit 5".format(keys=', '.join(keys),table=table)
    cursor.execute(sql)
    data = cursor.fetchall()
    return data
def select_triple_table_neo4j(table):
    sql = "select * from {table}".format(table=table)
    cursor_neo4j.execute(sql)
    data = cursor_neo4j.fetchall()
    return data
'''
keys =('id','news_title','news_summary')
data=select_triple_table('sea_news_domestic',keys)
'''

'''
#变量查询
sql="select * from {table} where {id} =%s and pig_age=%s".format(table='pig',id='id')
cursor.execute(sql,(1,10))
data = cursor.fetchall()
for record in data:
    print(record)
'''
def creat_triple_table_test(table_name,keys,values):
    # sql = "select * from  where {id} =%s and pig_age=%s".format(table='pig', id='id')
    # cursor.execute(sql, (1, 10))
    # data = cursor.fetchall()
    #(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source)
    sql = "INSERT INTO {table_name}({keys}) VALUES (%s, %s)".format(table_name=table_name,keys=keys)
    result = True
    print(sql)
    try:
        print(values)
        cursor.execute(sql,values)
        #data = cursor.fetchone()
        db.commit()
        print('成功')
    except:
        db.rollback()
        result = False
        print('失败')

    return result

def test_retrieve(sql):#查询
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def retrieve_interface(sql):#查询
    cursor.execute(sql)
    data = cursor.fetchall()
    for record in data :
        print(record)
    return True

def create_interface(a,b,c,d,e,f,g):#创建
    sql = "INSERT INTO sea_news(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    result=True
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
    return result
#test
# sql="select news_web_url from sea_news_trave"
# retrieve_interface(sql)
# #关闭数据库
# db.close()
    # 执行 SQL 语句
    # sql = "select * from sea_news"
    # sql="INSERT INTO sea_news(news_title,news_type,news_date) \
    #     VALUES('test','test','2020-02-14')"
    # cursor.execute(sql)
    # fetchone() ：
    # 返回单个的元组，也就是一条记录(row)，如果没有结果，则返回None
    # fetchall() ：
    # 返回多个元组，即返回多个记录(rows), 如果没有结果则返回()

    #查表
    # data = cursor.fetchall()
    # for record in data :
    #     print(record)

    #插入
#     data = cursor.fetchone()
#     print(data)
#
#     # 提交修改
#     db.commit()
#     print('finish')
# except:
#     # 发生错误时回滚
#     db.rollback()
#     print('error')



