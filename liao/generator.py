#coding=utf-8

#上面的函数和generator仅一步之遥，要把fib函数变成generator，只需要把print b改为yield b就可以了
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib (max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b =b,b+a
		n=n+1
		
for n in fib (6):
	print n
	
