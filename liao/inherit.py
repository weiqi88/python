#coding=utf-8
class Animal(object):
	def run(self):
		print 'Animal is running...'

#最大的好处是子类获得了父类的全部功能
class Dog(Animal):
	def run(self):
		print 'Dog is running...'
	def eat(self):
		print 'Eating meat...'
		
class Cat(Animal):
	pass

dog =Dog()
#多态:当子类和父类都存在相同的run()方法时,子类的run()覆盖了父类的run()
dog.run()
dog.eat()

#继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，
#也可以把父类不适合的方法覆盖重写
def run_twice(animal):
	animal.run()
	animal.run()
run_twice(Animal())
run_twice(Dog())