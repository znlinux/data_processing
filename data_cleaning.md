1.	数据清洗：修改数据使其满足新的标准化数据格式<br>
  MICS上原始数据是SPSS格式或.sav文件<br><br>
利用PSPP查看（https://www.gnu.org/software/pspp）<br>
R命令转换成.csv文件（http://bethmcmillan.com/blog/?p=1073）<br>
  应该该弄清楚需要清洗的数据具体是什么含义<br>
2.	替换标题（提高标题可读性）<br>
  将短标题替换成易于理解的长标题<br><br>
3.	列表生成式函数<br>
    [func(x) for x in iter_x]<br>
  将可迭代对象iter_x的每一行或每一个值传入func(x)，用返回值创建一个新的列表<br>
 * 实例：<br>
    #导入csv文件，DictReader为可迭代对象<br>
    from csv import DictReader<br>
    #打开csv文件<br>
    data_rd = DictReader(open('data/mn.csv','rt',encoding="utf-8"))<br>
    #生成一个新的列表<br>
    data_rows = [d for d in data_rd]<br><br>
4.	if dkey in head_dict.values()利用字典的values方法，返回仅由字典的值组成的列表<br><br>
5.	if * in *判断某一对象是否包含在某个列表中。<br><br>
6.	查看数据字典的每一个键值对，使用的是items方法<br>
    for dkey,dval in data_dict.items():<br><br>
