#coding=utf-8
from sys import argv 

script,filename=argv
#上面是获取文件名
txt =open(filename)#打开文档
print script
print "Here's your file %r:"%filename

print txt.read()#让文件执行读命令
txt.close()
print "Type the filename again:"
file_again=raw_input('>')#输入文件名
txt_again = open(file_again)#打开文件

print txt_again.read()
txt_again.close()