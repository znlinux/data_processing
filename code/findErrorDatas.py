# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:28:52 2018

@author: Administrator
发现数据中可能存在的错误：“这些数据是否有不一致的地方？”
简单方法：查看数据值里是否有错误。
找出离群值和不良数据
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
z = list(zipped_data[0])  
    #遍历第一条数据的每一行
for answers in z:
    if not answers[1]:
        print(answers)

 """
a= list(zipped_data)
#遍历数据集的每一行


#定义一个字典，保存回答中包括NA的问题：键是问题，值是NA回答的个数
na_count ={}

print(len(a))
for row in a:
    for resp in row:
        question = resp[0][1]
        answer = resp[1]
        if answer == 'NA':
            if question in na_count.keys():
                na_count[question] += 1
            else:
                na_count[question] = 1
print(na_count)
        


