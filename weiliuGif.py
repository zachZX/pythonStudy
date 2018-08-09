# -*- coding: UTF-8 -*-
import gifGet

import os

url = 'https://dev-test-api-wechat-app-nddk.qinbaowan.cn/v1.0.0/Ktcys/Game/getQuestion'
data = {"app_id": "wx05938c4520e7473b",
        "token": "9132cd8cc52dcc62da2b048a3b72e45ab0b94aa3f3414a0e",
        "login_user_id": 2,
        "version_code": 1}
# print('传入data', data)
# html = gifGet.getHtml(url, data)
# dic = gifGet.htmlToDic(html)
# print dic
# gifGet.saveImage(
# 'https://static-nddk.faquange.com/images/m/index/redpack.gif', 'gifpic')

book = gifGet.getNewXlsBook()
sheet = gifGet.getNewSheetWithBook(book)
for value in range(1, 10):
    pass
    for value1 in range(1, 10):
        pass
        text = '第' + str(value) + '行第' + str(value1) + '列'
        print text
        gifGet.writeLine(sheet=sheet, row=value, colom=value1, text=text)
gifGet.bookSave(book, 'sheet_dir', 'test')
# filename = '{}{}{}{}'.format(
#     'sheet_dir', os.sep, 'test', '.xls')
# book = gifGet.getExitedBook(filename)
# sheet = gifGet.getSheetByIndex(book, 0)
# print sheet
# gifGet.writeLine(sheet=sheet, row=0, colom=4, text='新增数据')
# gifGet.showSheetRow(sheet, row=1)
# gifGet.bookSave(book, 'sheet_dir', 'test')
