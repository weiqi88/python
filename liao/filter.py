#coding=utf-8
#filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的
#函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#在一个list中，删掉偶数，只保留奇数，可以这么写
def is_odd(n):
	return n%2 ==1

print filter(is_odd,[1,2,4,5,6,9,10,15]) #返回为true保留该元素

#把一个序列中的空字符串删掉，可以这么写：

def not_empty(s):
	return s and s.strip()

print filter(not_empty,['A','','B',None,'C','  '])