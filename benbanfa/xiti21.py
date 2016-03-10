#coding=utf-8
def add(a,b):
	print 'ADDING %d +%d '%(a,b)
	return a+b
def subtract(a,b):
	print"SUBTRACTING %d -%d"%(a,b)
	return a-b

def multiply(a,b):
	print "MULTIPLYING %d *%d"%(a,b)
	return a*b
	
def divide(a,b):
	print "DIVIDING %d /%d"%(a,b)
	return a/b

print "Let's go some matn with just functions"

age = add(30,5)#返回6
height = subtract(78,4)#返回74
weight = multiply(90,2)#返回180
iq = divide(100,2)#返回50

print "Age:%d,Height:%d,Weight:%d,IQ:%d"%(age,height,weight,iq)

print "Here is a puzzle."

what = add (age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes:",what,"Can you do it by hand?"
