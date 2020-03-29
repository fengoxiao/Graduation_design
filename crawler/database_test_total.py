#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql
#连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='zw6262099', db='HelloSea', charset='utf8')

#创建游标
cursor = db.cursor()
#添加数据，表明，属性字典
def creat_sea_news(table,data):
    result=True
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
        cursor.execute(sql, tuple(data.values()))
        db.commit()
    except:
        result=False
        db.rollback()
    return result

def select_sea_news(table,url):
    sql = "select news_web_url from {table} where news_web_url ='{url}'".format(table=table,url=url)
    cursor.execute(sql)
    data = cursor.fetchall()
    if not data:#空
        return False
    return True

# result=select_sea_news('sea_news_domestic','http://www.hellosea.net//Economics/1/72876.html')
# print(result)
'''
#变量查询
sql="select * from {table} where {id} =%s and pig_age=%s".format(table='pig',id='id')
cursor.execute(sql,(1,10))
data = cursor.fetchall()
for record in data:
    print(record)
'''
def creat_table_v2(table):
    sql="""
    CREATE TABLE {table_name} (
      `id` int(10) NOT NULL AUTO_INCREMENT,
      `news_title` varchar(100) DEFAULT NULL COMMENT '标题',
      `news_type` varchar(10) DEFAULT NULL COMMENT '类型',
      `news_date` date DEFAULT NULL COMMENT '日期',
      `news_summary` varchar(100) DEFAULT NULL COMMENT '摘要',
      `news_content` text COMMENT '正文',
      `news_web_url` varchar(100) DEFAULT NULL COMMENT '网页URL',
      `news_source` varchar(100) DEFAULT 'http://www.hellosea.net' COMMENT '来源',
      PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;
        """.format(table_name=table)
    cursor.execute(sql)

def drop_table_v2(table):
    sql_drop="drop table {table_name}".format(table_name=table)
    cursor.execute(sql_drop)

def table_not_exists_v2(table):
    sql = "show tables"
    cursor.execute(sql)
    tables = cursor.fetchall()
    for record in tables:
        if table==record[0]:
            return False
    return True

#添加新闻,1=原表，2=v2
def select_sea_add_news(table1,table2):
    count=0
    sql = "select * from {table}".format(table=table1)
    cursor.execute(sql)
    data = cursor.fetchall()
    for record in data:
        news_content=record[5]
        if not news_content:
            continue
        url = record[6]
        if not select_sea_news(table2,url):
            news_dic = {}
            news_dic['news_title'] = record[1]
            news_dic['news_type'] = record[2]
            news_dic['news_date'] = record[3]
            news_dic['news_summary'] = record[4]
            news_dic['news_content'] = news_content
            news_dic['news_web_url'] = url
            news_dic['news_source'] = record[7]
            if creat_sea_news(table2, news_dic):
                count+=1
            else:
                print('填入失败！？')
    print('{}成功填入{}条新闻'.format(table2,count))


    return True

def retrieve_interface(sql):#查询
    cursor.execute(sql)
    data = cursor.fetchall()
    for record in data :
        print(record)
    db.close()
    return True

def edu_create_interface(a,b,c,d,e,f,g):#创建
    sql = "INSERT INTO sea_news_edu(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) VALUES(%s,%s,%s,%s,%s,%s,%s)"
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

def economics_create_interface(a,b,c,d,e,f,g):#创建
    sql = "INSERT INTO sea_news_economics(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) VALUES(%s,%s,%s,%s,%s,%s,%s)"
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

def mil_retrieve_interface(url):
    sql = "select news_web_url from sea_news_mil"
    cursor.execute(sql)
    data = cursor.fetchall()
    for record in data:
        if url==record[0]:
            return False
    return True



def mil_create_interface(a,b,c,d,e,f,g):#创建
    sql = "INSERT INTO sea_news_mil(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) VALUES(%s,%s,%s,%s,%s,%s,%s)"
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

def culture_create_interface(a,b,c,d,e,f,g):#创建
    sql = "INSERT INTO sea_news_culture(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) VALUES(%s,%s,%s,%s,%s,%s,%s)"
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

def tech_create_interface(a,b,c,d,e,f,g):#创建
    sql = "INSERT INTO sea_news_tech(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) VALUES(%s,%s,%s,%s,%s,%s,%s)"
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

def tech_retrieve_interface(url):
    sql = "select news_web_url from sea_news_tech"
    cursor.execute(sql)
    data = cursor.fetchall()
    for record in data:
        if url==record[0]:
            return False
    return True

def trave_create_interface(a,b,c,d,e,f,g):#创建
    sql = "INSERT INTO sea_news_trave(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) VALUES(%s,%s,%s,%s,%s,%s,%s)"
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

def cbhg_create_interface(a,b,c,d,e,f,g):#创建
    sql = "INSERT INTO sea_news_cbhg(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    result=True
    try:
        cursor.execute(sql,(a,b,c,d,e,f,g))
        db.commit()
    except:
        db.rollback()
        result=False
    return result

def cbhg_retrieve_interface(url):
    sql = "select news_web_url from sea_news_cbhg"
    cursor.execute(sql)
    data = cursor.fetchall()
    for record in data:
        if url==record[0]:
            return False
    return True

def trave_retrieve_interface(url):
    sql = "select news_web_url from sea_news_trave"
    cursor.execute(sql)
    data = cursor.fetchall()
    for record in data:
        if url==record[0]:
            return False
    return True

def international_create_interface(a,b,c,d,e,f,g):#创建
    sql = "INSERT INTO sea_news_international(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) VALUES(%s,%s,%s,%s,%s,%s,%s)"
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

def international_retrieve_interface(url):
    sql = "select news_web_url from sea_news_international"
    cursor.execute(sql)
    data = cursor.fetchall()
    for record in data:
        if url==record[0]:
            return False
    return True

def domestic_create_interface(a,b,c,d,e,f,g):#创建
    sql = "INSERT INTO sea_news_domestic(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) VALUES(%s,%s,%s,%s,%s,%s,%s)"
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

def domestic_retrieve_interface(url):
    sql = "select news_web_url from sea_news_domestic"
    cursor.execute(sql)
    data = cursor.fetchall()
    for record in data:
        if url==record[0]:
            return False
    return True