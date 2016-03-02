#coding=utf-8
names =['wangyi','wanger','wangsan']
#for x in ...循环就是把每个元素代入变量x
for i in names:
	print i

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum
#range(101)就可以生成0-100的整数序列
sum = 0
for x in range(101):
    sum = sum + x
print sum
#计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum
#从raw_input()读取的内容永远以字符串的形式返回,必须先用int()把字符串转换为我们想要的整型
birth = int(raw_input('birth: '))
if birth < 2000:
    print u'00前'
else:
    print u'00后'