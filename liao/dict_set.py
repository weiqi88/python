#coding=utf-8
#dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩
d={'wangyi':95,'wannger':99,'wangsan':59}
print d['wangyi']

#数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['wangsi']=67
print d['wangsi']

# 如果key不存在，则dict就会报错
# 通过in判断吧key是否存在
print ('aa' in d)
print ('wangsi' in d)
#dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print d.get('aa')
print d.get('aa',1)
print d.get('aa')
print (d.get('wangsi'))
#需要牢记的第一条就是dict的key必须是不可变对象

#et和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s = set([1,2,3])
print s
#重复元素在set中自动被过滤：
s = set([1,1,22,2,3,4])
print s 

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(5)
print s
s.add(4)
print s
#通过remove(key)方法可以删除元素
s.remove(1)
print s
#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([1,2,4]) 
print (s1&s2)#交集
print (s1|s2)#并集

#str是不变对象，而list是可变对象
#对于可变对象，比如list，对list进行操作，list内部的内容是会变化的
a =['c','b','a']
a.sort()
print a

#而对于不可变对象，比如str，对str进行操作呢

a='abc'
print a.replace('a','A')
print a
