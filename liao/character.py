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
print u"中文".encode('gbk')