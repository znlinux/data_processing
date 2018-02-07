# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 00:59:49 2018

@author: ZN
正则表达式：
计算机可以对代码中的字符串或数据的模式进行匹配、查找或删除
\w :匹配任意一个字母字符或数字字符，包括下划线
\d :匹配任意一个数字
\s :匹配任意一个空格字符    ‘’
+  :匹配一个或多个字符  如：\d+可以匹配2748348
\. :匹配.字符
*  :匹配零个或多个字符或模式 如：\d*可以匹配423425和''
|  :匹配多个模式中的一个（or) 如：\d|\w匹配0或a
[]或():匹配字符类或字符组        [A-C]或(AlBlC)可匹配A
                            [A-Z]\w+表示的是希望第一个字母是大写，后面紧跟一个连续的单词
-  :合并字符组

使用内置的正则表达式模块re
"""

import re

"""
定义一个普通字符串的基本模式：
包含字母和数字，但不包含空格和标点的字符串
该模式会一直匹配（+）
.findall()找出这个模式下字符串的所有匹配组成的列表

.search()在整个字符串中搜索匹配，发现匹配对象则返回

匹配对象.group()返回匹配的字符串

.match()只从字符串的开头开始搜索，原理与search不同：
match()方法用于匹配特定模式开头的字符串：若第一个不匹配则返回None
serch()方法用于在字符串中找到第一个匹配或任意匹配：直到到达结尾还没找到匹配才返回None
"""
word = '\w+'
sentence='Here is my sentence.'

print(re.findall(word,sentence))

search_result = re.search(word,sentence)

print(search_result)
print(search_result.group())

match_result =re.match(word,sentence)
print(match_result.group())

"""
out:
['Here', 'is', 'my', 'sentence']
<_sre.SRE_Match object; span=(0, 4), match='Here'>
Here
Here
"""
number = '\d+' 
capitalized_word = '[A-Z]|[A-Z]\w+'
 
sentence = 'I have 2 pets: Bear and Bunny.' 
 
search_number = re.search(number, sentence)  
print(search_number.group())
 
#match_number = re.match(number, sentence) 
#print(match_number.group())
 
search_capital = re.search(capitalized_word, sentence)  
print(search_capital.group()) 
 
match_capital = re.match(capitalized_word, sentence) 
print(match_capital.group())

"""
out:
AttributeError: 'NoneType' object has no attribute 'group'
证明match_number返回的是None
注释后继续运行其他三个：
out2：
AttributeError: 'NoneType' object has no attribute 'group'
match_capital返回的是None
(？证明I并没有被识别认为匹配'[A-Z]\w+':
    改进：
    '[A-Z]\w+'改为'[A-Z]|[A-Z]\w+'再取消最后一个注释
    运行out:
        2
        I
        I
    )

注释运行：
out:
2
Bear

创建匹配多个模式组的模式：
利用括号的分组功能将多个单词语法放在一起
因为含有多个正则表达式组，若找到匹配则返回多个匹配组
.group()返回的是所有匹配组
 如：Barack Obama
.groups()方法返回所有匹配组构成的列表
 如：('Barack', 'Obama')

使用(?P<命名>正则表达式)为各组命名，候命值需要调用'命名'即可
.finditer(模式，字符串数组)与findall类似,返回的是一个迭代器，利用这个 
要使用for循环调用
在匹配的字符输出的时候用{}表示
"""
name_regex = '([A-Z]\w+) ([A-Z]\w+)'
names = "Barack Obama, Ronald Reagan, Nancy Drew"

name_match = re.match(name_regex,names)
print(name_match.groups())

name_regex2 = '(?P<first_name>[A-Z]\w+) (?P<last_name>[A-Z]\w+)'

for name in re.finditer(name_regex2, names):
    print('Meet {}!'.format(name.group('first_name')))
    
"""
out:
Meet Barack!
Meet Ronald!
Meet Nancy!
"""



