#coding=utf-8
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "Copying from %s to %s "%(from_file,to_file)#复制 某个文件到某个文件

#we could do these two on one line too,how?
input = open(from_file)#打开文件
indata = input.read()#读取输入内容,在此处读写from_file的文件内容

print "the input file is %d bytes long"%len(indata)#获取内容长度
#exists 将文件名字符串作为参数，如果文件存在返回True，否则返回False，并创建文件
print "Does the output file exist? %r"%exists(to_file)



output = open(to_file,'w')#打开to_file文件进行读写

output.write(indata)#把indata写入文件to_file中

print "Alright,all done."

output.close()#关闭to_file文件

input.close()#关闭input文件