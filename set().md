set函数:<br><br><br>

是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key<br>

set可以看成数学意义上的无序和无重复元素的集合<br><br>


使用方法：<br>
set1.intersection（set2）：交集<br>
union：并集<br>
difference：差<br>
in：判断是否在内<br><br>


set.add()可用来添加函数<br>
set.remove()可用来删除函数，一旦删除异常（删除多次或删除的对象不存在--可以用来检验数据的唯一性）就会报错<br>
set.discard()是remove()函数的友好版，只当存在的时候删除<br>
set.copy()赋值操作，返回set的副本<br>
frozenset()与set方法相似，返回的是不可变集合<br><br>
