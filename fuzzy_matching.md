1.	模糊匹配<br>
 适用于：处理不止一个数据集或是为标准化的脏数据<br>
可以判断两个元素是否相同，如判断“My dog & I”和”me and my dog”意思相近<br>
<br>
	安装库：<br>
	pip install  fuzzywuzzy<br>
	处理的脏数据，可能是输入时粗心，也可能是用户输入是导致的数据中包含的拼写错误和较小的语法错误和句法偏移<br>
.ratio函数：<br>
接受两个字符串作比较。返回的是两个字符串序列的相似程度（1~100）<br>
.partial_ratio函数：<br>
接受两个字符串作比较，返回的是匹配程度最高的子字符串序列的相似程度（1~100）<br>
.partial_token_sort_ratio函数：<br>
匹配字符串时不考虑单词的顺序，每个字符串都是先排序后比较，每个字符串都是先排序然后再比较，<br>
所以如果包含相同的单词但顺序不同，也是可以匹配的<br>
.partial_token_set_ratio:对排序后的标记尝试寻找最佳匹配，返回这些标记相似的比例<br>
缺点：可能会出现错误匹配<br>
	如果计算相似度的字符串只有字母和数字，直接可以用ratio（）和partial_ratio()。<br>
但如果还有其他字符，而且我们想要去掉这些没用字符，就用partial_token_sort_ratio和partial _token_set_ratio，对顺序不敏感，<br>
但partial _token_sort_ratio系列是全字符匹配，不管顺序。<br>
而partial _token_set_ratio只要第二个字符串包含第一个字符串就100,不管顺序。<br>
	process模块：<br>
.extract(Str,List,limit=2)将字符串与可能匹配的列表依次比较，返回列表中2个可能的匹配<br>
.extractOne(Str,List)返回列表中与字符串对应的最佳匹配<br>
