# -*- coding: UTF-8 -*-
import re
file_object = open('new.txt')
new = file_object.read()
results = re.findall('([0-9]{9})', new, re.S)
print('今日日赚10元以上    ' + bytes(len(results)))

new_file = open('today.txt')
html1 = new_file.read()
results1 = re.findall('([0-9]{9})', html1, re.S)

print('已统计日赚10元以上    ' + bytes(len(results1)))
items = list(set(results).difference(set(results1)))
print('未统计用户')
for item in items:
    retext = item + '.*?' + '(\d+\.*\d*元)'
    num = re.findall(retext, new, re.S)
    print(item + '      ' + bytes(num[0]) + '\n')
