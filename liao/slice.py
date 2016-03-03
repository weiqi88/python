#coding=utf-8
L=['weiqi1','weiqi2','weiqi3','weiqi4','weiqi5','weiqi6','weiqi7','weiqi8']
r=[]
n=3
# 取前3个元素
for i in range(n):#range 只有一个参数的时候代表取前几个自然数
	r.append(L[i])
	
print r

#对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作
print L[0:3] #[0:3]表示从索引0开始取，直到索引3，但不包括3

#既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print L[-2:]  #记住倒数第一个元素的索引是-1

L =range(100)

#前11-20个数
print L[10:20]

# 前10个数，每隔两个曲一个
print L[0:10:2]

# 所有数每5个去一个
print L[::5]
