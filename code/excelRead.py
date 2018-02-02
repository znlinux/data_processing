# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 20:40:17 2018

@author: Administrator
"""

import xlrd

book = xlrd.open_workbook('data/SOWC 2014.xlsx')

sheet = book.sheet_by_name('Table 9 ')

for i in range(sheet.nrows):
    print(sheet.row_values(i))