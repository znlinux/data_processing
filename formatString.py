# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 14:59:52 2018

@author: ZN
本例中主要解释format的用法
"""
example_dict = {
        'float_number':15645.231,
        'very_large_integer':151651321321532132,
        'percentage':.5165,
        }
"""
利用键访问字典的值，用：分割键名和格式。
.4f将数字转换成浮点数，保留4位小数
,千位分隔符
.2%插入百分号，小数部分保留两位有效数字
**将字典拆包：将字典的键/值拆开，拆包后的键和值被传递给format方法
"""
string_to_print = "float:{float_number:.4f}\n"
string_to_print += "integer:{very_large_integer:,}\n"
string_to_print += "percentage:{percentage:.2%}"

print(string_to_print.format(**example_dict))
