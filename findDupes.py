# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:43:54 2018

@author: Administrator
找出重复值
使用set函数
"""

list_with_dupes = [1,5,1,5,2,3,2,3,4,5,6,5,1]

set_without_dupes =set(list_with_dupes)

print(set_without_dupes)
"""
intersection：交集
union：并集
difference：差
in：判断是否在内

"""

first_set = set([1, 5, 6, 2, 6, 3, 6, 7, 3, 7, 9, 10, 321, 54, 654, 432])  
 
second_set = set([4, 6, 7, 432, 6, 7, 4, 9, 0]) 
 
print(first_set.intersection(second_set))
 
print(first_set.union(second_set)) 
 
print(first_set.difference(second_set)) 
print(second_set - first_set)
 
print(6 in second_set)
 
print(0 in first_set)
"""
out:
{1, 2, 3, 4, 5, 6}
{432, 9, 6, 7}
{0, 1, 2, 3, 321, 5, 6, 7, 4, 9, 10, 654, 432, 54}
{321, 1, 2, 3, 5, 10, 654, 54}
{0, 4}
True
False  
"""
import numpy as np 
 
list_with_dupes = [1, 5, 6, 2, 5, 6, 8, 3, 8, 3, 3, 7, 9]
""" 
#unique方法保存索引编号， 返回（数组1，数组2）：数组1：唯一值组成的数组：
数组2：索引编号组成的数组
#array方法将连个长度相同的数组组成的唯一值数组
"""
print(np.unique(list_with_dupes, return_index=True)) 
 
array_with_dupes = np.array([[1, 5, 7, 3, 9, 11, 23], [2, 4, 6, 8, 2, 8, 4]]) 
 
print(np.unique(array_with_dupes))
"""
out: 
(array([1, 2, 3, 5, 6, 7, 8, 9]), array([ 0,  3,  7,  1,  2, 11,  6, 12], dtype=int64))
[ 1  2  3  4  5  6  7  8  9 11 23]
"""

