#coding=utf-8
age = 20
if age >=18:
	print('your age is ',age)
	print 'adult'

age =3
if age >=18:
	print('your age is ',age)
	print 'adult'
else:
	print('your age is',age)
	print'teenager'
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x=''
if x:
	print 'True'
else:
	print 'False'
'''
这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转
换成整数。Python提供了int()函数来完成这件事情
'''
s = input('birth:')
birth=int(s)
if birth<2000:
	print u'00前'
else:
	print u'00后'
	
'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）
帮小明计算他的BMI指数，并根据BMI指数：
    低于18.5：过轻
    18.5-25：正常
    25-28：过重
    28-32：肥胖
    高于32：严重肥胖
'''

height =1.73
weight =91 
bmi =weight/(height*2)
if bmi <18.5:
	print u'过轻'
elif bmi<25:
	print u'正常'
elif bmi<28:
	print u'过重'
elif bmi<32:
	print u'肥胖'
else:
	print u'严重肥胖'