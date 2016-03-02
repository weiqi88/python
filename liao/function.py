#coding=utf-8
#比较函数cmp(x, y)就需要两个参数，如果x<y，返回-1，如果x==y，返回0，如果x>y，返回1
import math
print cmp(1,2)
print cmp(2,1)
print cmp(2,2)

print unicode(100)

#定义一个函数要使用def语句,依次写出函数名、括号、括号中的参数和冒号:

def abs(x):
	if x>=0:
		return x
	else:
		return -x
a = abs(-3)		
print a

#如果想定义一个什么事也不做的空函数，可以用pass语句
#实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass

#修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance实现

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError(u'数据类型错误')
	if x>=0:
		return xrange
	else:
		return -x
		
a = my_abs(4)		
print a


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
	
x,y =move(100,100,60,math.pi/6)
print x,y

#返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一
#个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
r = move(100, 100, 60, math.pi / 6)
print r
