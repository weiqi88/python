#coding=utf-8
from collections import Iterable
d ={'a':1,'b':2,'c':3}

# 默认dict迭代的是key
for  key in d:
	print key
	
# 迭代value

for value in d.itervalues():
	print value
	
# 同时迭代key和value
for v,k in d.iteritems():
	print v,k
#判断一个对象是可迭代对象,方法是通过collections模块的Iterable类型判断

print isinstance('abc',Iterable)#str是否可迭代，Ture是可迭代

print isinstance(123,Iterable)

#要对list实现类似Java那样的下标循环怎么办，Python内置的enumerate函数可以把一个
#list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(['a','b','c']):
	print i,value