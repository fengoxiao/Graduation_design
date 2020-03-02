#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql
#连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='zw6262099', db='HelloSea', charset='utf8')

#创建游标
cursor = db.cursor()

def retrieve_interface(sql):#查询
    cursor.execute(sql)
    data = cursor.fetchall()
    for record in data :
        print(record)
    db.close()
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

#truncate table 表名

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



