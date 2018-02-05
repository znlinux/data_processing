# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:10:32 2018

@author: ZN
找出数据的唯一标识符
"""
from csv import reader

data_rd = reader(open('data/mn.csv','r',encoding="utf-8"))
head_rd = reader(open('data/mn_headers_updated.csv','r',encoding="utf-8"))

data_rows = [d for d in data_rd]
head_rows = [h for h in head_rd if h[0] in data_rows[0]]

all_short_heads = [h[0] for h in head_rows]

skip_index = []

final_head_rows = []

for dhead in data_rows[0]:
    if dhead not in all_short_heads:
        index = data_rows[0].index(dhead)
        skip_index.append(index)
    else: 
        for head in head_rows:
            if head[0] == dhead:
                final_head_rows.append(head)
                break

new_data = []

for row in data_rows[1:]:
    new_row = []
    for i,d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
    new_data.append(new_row)
    
zipped_data = []

for drow in new_data:
    zipped_data.append(zip(final_head_rows,drow))
#print(zipped_data)
    
"""
利用enumerate函数观察数据：返回索引号和数据值

测试家庭成员编号是不是唯一标识符 第三行第二列是家庭成员编号
利用remove函数判断家庭成员编号是否唯一：不唯一，remove会引发KeyError
测试某个值是否存在 if not x:
测试是否有None类型的数据 if x is None:
set可以看成数学意义上的无序和无重复元素的集合
"""


#创建一个集合包含所有的家庭成员编号

lines = []
for x in zipped_data:
    y = list(x)
    lines.append(y)
set_of_lines = set([y[2][1] for y in lines])

uniques=[ y for y in lines if not set_of_lines.remove(y[2][1])]

print(uniques)

"""
out:
KeyError: '1'
证明有重复数据
"""
