#coding=utf-8
from sys import argv
script,input_file=argv #获取argv的参数

def print_all(f):
	print f.read()#读取文件内容

def rewind(f):
	f.seek(0)#表示找到文件开始的位置

def print_a_line(line_count,f):
	print line_count,f.readline()#读取文本中的一行

current_file =open(input_file)#打开文件，并把内容赋给 current_file，current_file相当于f

print "First let's print the whole file:\n"

print_all(current_file)#current_file调用print_all函数，相当于f=current_file

print "Now let's rewind,kind of like a tape."

rewind(current_file)#每打印一次，位移1次

print "let's print three lines:"

current_line = 1 #给current_line 赋值

print_a_line(current_line,current_file)#给print_a_line 传值，1和文件内容，那么打印出来的时候是1 和文件第一行

current_line =current_line+1#给current_line 赋值，此时给current_line 赋值=2
print_a_line(current_line,current_file)#给print_a_line 传值，2和文件内容，那么打印出来的时候是2 和文件第二行

current_line = current_line+1
print_a_line(current_line,current_file)