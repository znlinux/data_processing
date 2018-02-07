# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 23:39:39 2018

@author: ZN
模糊匹配，判断两个元素（通常是字符串）是否“相同”
ratio:接受两个字符串作比较。返回的是两个字符
串序列的相似程度（一个介于1 和 100 之间的值)

partial_ratio:接受两个字符串作比较。返回的是
匹配程度最高的子字符串序列的相似程度（一个介于1和 100 之间的值）

partial_token_sort_ratio:在匹配字符串时不考虑单词顺序。每个字符串都是先排序然后再比较，所以如果包
含相同的单词但顺序不同，也是可以匹配的

partial_token_set_ratio:对排序后的标记尝试寻找最佳匹配，返回这些标记相似的比例
缺点：可能会出现错误匹配
"""
from fuzzywuzzy import fuzz

my_records = [{'favorite_book':'Grapes of wrath',
               'favorite_movie': 'Free Willie',
               'favorite_show': 'Two Broke Girls',
               },
            {'favorite_book': 'The Grapes of Wrath',
              'favorite_movie': 'Free Willy', 
              'favorite_show': '2 Broke Girls', 
              }]

print(fuzz.ratio(my_records[0].get('favorite_book'),
                 my_records[1].get('favorite_book')
        ))

print(fuzz.partial_ratio(my_records[0].get('favorite_book'),
                         my_records[1].get('favorite_book')
        ))

print(fuzz.partial_token_sort_ratio(my_records[0].get('favorite_book'),
                                    my_records[1].get('favorite_book')
        ))

print(fuzz.partial_token_set_ratio(my_records[0].get('favorite_book'),
                                   my_records[1].get('favorite_book')
        ))

"""
output:
82
93
80
100

"""