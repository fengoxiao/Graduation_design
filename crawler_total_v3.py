#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from lxml import html
import urllib.request
import re
import time
from database_crawler_total import creat_sea_news,select_sea_news
# 清理html标签
def clean_tag(string):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', string)
    return dd

#默认列表
'''
news_total={'domestic':{'News':{'2':['国内资讯',1,121]}},
            'international':{'News':{'3':['国际资讯',1,121]}},
            'cbhg':{'cbhg':{'news':['船舶海工',1,29],'news/1':['船舶海工',1,23]}},
            'culture':{'Culture':{'1':['历史文化',1,121]}},
            'economics':{'Economics':{'1':['蓝色经济',1,100]}},
            'edu':{'Edu':{'1':['教育资讯',1,62],'2':['海洋高校',1,41]}},
            'mil':{'Mil':{'1':['海洋军事',1,67],'4':['海洋军事',1,66]}},
            'tech':{'Tech':{'1':['海洋通讯',1,12],'3':['互联网+海洋',1,6],'4':['高新技术',1,84],'5':['生物技术',1,10]}},
            'trave':{'Trave':{'2':['海洋旅游',1,100]}}
            }
'''
#实际列表
news_total={'domestic':{'News':{'2':['国内资讯',1,121]}},
            'international':{'News':{'3':['国际资讯',1,121]}},
            'cbhg':{'cbhg':{'news':['船舶海工',1,29],'news/1':['船舶海工',1,23]}},
            'culture':{'Culture':{'1':['历史文化',1,121]}},
            'economics':{'Economics':{'1':['蓝色经济',79,100]}},
            'edu':{'Edu':{'1':['教育资讯',1,62],'2':['海洋高校',1,41]}},
            'mil':{'Mil':{'1':['海洋军事',1,67],'4':['海洋军事',1,66]}},
            'tech': {'Tech': {'1': ['海洋通讯', 1, 12], '3': ['互联网+海洋', 1, 6], '4': ['高新技术', 1, 84], '5': ['生物技术', 1, 10]}},
            'trave':{'Trave':{'2':['海洋旅游',1,100]}}
            }
url_start='http://www.hellosea.net/{url_level_1}/{url_level_2}/index_{page}.html'
url_start_first='http://www.hellosea.net/{url_level_1}/{url_level_2}/'
for key_level_1,value_level_1 in news_total.items():
    count=0
    table_name="sea_news_{}_v2".format(key_level_1)#v2表
    #table_name="sea_news_{}".format(key_level_1)#原表

    #更新的时候注释掉这段
    # if not table_not_exists_v2(table_name):
    #     drop_table_v2(table_name)
    #     print('删除{}表成功'.format(table_name))
    # creat_table_v2(table_name)
    # print('创建{}表成功'.format(table_name))
    # 更新的时候注释掉这段

    url_level_1=[key for key in value_level_1.keys()][0]
    value_level_2=[key for key in value_level_1.values()][0]
    print(value_level_2)
    for key_level_3,value_level_3 in value_level_2.items():
        url_level_2=key_level_3
        #上下限
        news_type,page_star,page_ceiling=value_level_3
        for page in range(page_star, page_ceiling):
            if page == 1:
                url = url_start_first.format(url_level_1=url_level_1,url_level_2=url_level_2)
            else:
                url = url_start.format(url_level_1=url_level_1,url_level_2=url_level_2,page=page)
            try:
                response = requests.get(url)
                string = response.text
                element = html.fromstring(string)
                news_list = element.xpath('//div[@class="left-lbzw"]/div')
                for news in news_list:
                    #news_web_url='http://www.hellosea.net/'+news.xpath('./a/@href')[0]
                    news_web_url = news.xpath('./a/@href')[0]
                    # 新方法
                    if select_sea_news(table_name,news_web_url):
                        print('该新闻已存在','跳过该{}，二级网址为{}'.format(url_level_1,url_level_2))
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

                    news_dic={}
                    news_dic['news_title']=news_title
                    news_dic['news_type']=news_type
                    news_dic['news_date']=news_date
                    news_dic['news_summary']=news_summary
                    news_dic['news_content']=news_content
                    news_dic['news_web_url']=news_web_url
                    news_dic['news_source']=news_source
                    print(news_title,':',news_web_url)
                    time.sleep(1)
                    if creat_sea_news(table_name,news_dic):
                        count+=1
                        print('第{}页，{}第{}个新闻爬取成功'.format(page,table_name,count))
                    else:
                        print('存储失败!第{}页{}的新闻'.format(page,table_name))
                    time.sleep(4)
            except requests.exceptions.ConnectionError as e:
                print('{}第{}页新闻网址异常：{}'.format(table_name,page,url),e)
            except BaseException as e:
                print('{}第{}页爬取异常：'.format(table_name, page), e)
            time.sleep(20)
            print('{}第{}页新闻爬取完成'.format(table_name,page))
        if count>1000:
            break
    print('{}的新闻finish!!!'.format(table_name))

#开始今日热点
url='http://www.hellosea.net/'
table_name="sea_news_{}_v2".format('todayhot')
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


