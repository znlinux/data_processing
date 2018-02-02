# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:47:26 2018

@author: Administrator
"""

import json

json_data = open('data/data-text.json').read()

data = json.loads(json_data)

for item in data:
    print(item)