#coding=utf-8
names = ['Michael', 'Bob', 'Tracy']
#所以for x in ...循环就是把每个元素代入变量x
for name in names:
	print name
'''要计算1-100的整数之和，从1写到100有点困难
Python提供一个range()函数，可以生成一个整数序列，比如range(5)生成的序列是从0开始小于5的整数：
'''
s=range(101)
sum = 0
for x in s:
	sum=sum+x
print sum

sum = 0
n =99
while n>0:
	sum=sum+n
	n=n-2
print sum

sum = 0
n =99
if n >0:
	for x in n:
		sum=sum+x
		n=n-2
print sum