# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 20:40:17 2018

@author: Administrator
"""

import xlrd
import pprint

book = xlrd.open_workbook('data/SOWC 2014.xlsx')

sheet = book.sheet_by_name('Table 9 ')

#嵌套循环
#for i in range(sheet.nrows):
   # row = sheet.row_values(i)
    
   # for cell in row:
      #  print(cell)
      
#简单计数器
#count = 0
#for i in range(1000):
 #   if count < 10:
#        print(i)
#    count += 1
    
#print('Count: ',count)
 
count=0
 
 
data={}#创建一个空的字典保存数据

for i in range(14,sheet.nrows):#通过计数器可得知数据从第14行得到
    row = sheet.row_values(i)
    country = row[1]#取出每一行国家名字赋值country
    data[country]={#将国家设为data字典的键
            'child_labor':{#根据需求创建child_labor键，值设为另一个字典
                    'total':[row[4],row[5]],
                    'male':[row[6],row[7]],#字典的键是字符串，说明保存的内容
                    'female':[row[8],row[9]],
                    },
            'child_marriage':{
                    'married_by_15':[row[10],row[11]],
                    'married_by_18':[row[12],row[13]],
                    }
            }
pprint.pprint(data)
