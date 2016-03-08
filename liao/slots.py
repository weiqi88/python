#coding=utf-8
from types import MethodType

class Student(object):
	pass
	
#给实例绑定一个属性
s = Student()
s.name='weiqi'

print s.name



#给实例绑定一个方法：
def set_age(self,age):#定义一个函数作为实例方法
	self.age=age


s.set_age = MethodType(set_age,s,Student)#给实例绑定一个方法，把 set_age方法绑定到实例Student,s上
s.set_age(25)#调用实例方法 ，调用set_age方法
print s.age



