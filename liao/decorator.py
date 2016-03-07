#coding=utf-8
import functools
def now():
	print '2013-12-25'

f = now 
f()
#函数对象有一个__name__属性，可以拿到函数的名字
print now.__name__
print f.__name__
#函数对象有一个__name__属性，可以拿到函数的名字

#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

def log(func):
	def warpper(*args,**kw):
		print 'call %s():' % func.__name__
		return func(*args,**kw)
	return warpper

@log
def now():
	print '2013-12-25'
now()


#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂
def log(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print '%s %s():'%(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print '2014-03-07'

now()