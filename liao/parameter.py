#coding=utf-8
def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
#计算任意n次方	
a=power(3,3)
print a

#由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
#当我们调用power(3)时，相当于调用power(3, 2)	
a=power(3)
print a
'''
设置默认参数时，有几点要注意：
一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
二是如何设置默认参数。
'''

'''
------------------------默认参数调用方法------------------------
有多个默认参数时，调用的时候，既可以按顺序提供默认参数，比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，
最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。也可以不按顺序提供部
分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', 
city='Tianjin')，意思是，city参数用传进去的值，其他默认参数继续使用默认值。

默认参数必须指向不变对象
'''

# 可变参数
#--非可变参数示例
def calc(number):
	sum =0
	for n in number:
		sum = sum + n*n#相乘后在做加法给予前面赋值
	return sum

# 调用
a = calc([1,2,3]) #组装一个list
print a
#组装一个tuple 
print calc((1,3,5,7))

#-- 可变参数：：：：定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号

def calc(*number):
	sum =0
	for n in number:
		sum = sum + n*n#相乘后在做加法给予前面赋值
	return sum
	
a = calc(1,2,3) #组装一个list
print a
#组装一个tuple 
print calc(1,3,5,7)
#如果已经有一个list或者tuple，可以这样做
nums =[1,2,3]
a = calc(nums[0],nums[1],nums[2])
print a
#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
b =calc(*nums)
print 'b=',b


# 关键字参数
def person(name,age,**kw):
	print 'name:',name,'age:',age,'other:',kw
	
print person('weiqi',30)
print person('weiqi',30,city='xian')

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
kw ={'city':'beijing','job':'test'}
print person('wangyi','22',**kw)