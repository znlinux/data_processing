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

first_set=set([1,5,6,2,6,3,6,7,9,10,321])
second_set=set([3,5,7,3,22,533,321])
print(first_set.intersection(second_set))
print(first_set.union(second_set))
print(first_set.difference(second_set))
print(first_set-second_set)
print(3 in second_set)
print(11 in first_set)
"""
out:
  {1, 2, 3, 4, 5, 6}
  {321, 3, 5, 7}
  {1, 2, 3, 321, 5, 6, 7, 9, 10, 533, 22}
  {1, 2, 10, 6, 9}
  {1, 2, 10, 6, 9}
  True
  False
"""
import numpy as np
list = [1,4,2,3,5,6,56,9,321,67]
print(np.unique(list,return_index=True))
array = np.array([[1,3,1,6,2,3,8],[3,5,6,3,2,1,1]])
print(np.unique(array))
"""
out:
(array([  1,   2,   3,   4,   5,   6,   9,  56,  67, 321]), array([0, 2, 3, 1, 4, 5, 7, 6, 9, 8], dtype=int64))
[1 2 3 5 6 8]
第一个数组是唯一值，第二个数组是第一个数组相应位置的数字第一次在原数组中的位置
第三个数组是有两个长度相同的数组取唯一值的并集
"""