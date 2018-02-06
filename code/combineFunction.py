# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 03:04:58 2018

@author: ZN
处理重复记录：
1. 如果数据集只有重复行：清洗数据中删除或舍弃这些行
2. 如果合并不同的数据集，并希望保存每一条重复数据则：
    使用DictReader模块，方便解析字段
    定义一个函数命名为combine_data_dict,使用def函数：将data_rows合并，然后返回一个字典
    定义一个新的字典，用于函数的返回值
    创建一个唯一键key(用类群编号和家庭编号表示唯一家庭)
    判断：如果已经添加过这个家庭，就把数据加在这个家庭下面
        否则，新建一个列表，添加键/值对
"""
from csv import DictReader

mn_data_rd = DictReader(open('data/mn.csv','r',encoding="utf-8"))
mn_data = [d for d in mn_data_rd]

def combine_data_dict(data_rows):
    data_dict= {}
    for row in data_rows:
        key = '%s-%s'%(row.get('HH1'),row.get('HH2'))
        if key in data_dict.keys():
            data_dict[key].append(row)
        else:
            data_dict[key]=[row]
    return data_dict

mn_dict = combine_data_dict(mn_data)

print(len(mn_dict))
            
"""
out:
6920
分析：总共9008条数据，有69200个家庭，则则平均每个家庭有1.3个男性
"""   