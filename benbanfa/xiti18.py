#coding=utf-8
#this one is like your scrtpts with orgv
#def 命令创建一个函数 ，紧接着是函数的名称
def print_two(*args):#然后我们告诉函数我们需要(*args)才能正常工作
	arg1,arg2 = args#将参数解包
	print "arg1:%r,arg2:%r"%(arg1,arg2)
#ok,that *args is actually pointless,we can just do this

def print_two_again(arg1,arg2):
	print"arg1:%r,arg2:%r"%(arg1,arg2)

#This just takes one argument

def print_one(arg1):
	print "arg1:%r"%arg1

def print_none():#不接受任何参数
	print "I got nothin'."
	
print_two('wei','qi')
print_two_again('wei','qi')
print_one('First')
print_none()