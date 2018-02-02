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
5.	代码：提前想好输出格式的样子，写出这样一个数据实例下一步我要怎么做才能实现目标<br>

