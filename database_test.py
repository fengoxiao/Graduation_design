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
    sql = "select {keys} from {table}".format(keys=', '.join(keys),table=table)
    #sql = "select {keys} from {table} limit 5".format(keys=', '.join(keys),table=table)
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def record_had_extracting(triple_table,original_text_table,original_text_table_id):
    sql="select original_text_table_id from {triple_table} where original_text_table='{original_text_table}' and original_text_table_id={original_text_table_id}".format(triple_table=triple_table,original_text_table=original_text_table,original_text_table_id=original_text_table_id)
    cursor_neo4j.execute(sql)
    data = cursor_neo4j.fetchall()
    if not data:  # 空
        return False
    return True

def neo4j_select_triple_table(table,keys):
    sql = "select {keys} from {table} limit 100".format(keys=', '.join(keys),table=table)
    #sql = "select {keys} from {table} limit 5".format(keys=', '.join(keys),table=table)
    cursor_neo4j.execute(sql)
    data = cursor_neo4j.fetchall()
    return data

def select_triple_table_neo4j(table):
    sql = "select * from {table}".format(table=table)
    cursor_neo4j.execute(sql)
    data = cursor_neo4j.fetchall()
    return data

def creat_table_neo4j(table):
    sql="""
    CREATE TABLE IF NOT EXISTS {table_name} (
          `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '索引',
          `triple_subject` varchar(100) DEFAULT NULL COMMENT '主语',
          `triple_subject_label` varchar(100) DEFAULT NULL COMMENT '主语标签',
          `triple_verb` varchar(100) DEFAULT NULL COMMENT '动词',
          `triple_object` varchar(100) DEFAULT NULL COMMENT '宾语',
          `triple_object_label` varchar(100) DEFAULT NULL COMMENT '宾语标签',
          `original_text` varchar(100) DEFAULT NULL COMMENT '原文',
          `original_text_table` varchar(100) DEFAULT NULL COMMENT '原文的表',
          `original_text_table_id` int(10) DEFAULT NULL COMMENT '原文的表的id',
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
        """.format(table_name=table)
    cursor_neo4j.execute(sql)

def truncate_table_neo4j(table):
    sql_truncate="truncate table {table_name}".format(table_name=table)
    cursor_neo4j.execute(sql_truncate)



def table_not_exists(table):
    sql = "show tables"
    cursor_neo4j.execute(sql)
    tables = cursor_neo4j.fetchall()
    for record in tables:
        if table==record[0]:
            return False
    return True

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



