import re
import urllib.request
import requests
from lxml import html
# 清理html标签
def clean_tag(string):
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', string)
    return dd

# 读取主网页，匹配子网页的地址
date = urllib.request.urlopen("http://www.hellosea.net/").read().decode("utf-8", "ignore")
pat1 = '<a href=".*" target="_blank" title=".*".*>.*</a>'
rst1 = re.compile(pat1).findall(date)
count=0
#读取子网页，匹配子网页新闻中的标题，摘要，内容，并且写入txt文件中
for x in rst1:
    url1 = "http://www.hellosea.net" + x
    print(url1)
    count+=1
    try:
        response = urllib.request.urlopen(url1).read().decode("utf-8", "ignore")
        element = html.fromstring(response)
        news_title = element.xpath('//h1[@id = "h1title"]/text()')
        if news_title:
            news_summary=clean_tag(element.xpath('//div[@class="summary"]/text()')[0])
            print(news_title[0])
            print(news_summary)
            news_content_list=element.xpath('//div[@id="text"]/p')
            news_content=''
            for content in news_content_list:
                string=content.xpath('./text()')
                if string:
                    news_content+=clean_tag(string[0])[2:]
            #print(news_content)
            # 创建txt，地址可自行设置
            with open (r"C:\Users\ZW\Desktop\test\hellosea.txt", "a") as fh:
                #print(news_title + ',' + news_summary + ',' + clean_tag(news_content) + '\n')
                fh.write('    ' + news_title[0] + ',' + news_summary + ',' + clean_tag(news_content) + '\n')
    except:
        print('空白网页')
print('end')
print(count)




