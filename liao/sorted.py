#coding=utf-8
print sorted([36,5,12,9,21])

#sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。
#比如，如果要倒序排序，我们就可以自定义一个reversed_cmp函数
def reversed_cmp(x,y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0
print sorted([36,5,12,9,21],reversed_cmp)

#忽略大小写，按照字母序排序
def cmp_ignore_case(s1,s2):
	u1=s1.upper() #字符串中的小写字母转为大写字母
	u2=s2.upper()

	if u1 < u2:
		return -1
	if u1 > u2:
		return 1
	return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case)
