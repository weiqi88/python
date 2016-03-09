#coding=utf-8
from sys import argv
script,filename = argv #第一个参数获取当前的文件名，第二个获取的是传入的第一个参数

print "We're going to erase %r."%filename #获取文件名
print "If you don't want that,his CTRL-C(^c)."
print "If you do want that,hit RETURN."#如果希望执行回车

raw_input("?")#回车

print "opening the file.."
target =open(filename,'w')#读写模式打开文件

print "Truncating thr file.Goodbye!"

target.truncate()#清空文件

print"Now I'm going to ask you for three lines."
#接受输入
line1 = raw_input('line 1 :')
line2 = raw_input('line 2 :')
line3 = raw_input('line 3 :')

print"I'm going to write these to the file."

target.write(line1)#把变量的值写入文件中
target.write("\n")#换行
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally,we close it."

target.close()#关闭文件