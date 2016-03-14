#coding=utf-8
the_things = "Apples Oranges Crows Telephone Light Sugar"

stuff = the_things.split(' ')

more_stuff = ['Day','Night','Song','Frisbee','Corn','Banana','Girl','Boy']

while len(stuff) != 10:
	next_one = more_stuff.pop()#没有参数代表从最后一个参数取值
	print "Adding:",next_one
	stuff.append(next_one)#把从more_stuff取出的值追加进 stuff 列表中
	print "There's %d items now."%len(stuff)
	
print "There we go:",stuff

print "Let's do some things with stuff."
	
print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)#,join()函数主要用来拼接字符串,
a = stuff[3:5]#后面一个数字代表截止位置

print a
print '#'.join(stuff[3:6])#使用#链接两个字符串