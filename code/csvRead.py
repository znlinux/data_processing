# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:42:52 2018

@author: Administrator
"""
import csv 
 
csvfile = open('data/data-text.csv', 'r') 
reader = csv.reader(csvfile) 
 
for row in reader: 
    print(row)