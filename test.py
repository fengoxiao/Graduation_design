#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql
#连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='zw6262099', db='HelloSea', charset='utf8')

#创建游标
cursor = db.cursor()
sql = "INSERT INTO sea_news_internation(news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source) select news_title,news_type,news_date,news_summary,news_content,news_web_url,news_source from sea_news_international"
try:
    cursor.execute(sql)
    data = cursor.fetchone()
    #print(data)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
    print('error')
#关闭数据库
# db.close()
