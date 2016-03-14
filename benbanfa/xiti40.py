#coding=utf-8
things = ['a','b','c','d']
print things[1] #打印数组的第二个元素

things[1]='z'#给数组第二个元素赋值
print things[1]

stuff ={'name':'weiqi','age':27,'height':6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']
stuff['city'] = 'xian'#给dict增加元素
print stuff['city']
stuff[1] = 'WOW'
stuff[2] = "Neato"
print stuff[1]
print stuff[2]
print stuff
del stuff ['city'] #删除元素
del stuff [1] #删除元素
del stuff [2] #删除元素
print stuff

cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}

cities['NY'] = "New York"
cities['OR'] = 'Portland'

def find_city(themap,state):
	if state in themap:#在themap查找state
		return themap[state]#找到的话返回
	else:#找不到的话执行下面的语句
		return "Not found"

#ok pay attention
cities['_find'] = find_city #把find_city返回的值添加进cities,并标记为'_find'

while True:
	print "State?(ENTER to quit)",
	state = raw_input('>')
	
	if not state:
		print bool(state)
		break#state如果是空值，bool(state)返回值是flase
	
	#this line is the most important ever!study!
	city_found = cities['_find'](cities,state)
	print city_found
		