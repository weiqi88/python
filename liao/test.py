#coding=utf-8
from collections import Iterable

L = ['Hello', 'World',18, 'Apple', None]
b=[]
a=[]

for x in L:
	if isinstance(x,Iterable):
		a.append(x)
		b = [s.lower() for s in a]
	else:
		print x
		b.append(x)
print b