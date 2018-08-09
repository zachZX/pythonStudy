# -*- coding: UTF-8 -*-


import urllib
import urllib2
from bs4 import BeautifulSoup
import gifGet
import os


def htmlGet(url):
    pass
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    requst = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(requst)
    html = page.read()
    return html


def getNewSoup(html):
    pass
    soup = BeautifulSoup(html, 'lxml')
    return soup


def destroyEmpty(name):
    pass
    picNameList = []
    for i in range(len(name)):
        pass
        pic_name = name[i].get_text().encode('utf-8')
        if pic_name == '\n':
            pass
            print '长度不对'
        elif len(pic_name) == 0:
            pass
            print '空字符串'
        elif pic_name == '':
            pass
            print '空内容'
        else:
            picNameList.append(pic_name)
        if len(picNameList) == 121:
            pass
            picNameList.append('死神')
            picNameList.append('十月围城')
    return picNameList


def outPng(list):
    pass
    urlList = []

    for i in range(len(list)):
        pass
        img_url = list[i]['real_src']

        file_suffix = os.path.splitext(img_url)[1]
        if file_suffix == '.png':
            pass
            print '这是个表情'
        else:
            urlList.append(img_url)
    return urlList


def blogPic():
    pass
    html = htmlGet(
        'http://blog.sina.com.cn/s/blog_6a8297850102w3u1.html')
    soup = getNewSoup(html=html)
    all = soup.find_all('div', class_='articalContent')
    list = all[0].find_all('img')
    print len(list)
    name = all[0].find_all('span')

    # 去除无效字符串，加入被莫名去除的两项
    picNameList = destroyEmpty(name=name)

    urlList = outPng(list=list)

    for value in range(len(urlList)):
        pass
        # print '>>>一条内容'
        if len(name) > value:
            pass
            picName = str(value) + picNameList[value]
            img_url = urlList[value]
            print 'picname', picName
            print 'imgurl', img_url
            if value > 120:
                pass
                gifGet.saveImage(img_url, picName, 'webImage')


def sinaPic():
    pass
    html = htmlGet(
        'http: // k.sina.com.cn / article_6380372847_17c4cc36f0010043xr.html?from=joke')
    soup = getNewSoup(html=html)
    all = soup.find_all('div', class_='article')
    print all
    list = all[0].find_all('img')
    # print list
    for value in range(len(list)):
        pass
        print '>>>一条内容'
        img_url = list[value]['src']
        print 'imgurl', img_url
        picName = 'pic' + str(value)
        gifGet.saveImage(img_url, picName, 'sina_webImage')


def hnbangPic():
    pass
    print '开始采集hnbang页面'
    html = htmlGet(
        'http://hnbang.com/view/25447.html')
    soup = getNewSoup(html=html)
    print '获取到html数据'
    all = soup.find_all('article', class_='article-content')
    list = all[0].find_all('p')
    picList = all[0].find_all('img')
    nameList = []
    print '开始'
    for value in range(len(list)):
        pass
        name = list[value]
        text = name.get_text()
        if text:
            pass
            if value > 0:
                pass
                nameList.append(text.encode('utf-8'))
    for value in range(len(picList)):
        pass
        print '>>>一条内容'
        print picList[value]
        img_url = picList[value]['src']
        print 'imgurl', img_url
        picName = nameList[value]
        gifGet.saveImage(img_url, picName, 'hnbang_webImage')


blogPic()
