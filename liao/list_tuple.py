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