# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:22:17 2018

@author: Administrator
"""
import tushare as ts
stockid=['600848','300412']
date='2017-12-01'

for i in range(2):
    df = ts.get_hist_data(stockid[i], start=date, end=date)
    print(float(df["close"]))

