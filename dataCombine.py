# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 08:16:42 2018

@author: ZN
将标题列表和数据列表合并在一起:使用Python的zip方法
需要：创建标题列表和数据列表，查看长度是否相同

"""
from csv import reader

data_rd = reader(open('data/mn.csv','rt',encoding ="utf-8"))
head_rd = reader(open('data/mn_headers.csv','r',encoding="utf-8"))

data_rows = [d for d in data_rd]
head_rows = [h for h in head_rd]

print(len(data_rows[0]))
print(len(head_rows))
"""
显示是159和210，需要发现
"""
bad_rows = []

for h in head_rows:
    if h[0] not in data_rows[0]:#测试标题行的而第一个元素是否包含在数据列表的第一行中
        bad_rows.append(h)
        
for h in bad_rows:
    head_rows.remove(h)
    
print(len(head_rows))

all_short_headers = [h[0] for h in head_rows]

for h in data_rows[0]:
    if h not in all_short_headers:
        print('mismatch!',h)
"""
检查不匹配的行发现：
有的数据是有用的，得在标题表格里添加
更新表格为mn_headers_update.csv
相应的代码存储到dataCombine_update.py文件中
"""

        
        