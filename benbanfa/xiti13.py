#coding=utf-8
from sys import argv
# 将argv，给每个参数一个变量名

script,first,second,third=argv
'''
在输入命令的时候用：python ex13.py 1 2 3 类似这样的命令格式就可以了。在运行python
的时候就直接把参数都输入了，就不会报错了。
'''
print 'The script is called:',script
print 'Your first variable is:',first
print 'Your second variable is:',second
print 'Your third variable is:',third
