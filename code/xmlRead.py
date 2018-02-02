# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:30:11 2018

@author: Administrator
"""
from xml.etree import ElementTree as ET

tree = ET.parse('data/data-text.xml')
root =tree.getroot()

data = root.find('Data')

all_data = []

for observation in data:
    record={}
    #设置键值对
    for item in observation:
        lookup_keys = list(item.attrib.keys())
        lookup_key = lookup_keys[0]
        if lookup_key == 'Numeric':
            rec_key ='NUMERIC'
            rec_value=item.attrib['Numeric']
        else:
            rec_key=item.attrib[lookup_key]
            rec_value = item.attrib['Code']
        #将每一个键值对添加到record字典中
        record[rec_key] = rec_value
        all_data.append(record)
        print(all_data)
        