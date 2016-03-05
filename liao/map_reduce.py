#coding=utf-8
def f(x):
	return x*x
#map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到
#序列的每个元素，并把结果作为新的list返回
L = map(f,range(10))
print L

L = map(str,range(10)) #把所有的数字转换为字符串
print L
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函
#数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#  reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fu(x,y):
	return x*10+y

a=reduce(fu,[1,3,5,7,9])
print a

a=reduce(fu,range(10))
print a