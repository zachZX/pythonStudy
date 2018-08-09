# -*- coding: UTF-8 -*-

import os
import xlwt
import xlrd
from xlutils.copy import copy
# 创建一个workbook对象，相当于创建了一个excel文件


def getNewXlsBook():

    book = xlwt.Workbook(encoding='utf-8')
    return book


# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
# 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
def getNewSheetWithBook(book):
    pass
    sheet = book.add_sheet('test', cell_overwrite_ok=True)
    return sheet

# 向表test中添加数据
# 其中的'row-行, colom-列'指定表中的单元，text是向该单元写入的内容


def writeLine(sheet, row, colom, text):
    pass
    sheet.write(row, colom, text.decode('utf-8'))


# 获取一个已存在得Excel文件得book对象
def getExitedBook(file_name):
    pass
    book = xlrd.open_workbook(file_name)
    return book

# 获取表得一整行内容


def showSheetRow(sheet, row):
    pass
    rowMsg = sheet.row_values(row)
    for value in rowMsg:
        pass
        print value.encode("utf-8")
    #     print json.dumps(value, encoding='UTF-8', ensure_ascii=False)

    return sheet.row_values(row)

# 获取一整列表得数据


def showSheetColom(sheet, colom):
    pass
    print sheet.col_values(colom)
    ncols = sheet.ncols  # 获取列总数
    print ncols

# 获取对应单元格得数据


def getSheetRowColPar(sheet, row, colom):
    pass
    # 通过坐标读取表格中的数据
    cell_value1 = sheet.cell_value(row, colom)
    print cell_value1


# 获取对应index的sheet


def getSheetByIndex(book, index):
    pass
    sheet = book.sheet_by_index(index)
    return sheet
# 保存excal表格


def bookSave(book, dir_path, file_name):
    pass
    try:
        if not os.path.exists(dir_path):
            pass
            print '文件夹', dir_path, '不存在，创建一个'
            os.makedirs(dir_path)
        filename = '{}{}{}{}'.format(
            dir_path, os.sep, file_name, '.xls')
        print '完整路径', filename
        book.save(filename)
    except IOError as e:
        print '文件操作失败', e
    except Exception as e:
        print '错误', e


def xlcWrite():
    pass
    # 创建一个workbook对象，相当于创建了一个excel文件
    book = xlwt.Workbook(encoding='utf-8')
    #     '''
    # Workbook类初始化时有encoding和style_compression参数
    # encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。
    # 默认是ascii。当然要记得在文件头部添加：
    # #!/usr/bin/env python
    # # -*- coding: utf-8 -*-
    # style_compression:表示是否压缩，不常用。
    # '''

    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
    # 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
    sheet = book.add_sheet('test', cell_overwrite_ok=True)
    # 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False
    # 向表test中添加数据
    # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
    sheet.write(0, 0, 'EnglishName')
    sheet.write(1, 7, 'test'.decode('utf-8'))
    text1 = '中文名字'
    sheet.write(0, 1, text1.decode('utf-8'))  # 此处需要将中文字符串解码成unicode码，否则会报错
    text2 = '马可瓦多'
    sheet.write(1, 1, text2.decode('utf-8'))
    # 最后，将以上操作保存到置顶的Excel文件中

    filename = '{}{}{}{}'.format('test_image', os.sep, 'test', '.xls')
    book.save(filename)


book = getNewXlsBook()
sheet = getNewSheetWithBook(book)
for value in range(1, 10):
    pass
    for value1 in range(1, 10):
        pass
        text = '第' + str(value) + '行第' + str(value1) + '列'
        print text
        writeLine(sheet=sheet, row=value, colom=value1, text=text)
bookSave(book, './sheet_dir', 'test')
