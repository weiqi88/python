#coding=utf-8
class Student(object):
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个
#参数永远是实例变量self，并且，调用时，不用传递该参数
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
		
	def get_grade(self):
		if self.__score>=90:
			print'A'
		elif self.__score >=60:
			print'B'
		else:
			print'C'
#但是如果外部代码要获取name和score,可以给Student类增加get_name和get_score这样的方法
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
#如果又要允许外部代码修改score怎么办？可以给Student类增加set_score方法
	def set_score(self,score):
		if 0<=score<=100:
			self.__score=score
		else:
			raise ValueError('bad score')
	def print_score(self):
		print '%s:%s'% (self.__name,self.__score)
		
		
bart=Student('wei',58)
print bart.get_name()
print bart.get_score()

bart.set_score=90
bart.print_score()
