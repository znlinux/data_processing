# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:43:29 2018

@author: zn
清洗数据
"""

#导入csv文件
from csv import DictReader
#打开csv文件
data_rd = DictReader(open('data/mn.csv','rt',encoding="utf-8"))
head_rd = DictReader(open('data/mn_headers.csv','rt',encoding="utf-8"))
#生成一个新的列表
data_rows = [d for d in data_rd]
head_rows = [h for h in head_rd]
"""
print(data_rows[:5])#slice方法，显示新列表的前5个元素
print(head_rows[:5])
"""
"""
输出发现长标题在head_rows的Lable属性中
短标题在Name属性中
1.遍历每一条记录
2.遍历每一行的数据的键和值：查看数据字典的每一个键值对，使用的是items方法
3.遍历所有标题行，保证不会有遗漏
4.遍历键和值
5.若数据列表的键和标题字典的值相同，则打印match!
for data_dict in data_rows:
    for dkey,dval in data_dict.items():
        for head_dict in head_rows:
            for hkey,hval in head_dict.items():
                if dkey == hval:
                    print('match!')
打印发现有很多匹配项，想办法将data的键与head的值对应
1.创建一个新列表，包含清洗过的行数据
2.为每一行创建一个新字典
3.if dkey in head_dict.values()利用字典的values方法，返回仅由字典的值组成的列表
4.if in 判断某一对象是否包含在某个列表中。
"""
new_rows=[]

for data_dict in data_rows:
    new_row = {}
    for dkey,dval in data_dict.items():
        for head_dict in head_rows:
            if dkey in head_dict.values():
                new_row[head_dict.get('Label')]=dval
    new_rows.append(new_row)
        