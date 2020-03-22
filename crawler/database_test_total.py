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