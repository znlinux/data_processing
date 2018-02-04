# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:36:16 2018

@author: ZN
"""
from csv import reader

data_rd = reader(open('data/mn.csv','r',encoding = "utf-8"))
head_rd = reader(open('data/mn_headers_updated.csv','r',encoding = "utf-8"))

data_rows = [d for d in data_rd]
#如果标题行的第一个元素包含在数据行的标题中，就将该标题行添加到新列表中
head_rows = [h for h in head_rd if h[0] in data_rows[0]]
"""
print('个数： ',len(head_rows))
print('数据表中的标题： ',data_rows[0])
print('标题表中的： ',head_rows)
"""
#标题表中的所有短标题
all_short_heads = [h[0] for h in head_rows]
#用来保存不希望保存的数据行的索引编号
skip_index = []

for head in data_rows[0]:
    if head not in all_short_heads:
        """
        index函数取数据的索引编号
        """
        index = data_rows[0].index(head)
        skip_index.append(index)
print('不需保存的索引编号（数据表中多余的）：',skip_index)

#创建一个新的列表存放data数据行（从第一行开始，而不是标题行）       
new_data =[]

for row in data_rows[1:]:
    #创建一个新的列表存放每行的数据
    new_row=[]
    """
    #enumerate函数找出不需要保存的数据行；i存放的是索引编号，d存放的是值
    """
    for i,d in enumerate(row):
        if i not in skip_index:
            new_row.append(d)
    new_data.append(new_row)
            
zipped_data = []

for drow in new_data:
    zipped_data.append(zip(head_rows,drow))
"""
print(list(zipped_data[2]))
"""
"""
真实核查
"""
#创建新的列表,存放数据列表的标题行
data_heads =[]
#遍历数据列表中的所有标题
for i,head in enumerate(data_rows[0]):
    if i not in skip_index:
        data_heads.append(head)
        
head_match = zip(data_heads ,all_short_heads)

print(list(head_match))

"""
发现在'MHA27'之后的标题都不匹配
进行数据匹配
数据匹配的代码：dataCombine_sort.py
"""
