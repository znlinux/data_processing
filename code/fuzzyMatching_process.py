# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 00:10:43 2018

@author: ZN
调用模糊匹配的process模块：
extract:返回列表中n（limit设定的）个可能的匹配，并带有比例（返回元组）
extractOne：返回列表中与字符串对应的最佳匹配，并带有比例（返回元组）
"""

from fuzzywuzzy import process

choices=['Yes','No','Maybe','N/A']

print(process.extract('ya',choices,limit=2))

print(process.extractOne('ya',choices))

"""
out:
[('Yes', 45), ('Maybe', 45)]
('Yes', 45)
"""