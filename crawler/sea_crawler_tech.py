#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from lxml import html
import urllib.request
import re
import time
from crawler.database_test_total import tech_create_interface,tech_retrieve_interface
# 清理html标签
def clean_tag(string):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', string)
    return dd
'''
count=0
url_start='http://www.hellosea.net/Tech/1/index_{}.html'
#http://www.hellosea.net/Edu/1/index_60.html
for page in range(1,13):
    try:
        if page==1:
            url='http://www.hellosea.net/Tech/1/'
        else:
            url = url_start.format(page)
        response = requests.get(url)
        string = response.text
        element = html.fromstring(string)
        # response= urllib.request.urlopen(url).read().decode("utf-8", "ignore")
        # element = html.fromstring(response)
        news_list = element.xpath('//div[@class="left-lbzw"]/div')
        for news in news_list:
            news_web_url='http://www.hellosea.net/'+news.xpath('./a/@href')[0]
            #新方法
            if not tech_retrieve_interface(news_web_url):
                continue
            child_response = urllib.request.urlopen(news_web_url).read().decode("utf-8", "ignore")
            child_element = html.fromstring(child_response)
            buff=child_element.xpath('//div[@class="ep-content-main"]')[0]
            news_title=buff.xpath('./h1/text()')[0]
            date_and_source=buff.xpath('.//div[@class="fl col6"]/text()')[0]
            news_date=date_and_source[:10]
            news_source=date_and_source.split('来源: ')[1].split('　作者:')[0]
            buff=child_element.xpath('//div[@class="bd"]')[0]
            news_summary=buff.xpath('./div[@class="summary"]/text()')[0][3:]
            news_content_list=buff.xpath('./div[@id="text"]/p')
            news_content = ''
            for content in news_content_list:
                string = content.xpath('./text()')
                if string:
                    news_content += clean_tag(string[0])[2:]
            # print(news_title)
            # print(news_date)
            # print(news_summary)
            # print(news_content)
            # print(news_web_url)
            # print(news_source)
            if not news_content:
                continue
            if tech_create_interface(news_title,'海洋通讯',news_date,news_summary,news_content,news_web_url,news_source):
                count+=1
                print('第{}个新闻'.format(count))
            time.sleep(5)
    except:
        print('异常')
        pass
    time.sleep(20)
    print('第{}页完成'.format(page))
count=0
url_start='http://www.hellosea.net/Tech/3/index_{}.html'
#http://www.hellosea.net/Edu/1/index_60.html
for page in range(1,7):
    try:
        if page==1:
            url='http://www.hellosea.net/Tech/3/'
        else:
            url = url_start.format(page)
        response = requests.get(url)
        string = response.text
        element = html.fromstring(string)
        # response= urllib.request.urlopen(url).read().decode("utf-8", "ignore")
        # element = html.fromstring(response)
        news_list = element.xpath('//div[@class="left-lbzw"]/div')
        for news in news_list:
            news_web_url='http://www.hellosea.net/'+news.xpath('./a/@href')[0]
            #新方法
            if not tech_retrieve_interface(news_web_url):
                continue
            child_response = urllib.request.urlopen(news_web_url).read().decode("utf-8", "ignore")
            child_element = html.fromstring(child_response)
            buff=child_element.xpath('//div[@class="ep-content-main"]')[0]
            news_title=buff.xpath('./h1/text()')[0]
            date_and_source=buff.xpath('.//div[@class="fl col6"]/text()')[0]
            news_date=date_and_source[:10]
            news_source=date_and_source.split('来源: ')[1].split('　作者:')[0]
            buff=child_element.xpath('//div[@class="bd"]')[0]
            news_summary=buff.xpath('./div[@class="summary"]/text()')[0][3:]
            news_content_list=buff.xpath('./div[@id="text"]/p')
            news_content = ''
            for content in news_content_list:
                string = content.xpath('./text()')
                if string:
                    news_content += clean_tag(string[0])[2:]
            # print(news_title)
            # print(news_date)
            # print(news_summary)
            # print(news_content)
            # print(news_web_url)
            # print(news_source)
            if not news_content:
                continue
            if tech_create_interface(news_title,'互联网+海洋',news_date,news_summary,news_content,news_web_url,news_source):
                count+=1
                print('第{}个新闻'.format(count))
            time.sleep(5)
    except:
        print('异常')
        pass
    time.sleep(20)
    print('第{}页完成'.format(page))

count=0
url_start='http://www.hellosea.net/Tech/4/index_{}.html'
#http://www.hellosea.net/Edu/1/index_60.html
for page in range(1,84):
    try:
        if page==1:
            url='http://www.hellosea.net/Tech/4/'
        else:
            url = url_start.format(page)
        response = requests.get(url)
        string = response.text
        element = html.fromstring(string)
        # response= urllib.request.urlopen(url).read().decode("utf-8", "ignore")
        # element = html.fromstring(response)
        news_list = element.xpath('//div[@class="left-lbzw"]/div')
        for news in news_list:
            news_web_url='http://www.hellosea.net/'+news.xpath('./a/@href')[0]
            #新方法
            if not tech_retrieve_interface(news_web_url):
                continue
            child_response = urllib.request.urlopen(news_web_url).read().decode("utf-8", "ignore")
            child_element = html.fromstring(child_response)
            buff=child_element.xpath('//div[@class="ep-content-main"]')[0]
            news_title=buff.xpath('./h1/text()')[0]
            date_and_source=buff.xpath('.//div[@class="fl col6"]/text()')[0]
            news_date=date_and_source[:10]
            news_source=date_and_source.split('来源: ')[1].split('　作者:')[0]
            buff=child_element.xpath('//div[@class="bd"]')[0]
            news_summary=buff.xpath('./div[@class="summary"]/text()')[0][3:]
            news_content_list=buff.xpath('./div[@id="text"]/p')
            news_content = ''
            for content in news_content_list:
                string = content.xpath('./text()')
                if string:
                    news_content += clean_tag(string[0])[2:]
            # print(news_title)
            # print(news_date)
            # print(news_summary)
            # print(news_content)
            # print(news_web_url)
            # print(news_source)
            if not news_content:
                continue
            if tech_create_interface(news_title,'高新技术',news_date,news_summary,news_content,news_web_url,news_source):
                count+=1
                print('第{}个新闻'.format(count))
            time.sleep(5)
    except:
        print('异常')
        pass
    time.sleep(20)
    print('第{}页完成'.format(page))
'''
count=0
url_start='http://www.hellosea.net/Tech/5/index_{}.html'
#http://www.hellosea.net/Edu/1/index_60.html
for page in range(1,10):
    try:
        if page==1:
            url='http://www.hellosea.net/Tech/5/'
        else:
            url = url_start.format(page)
        response = requests.get(url)
        string = response.text
        element = html.fromstring(string)
        # response= urllib.request.urlopen(url).read().decode("utf-8", "ignore")
        # element = html.fromstring(response)
        news_list = element.xpath('//div[@class="left-lbzw"]/div')
        for news in news_list:
            news_web_url='http://www.hellosea.net/'+news.xpath('./a/@href')[0]
            #新方法
            if not tech_retrieve_interface(news_web_url):
                continue
            child_response = urllib.request.urlopen(news_web_url).read().decode("utf-8", "ignore")
            child_element = html.fromstring(child_response)
            buff=child_element.xpath('//div[@class="ep-content-main"]')[0]
            news_title=buff.xpath('./h1/text()')[0]
            date_and_source=buff.xpath('.//div[@class="fl col6"]/text()')[0]
            news_date=date_and_source[:10]
            news_source=date_and_source.split('来源: ')[1].split('　作者:')[0]
            buff=child_element.xpath('//div[@class="bd"]')[0]
            news_summary=buff.xpath('./div[@class="summary"]/text()')[0][3:]
            news_content_list=buff.xpath('./div[@id="text"]/p')
            news_content = ''
            for content in news_content_list:
                string = content.xpath('./text()')
                if string:
                    news_content += clean_tag(string[0])[2:]
            # print(news_title)
            # print(news_date)
            # print(news_summary)
            # print(news_content)
            # print(news_web_url)
            # print(news_source)
            if not news_content:
                continue
            if tech_create_interface(news_title,'生物技术',news_date,news_summary,news_content,news_web_url,news_source):
                count+=1
                print('第{}个新闻'.format(count))
            time.sleep(5)
    except:
        print('异常')
        pass
    time.sleep(20)
    print('第{}页完成'.format(page))