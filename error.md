Python 3.6使用错误合集<br><br>

1. TypeError: 'dict_keys' object does not support indexing<br>
Python2： lookup-key =item.attrib.keys()[0]   <br>

Python4:	lookup-keys = list(item.attrib.keys())  #获取列表<br>
        lookup_key = lookup_keys[0]        #获取列表索引，得到第一个值<br><br>
2.	SyntaxError: can't assign to operator<br>
我遇到的是：变量名不能有”-“符号，应该是下划线的<br><br>
3.	IndentationError: unexpected unindent<br>
检查代码的缩进，箭头所指地方缩进不符合规范<br>
4.	XLRDError: No sheet named <'Table 9'><br>
在表名后面加一个空格：’Table 9 ’<br><br>
5.	UnicodeDecodeError: 'gbk' codec can't decode byte 0x9d in position 2817: illegal multibyte sequence
data_rd = DictReader(open('data/mn.csv','r'))<br>
改为：<br>
data_rd = DictReader(open('data/mn.csv','rb'))<br><br>
6.	Error: iterator should return strings, not bytes (did you open the file in text mode?)<br>
源代码：<br>
data_rd = DictReader(open('data/mn.csv','rb'))<br>
错误原因：此CSV文件并非二进制文件，只是一个文本文件<br>
解决：<br>
data_rd = DictReader(open('data/mn.csv','rt',encoding="utf-8"))<br>
或<br>
data_rd = DictReader(open('data/mn.csv','r',encoding="utf-8"))<br><br>

7.	TypeError: 'zip' object is not subscriptable<br>
错误原因：python3.* <br>
需要用list读取zip<br>
错误代码：<br>
for x in enumerate(zipped_data[0][:20]):<br>
    print(x)<br><br>
改为：<br>
for x in enumerate(list(zipped_data[0])[:20]):<br>
    print(x)<br><br>
8。      ValueError: time data '4-7-2014 17:59' does not match format<br> '%m-%d-%y %H:%M'<br>
错误原因：Y,H,M需要大写<br>
改正：<br>
ValueError: time data '4-7-2014 17:59' does not match format '%m-%d-%Y %H:%M'<br><br>
9.      应用list()时候要注意，list一次后，zip对象会被清空（当迭代结构遍历后会被清空）<br>

