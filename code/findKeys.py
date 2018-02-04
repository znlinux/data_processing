# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:43:41 2018

@author: ZN
"""
from csv import reader
data_rd = reader(open('data/mn.csv','r',unicoding="utf-8"))
head_rd = reader(open('data/mn_headers_updated.csv','r',unicoding="utf-8"))

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
a=list(zipped_data[0])
for x in enumerate(a):#返回索引编号+值
  print(x)
  为了查看哪些组成了唯一标识符
  “Line number”不确定是否是唯一标识符的组成，需确定:
  
"""
b = list(zipped_data)
"""
x[2][1]表示的是第3行第2个元素---即Line number所在的位置
set返回的是不重复的元素集合
利用remove方法检测每个键出现的次数是否多于一次;
set_of_lines存放的是唯一键，若有重复值，则remove会触发KeyError
"""
set_of_lines = set(x[2][1] for x in b)#
uniques = [x for x in b if not set_of_lines.remove(x[2][1]) ]
print(set_of_lines)


"""
结果表明家庭成员编号并不是唯一的，
但我们可以利用类群编号、家庭编号和家庭成员编号作为唯一标识符：
利用类群编号、家庭编号和家庭成员编号创建一个字符串，构成唯一标识符
利用remove方法重新创建唯一键，unqiue表中包含每一个唯一数据，如果有重复会抛出异常
计算唯一列表的长度
"""
set_of_keys =set([
    '%s-%s-%s' % (x[0][1],x[1][1],x[2][1])for x in b]) 
unique = [x for x in b if not set_of_keys.remove(
     '%s-%s-%s' % (x[0][1],x[1][1],x[2][1]))]
print(len(set_of_keys))