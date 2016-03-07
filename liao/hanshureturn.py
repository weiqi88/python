#coding=utf-8
#实现一个可变参数的求和
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax +n
	return ax

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax =ax+n
		return ax 
	return sum

f =lazy_sum(1,3,5,7,9)
print f()

def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
#返回函数不要引用任何循环变量，或者后续会发生变化的变量
#全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，
#它们所引用的变量i已经变成了3，因此最终结果为9。
f1,f2,f3 = count()
print f1(),f2(),f3() 
			
	