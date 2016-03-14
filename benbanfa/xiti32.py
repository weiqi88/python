#coding=utf-8
hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weights = [1,2,3,4]
the_count = [1,2,3,4,5]
fruits = ['apples','orangs','pears','aprictos']
change = [1,'pennies',2,'dimes',3,'quarters']
#this first kind of for-loop goes through a list 
for number in the_count:#把the_count从第一个开始每循环一次赋值给number一次
	print "This is count %d"%number

#same as above
for fruit in fruits:
	print "A fruit of typr:%s"%fruit
	
for i in change:
	print "I got %r"%i

elements = []#创建空的数组

for i in range(0,6):
	print "Adding %d to the list."%i
	elements.append(i)#把值追加进数组中

for i  in elements:#取出数组中的词并打印
	print "Element waas:%d"%i
	
elements=range(10)

for i  in elements:#取出数组中的词并打印
	print "Element waas:%s"%i