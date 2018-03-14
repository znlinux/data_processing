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
9.      应用list()时候要注意，list一次后，zip对象会被清空（当迭代结构遍历后会被清空）<br><br>

10.	TypeError: 'zip' object is not subscriptable<br>
在使用zip函数时，2.*版本和3的用法不一致：<br>
	实例：<br>
	python2:<br>
	set_of_keys = set([ <br>
    '%s-%s-%s' % (x[0][1], x[1][1], x[2][1]) for x in zipped_data]) <br>
<br>
	python3:<br>
	for x in zipped_data:<br>
    y = list(x)<br>
    key.append(y)<br>
set_of_keys = set([<br>
        '%s-%s-%s'%(y[0][1],y[1][1],y[2][1]) for y in key])<br>
	#要先将zip转换成list类型才可以迭代<br><br>
11.	ModuleNotFoundError: No module named 'MySQLdb'<br>
错误原因：python3不适用<br>
解决：<br>
详情：http://www.runoob.com/python3/python3-mysql.html<br>
pip install pymysql<br>
连接已创建好的数据库：<br>
import pymysql<br>
 <br>
# 打开数据库连接<br>
db = pymysql.connect("localhost","用户名","密码","表名" ) <br>
# 使用 cursor() 方法创建一个游标对象 cursor<br>
cursor = db.cursor()<br>
# 使用 execute()  方法执行 SQL 查询 <br>
cursor.execute("SELECT VERSION()")<br>
# 使用 fetchone() 方法获取单条数据.<br>
data = cursor.fetchone()<br>
print ("Database version : %s " % data)<br>
# 关闭数据库连接<br>
db.close()<br>
	创建数据库表：<br>
		import pymysql<br>
 
# 打开数据库连接<br>
db = pymysql.connect("localhost","testuser","test123","TESTDB" ) <br>
# 使用 cursor() 方法创建一个游标对象 cursor<br>
cursor = db.cursor()<br>
# 使用 execute() 方法执行 SQL，如果表存在则删除<br>
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")<br>
# 使用预处理语句创建表<br>
sql = """CREATE TABLE EMPLOYEE (<br>
        	FIRST_NAME  CHAR(20) NOT NULL,<br>
         	LAST_NAME  CHAR(20),<br>
        	AGE INT,  <br>
        	SEX CHAR(1),<br>
         	INCOME FLOAT )"""<br>
 
cursor.execute(sql)<br>
# 关闭数据库连接<br>
db.close()<br>
12.	SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape<br><b
错误：x.to_excel("C:\ Python\news.xlsx")<br>
改为：x.to_excel(r"C: \Python\news.xlsx")<br>

13.	python3的map,reduce函数：<br>
reduce函数：用于计算累加<br>
引入import functiools as func<br>
		func.reduce()<br>
或者用from functools import reduce<br>
		  reduce()<br>
<br>
map函数改为列表生成式<br>
函数功能： 运用表达式，运算两个列表生成新的列表；map（表达式，列表1，列表2）<br>
如： map(lambda(x,w) : x * w, zip(input_vec,self.weights)<br>
改为[x * w for x, w in zip(input_vec, self.weights)]<br>



