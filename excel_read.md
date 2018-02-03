# data_processing
Tool-version:  python 3.6<br>
1.	处理Excel数据<br>
环境准备：<br>
安装外部包xlrd<br>
pip install xlrd<br>
【扩展： 卸载Python包：pip uninstall xlrd<br><br>
2.	解析Excel文件：<br>
解析前思考：<br>
是否尝试过寻找其他格式的数据？<br>
是否尝试过将Excel文件的一个或多个标签导出成CSV格式（尤其是若EXCEL表中只有几个标签有数据，或只有一个标签的独立数据）<br><br>
3.	开始解析：<br>
*  	处理Excel文件的三个主要库：<br>
xlrd ：读取<br>
xlwt ：写入并设置格式<br>
xlutils：一组高级操作工具（先安装xlrd和xlwt）<br>
*  	指令：<br>
*  	import xlrd:必备<br>
*  	book = xlrd.open_workbook(‘*.xlsx’) :打开表<br>
*  	book.sheet_by_name(工作表名字)：访问工作表<br>
*  	for sheet in book.sheets():<br>
		print sheet.name  ：获得所有工作表的名字<br><br>
*   dir(sheet)列出内置方法和属性的列表<br><br>
*   sheet.nrows返回总行数<br>
*  range(i)函数：输出i个元素组成的列表<br>
		注意：range(0,i)返回前i个数<br>
*  sheet.row_values(i)根据行号获取每一行的值<br>
5.	代码：提前想好输出格式的样子，写出这样一个数据实例下一步我要怎么做才能实现目标<br><br>
6.	嵌套循环：<br>
	for i in range(sheet.nrows):<br>
    row = sheet.row_values(i) #将每一行内容组成的列表保存到row变量中<br><br>
    
    for cell in row:    #遍历表中的每一个单元格<br>
        print(cell)<br><br>
7.	计数器（计数器是用来发现我们所需数据的位置）<br>
#简单计数器，实现功能：只输出小于10的数，并统计循环次数<br>
count = 0<br>
for i in range(1000)<br>
if count < 10:
 print(i)<br>
count += 1<br>
    
print('Count: ',count)<br>

#观察计数器<br>
count = 0 <br>
data = {} <br><br>                              
 
for i in range(sheet.nrows):<br>  
    if count < 10: <br>
        if i >= 14:<br> 
            row = sheet.row_values(i)  <br>
            country = row[1]     <br>       
            data[country] = {}    <br>      
            count += 1  <br><br>
 
print data     <br><br>                         
8.	索引<br>
Python的索引编号从0 开始，x[i]<br>
正数索引从前面数输出第i+1个，负数索引从后面开始数输出第i个<br><br>
9.	切片<br>
x[i,j]输出第i+1到第j个元素<br>
例子：x = ['cat', 'dog', 'fish', 'monkey', 'snake']<br>
x[1:4]：['dog', 'fish', 'monkey']输出第2个到第4个<br>


