#coding=utf-8
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print "You have %d cheeses!"%cheese_count
	print "You have %d boxes of crackers"%boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print"We can just give the function numbers directly:"

cheese_and_crackers(20,30)#调用函数 cheese_and_crackers

print"OR,we can use variables from our script:"
amount_of_chesse = 10 #给变量赋值
amount_of_crackers = 50

cheese_and_crackers(amount_of_chesse,amount_of_crackers)#调用函数 并把变量传入函数

print "We can even do math inside too"

cheese_and_crackers(10+20,5+6)#调用函数，参数可进行计算

print "and we can combine the two ,variables and math:"

cheese_and_crackers(amount_of_chesse+100,amount_of_crackers+1000)#调用函数，变量可与数字进行计算