#coding=utf-8
from collections import Iterable
import os
#生成一个list
list = range(1,11)
print list

#生成[1x1, 2x2, 3x3, ..., 10x10]
L=[]
for x in range(1,11):
	L.append(x*x)
print L
#循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
L = [x*x for x in range(1,12)]  #把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
print L

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
L = [x*x for x in range(1,11) if x%2==00]
print L

L=[m + n for m in 'ABC' for n in 'XYZ']
print L
#上面的可以理解为下面这种形式
L=[]
for m in 'abc':
	for n in 'xyz':
		L.append(m+n)
print L
#列出当前目录下的所有文件和目录名
L = [d for d in os.listdir('D:\\python\\liao')]
print L

#列表生成式也可以使用两个变量来生成list
d ={'x':'A','y':'B','z':'C'}
L =[k+'='+v for k,v in d.iteritems()]
print L

#把所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
a = [s.lower() for s in L]
print a

#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法,可采用下面方法
