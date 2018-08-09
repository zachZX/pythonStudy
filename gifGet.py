
# -*- coding: UTF-8 -*-
import re
import urllib
import urllib2
import json
import os


# 获取json或网页HTML数据
def getHtml(url, data={}, header={}):
    u"""获取url中的数据

    url,data,headers"""

    pass
    print '原始data', data
    data = urllib.urlencode(data)
    requst = urllib2.Request(url, headers=header)
    page = urllib2.urlopen(requst, data)
    html = page.read()

    return html


def htmlToDic(html):
    pass
    dic = json.loads(html)
    return dic

# 保存一张网络图片到本地


def saveImage(image_url, file_name, dir_path='test_image'):
    pass
    try:
        if not os.path.exists(dir_path):
            pass
            print '文件夹', dir_path, '不存在，创建一个'
            os.makedirs(dir_path)
        # 获取图片后缀
        # splitext 方法会将文件名和后缀分开
        file_suffix = os.path.splitext(image_url)[1]
        if len(file_suffix) == 0:
            pass
            file_suffix = '.gif'
        # 下载文件保存到指定位置
        print '图片后缀', file_suffix
        filename = '{}{}{}{}'.format(dir_path, os.sep, file_name, file_suffix)
        print '完整路径', filename
        urllib.urlretrieve(image_url, filename=filename)
    except IOError as e:
        print '文件操作失败', e
    except Exception as e:
        print '错误', e


getHtml('http://admin-link.like-xinbaby.top/data/modules/log/task_log.php?do=viewUUID&master_user_id=100089170')
