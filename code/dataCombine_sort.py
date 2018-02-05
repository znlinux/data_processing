# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:03:01 2018

@author: ZN
"""
from csv import reader

data_rd = reader(open('data/mn.csv','r',encoding="utf-8"))
head_rd = reader(open('data/mn_headers_updated.csv','r',encoding="utf-8"))

data_rows = [d for d in data_rd]
head_rows = [h for h in head_rd if h[0] in data_rows[0]]



all_short_heads = [h[0] for h in head_rows]

skip_index = []
#创建新的列表，，包含顺序正确的最终标题行
final_head_rows = []
#取出所有不需要保存的数据表中的索引号
for dhead in data_rows[0]:
    if dhead not in all_short_heads:
        index = data_rows[0].index(dhead)
        skip_index.append(index)
    else:  #利用else语句，只将匹配的列添加到列表，遍历head_rows
        for head in head_rows:
            if head[0] == dhead:
                final_head_rows.append(head)
                break#找到匹配后退出循环
#print(final_head_rows)

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
    
#print(list(zipped_data[0]))
"""
for x in zipped_data[0]:
    print('Question:{}\nAnswer:{}'.format(x[0],x[1]))
"""
"""
数据格式：
Question:['HH1', 'Cluster number', '']
Answer:1
需进一步清洗：Question部分只需要第二个值
"""
"""
for x in zipped_data[0]:
    print('Question:{[1]}\nAnswer:{}'.format(x[0],x[1]))

for x in enumerate(list(zipped_data[0])[:20]):
    print(x)

处理日期
"""
from datetime import datetime
"""
创建一个字符串模板 zipped_data[第一条数据][数据行索引号，通过enumerate获得][数据本身]
两种方式更改日期格式
"""
a=list(zipped_data[0])

start_str='{}-{}-{} {}:{}'.format(
        a[8][1],
        a[7][1],
        a[9][1],
        a[13][1],
        a[14][1])

start_time = datetime.strptime(start_str,'%m-%d-%Y %H:%M')
#2014-04-07 17:59:00
print(start_time)

end_time=datetime(
        int(a[9][1]),
        int(a[8][1]),
        int(a[7][1]),
        int(a[15][1]),
        int(a[16][1])
        )
#2014-04-07 18:07:00
print(end_time)
duration = end_time - start_time
#0:08:00
print(duration)
#0
print(duration.days)
#480.0
print(duration.total_seconds())
#8.0
print(duration.total_seconds()/60.0)
#将datetime格式的日期转换成希望的日期格式
#04-07-2014 18:07:00
print(end_time.strftime('%m-%d-%Y %H:%M:%S'))

#Mon Apr  7 18:07:00 2014
print(end_time.ctime())
#2014-04-07T17:59:00
print(start_time.strftime('%Y-%m-%dT%H:%M:%S'))
