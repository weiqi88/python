#coding=utf-8
classmates=['zhangsan','lisi','wanger']
print classmates
#用len()函数可以获得list元素的个数
a=len(classmates)
print a 
print classmates[0]
print classmates[1]
print classmates[2]
#直接获取最后一个元素
print classmates[-1]
#追加元素到末尾
classmates.append('zhaoliu')
print classmates
#把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1,'wangwu')
print classmates
#删除list末尾的元素，用pop()方法
classmates.pop()
print classmates
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
print classmates

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1]='weiqi'
print classmates
#list元素也可以是另一个list
s=['python','java',['asp','php'],'c']
print len(s)
#要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组
print s[2][0]
print s[2][1]

classmates=('wangyi','wanger','wangsan')
print classmates
'''只有1个元素的tuple定义时必须加一个逗号,
定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号
'''
classmates =(1,)
print classmates

#'可变的'tuple,变的不是tuple的元素，而是list的元素
classmates=('A','B',['C','D'])
print classmates
classmates[2][0]='X'
classmates[2][1]='Y'
print classmates

# 请用索引取下面的指定元素
L =[
['Apple','Goglle','Microsoft'],
['JAVA','Python','Ruby','PHP'],
['Adam','Bart','Lisa']
]
print u'打印Apple:'+L[0][0]
print u'打印Python:'+L[1][1]
print u'打印Lisa:'+L[2][2]