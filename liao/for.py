#coding=utf-8
names = ['Michael', 'Bob', 'Tracy']
#����for x in ...ѭ�����ǰ�ÿ��Ԫ�ش������x
for name in names:
	print name
'''Ҫ����1-100������֮�ͣ���1д��100�е�����
Python�ṩһ��range()��������������һ���������У�����range(5)���ɵ������Ǵ�0��ʼС��5��������
'''
s=range(101)
sum = 0
for x in s:
	sum=sum+x
print sum

sum = 0
n =99
while n>0:
	sum=sum+n
	n=n-2
print sum

sum = 0
n =99
if n >0:
	for x in n:
		sum=sum+x
		n=n-2
print sum