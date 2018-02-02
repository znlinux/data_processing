# data_processing
Tool-version:  python 3.6
1.	机器可读格式：
  *	逗号分隔值CSV
  *	JavaScript对象符号 JSON
  *		可扩展标记语言 XML
2.	运用Python读取CSV数据
  *	步骤：
编写代码，命名为*.py文件(csvRead.py)（注意大小写，间距和换行<python比较严格>）<br>
将csv文件和py文件放在同一文件夹code中<br>
（或）/code/data/*.csv<br>
		 /code/*.py<br>
		则代码改为open(‘data/*.csv’,’rb’)<br><br>
 
运行<br>
  * 命令行运行（终端或cmd）<br>
cd ~/Projects/data_wrangling/code(跳转到py文件所在路径)<br>
python *.py<br>
  * 在 Anaconda里直接打开*.py文件Run<br>
 
  * 缺点：可读性不高<br>
2.3	改进：<br>
  代码改为：reader = csv.DictReader(csvfile)<br>
  则每个数据记录变成一个字典（键是CSV文件的第一行，其余均为值）<br><br>
 
3.	JSON数据<br>
  导入JSON数据<br>
  保存数据： 键/值对<br>
  * 步骤：<br>
  导入json包open函数打开json.loads()将数据载入Python，输出保存在变量datafor循环遍历所有数据，打印每一项<br><br>
 
  * 与CSV的读取区别：<br>
  * CSV: 只读方式打开文件，得到的是文件对象<br>
  * JSON：读取文件并将内容保存在变量中，得到的是字符串对象<br>
  * 注意：<br>
     loads()函数接受字符串作为参数，但是不接收文件作为参数：将JSON字符串载入Python。<br>
      reader函数接受打开的文件作为参数<br><br>
4.	XML数据<br>
    保存数据： 标签和属性<br>
    导入XML数据：<br>
  * 步骤：<br>
    导入ElementTree（用来解析XML）<br>
   调用ET类的parse方法（对传入文件中的数据进行解析，返回Python对象—树）<br>
    使用getroot函数获取树的根元素（根标签）<br>
  【打印： print(root)  得到：<Element 'GHO' at 0x000000000C4B3458>】<br>
   【代码外Analysis：只取XML的标签，理解XML树的整体结构与格式<br>
  print list(root)去更好的理解如何提取所需数据<br><br>
 
* 比如发现Data数据较好，我们就可以获取Data数据—替换代码：<br>
  data = root.find(‘Data’)   #如果有多个Data元素列出来，则用findAll()<br>
  print (list(data) ) <br>
  得到一个超级长的列表,每个Observation元素代表一行数据，其中还夹杂着子元素，<br>  
 遍历—替换代码：<br>
  for observation in data:<br>
  for item in observation:<br>
  print(item)得到Dim 和Value对象<br>
替换成 print(list(item))可以查看有无子元素<br>
调用  print(item.attrib)返回每一个节点的属性<br>
为了显示更清晰：创建数据结构：为每一条数据记录创建一个空字典record添加值对使用append方法将每一条数据记录都添加到一个列表中all_data<br>
得到每个属性字典的键（有多个主键的取第一个）<br>
  lookup-keys = list(item.attrib.keys())  #获取列表<br>
  lookup_key = lookup_keys[0]        #获取列表索引，得到第一个值】<br>
使用item.attrib[lookup_key]返回键对应的值<br><br>

  *	注解： tree = ET.parse(‘’) 指的是整个XML对象，以Python能够理解并解析的方式保存<br>
