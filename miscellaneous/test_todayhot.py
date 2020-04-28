#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from lxml import html
import urllib.request
import re
import time
from database_crawler_total import creat_sea_news,select_sea_news,table_not_exists_v2,creat_table_v2
# 清理html标签
def clean_tag(string):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', string)
    return dd
#开始今日热点
url='http://www.hellosea.net/'
table_name="sea_news_{}_v2".format('TodayHot')
'''
if table_not_exists_v2(table_name):
    creat_table_v2(table_name)
    print('创建{}表成功'.format(table_name))
'''
count=0
try:
    response = requests.get(url)
    string = response.text
    element = html.fromstring(string)
    news_list=[]
    Today_Hot = element.xpath('//div[@id="bd_headline"]/div[@class="atom-editor"]')
    Today_Hot_ul = element.xpath('//div[@id="bd_headline"]/ul')
    for news in Today_Hot:
        # news_web_url='http://www.hellosea.net/'+news.xpath('./a/@href')[0]
        news_list.append(news.xpath('./p/a/@href')[0])
    for news in Today_Hot_ul:
        p_list= news.xpath('./p')
        for p in p_list:
            news_list.append(p.xpath('./a/@href')[0])
    for news_web_url in news_list:
        # 新方法
        if select_sea_news(table_name, news_web_url):
            print('该今日热点新闻已存在')
            continue
        child_response = urllib.request.urlopen(news_web_url).read().decode("utf-8", "ignore")
        child_element = html.fromstring(child_response)
        buff = child_element.xpath('//div[@class="bd"]')[0]
        news_content_list = buff.xpath('./div[@id="text"]/p')
        news_content = ''
        for content in news_content_list:
            string = content.xpath('./text()')
            if string:
                news_content += clean_tag(string[0])[2:]
        if not news_content:
            print('该新闻正文为空，跳过{}'.format(news_web_url))
            continue
        news_summary = buff.xpath('./div[@class="summary"]/text()')[0][3:]
        buff = child_element.xpath('//div[@class="ep-content-main"]')[0]
        news_title = buff.xpath('./h1/text()')[0]
        date_and_source = buff.xpath('.//div[@class="fl col6"]/text()')[0]
        news_date = date_and_source[:10]
        news_source = date_and_source.split('来源: ')[1].split('　作者:')[0]

        news_dic = {}
        news_dic['news_title'] = news_title
        news_dic['news_type'] = '今日热点'
        news_dic['news_date'] = news_date
        news_dic['news_summary'] = news_summary
        news_dic['news_content'] = news_content
        news_dic['news_web_url'] = news_web_url
        news_dic['news_source'] = news_source
        print(news_title, ':', news_web_url)
        time.sleep(1)
        if creat_sea_news(table_name, news_dic):
            count += 1
            print('第{}个热点新闻爬取成功'.format(count))
        else:
            print('该热点新闻存储失败!')
        time.sleep(4)
except requests.exceptions.ConnectionError as e:
    print('第{}个热点新闻网址异常：{}'.format(count, url), e)
except BaseException as e:
    print('第{}个热点新闻爬取异常：'.format(count), e)
print('今日热点新闻爬取完成')

print('全部完成')