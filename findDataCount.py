# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:29:23 2018

@author: Administrator
计算数据类型的数目
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
#建立一个空字典：  
datatypes={}
#创建一个用于统计data set中的数据类型，列出所有可能的数据类型
start_dict = {
        'digit':0,
        'boolean':0,
        'empty':0,
        'time_related':0,
        'text':0,
        'unknown':0
        }

a=list(zipped_data)
for row in a:
    for resp in row:
        question = resp[0][1]
        answer = resp[1]
        key = 'unknown'#设置默认值为unknown
        #判断数据类型的方法
        if answer.isdigit():#判断字符串中是否只包含数字
            key ='digit'
        elif answer in ['Yes','No','True','False']:#判断字符串是否是布尔组成的
            key ='boolean'
        elif answer.isspace():#判断字符串是否只包含空格
            key ='empty'
        elif answer.find('/') > 0 or answer.find(':')>0:#字符串是否时间格式的数据
            key = 'time_related'
        elif answer.isalpha():#判断字符串是否只包含字符
            key = 'text'
        if question not in datatypes.keys():#不在，则将问题添加到字典中
            #copy方法为每一条数据创建一个独立的字典对象
            datatypes[question] = start_dict.copy()
        
        datatypes[question][key] += 1
    
print(datatypes)
