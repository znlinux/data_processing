# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 12:18:19 2018

@author: ZN
检查类群编号、家庭编号和家庭成员编号三者是否构成唯一键
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
    
"""
利用类群编号、家庭编号和家庭成员编号创建一个字符串构成唯一标识符
利用remove方法判断是否有重复数据并创建uniques列表存放唯一数据
len返回的是唯一键列表的长度
"""
key =[] 

for x in zipped_data:
    y = list(x)
    key.append(y)
set_of_keys = set([
        '%s-%s-%s'%(y[0][1],y[1][1],y[2][1]) for y in key])
print(len(set_of_keys))
uniques = [y for y in key if not set_of_keys.remove(
        '%s-%s-%s'%(y[0][1],y[1][1],y[2][1]))]
print(len(uniques))    
