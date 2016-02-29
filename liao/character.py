#coding=utf-8
print 'i\'m\ "ok\"'
print'I\'m learning\nPython'
print '\\\n\\'
print '\\\t\\'
print r'\\\t\\'
print '''line1
line2
line3
'''

print 3>2
print 3>5
print 3>2 or 3>1
print 3>2 or 3>4
print 3>4 or 3>4
print not 3>2 
print not 3>2
print not 3>4
print '............'
if False:
	print '123'
else:
	print 'abc'
	
a='ABC'
b=a
a='XYZ'
print 'a='+a,'b='+b

print u'ABC'

print u'ABC'.encode('utf-8')
#把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法：
print u"中文".encode('gbk')
#在字符串内部，%s表示用字符串替换,如果只有一个%?，括号可以省略
print 'Hello,%s'%'word'
a ='weiqi'
d=100
#%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好
print 'Hi,%s,you have $%d'%(a,d)
#格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print '%2d-%02d'%(3,1)# %2d代表两位，但传入值是3所以前面空一位，%02d代表补零所以结果是01
print '%.2f'% 3.1415926 # .2 代表保留两位小数
#对于Unicode字符串，用法完全一样，但最好确保替换的字符串也是Unicode字符串：
print  u'Hi, %s' % u'Michael'
#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print 'growth rate: %d %%'%7
