# materials from www.liaoxuefeng.com

class Student(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score


	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

bart = Student('Bart Simpson', 59)
bart.print_score()

#print(bart.__name)
#AttributeError: 'Student' object has no attribute '__name'

print(bart._Student__name)
#Bart Simpson

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	pass

class Cat(Animal):
	pass

dog = Dog()
dog.run()

class Dog(Animal):
	name = 'Doggie'
	def run(self):
		print('Dog is running...')

	def eat(self):
		print('Dog is eating...')

	def __len__(self):
		return 100

dog = Dog()
dog.run()
print(dog.name)
print(Dog.name)

print(len(dog))
print(dir(dog))
print(hasattr(dog, 'test'))
setattr(dog, 'test', 'haha')
print(hasattr(dog, 'test'))
print(dog.test)
print(getattr(dog, 'test'))

print(isinstance(3,int))
#True
print(isinstance(dog, Dog))
#True
print(isinstance(dog, Animal))
#True

import types
def fn():
	pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)


'''
__slots__
'''

class Student(object):
	pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
	self.age = age

s.set_age = types.MethodType(set_age, s)
s.set_age(25)
print(s.age)

# s2 = Student()
# s2.set_age(25)
# AttributeError: 'Student' object has no attribute 'set_age'

Student.set_age = set_age

s2 = Student()
s2.set_age(26)
print(s2.age)

#limit attributes of class
class Student(object):
	__slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25

# s.score = 99
# AttributeError: 'Student' object has no attribute 'score'

# not available for child class
class Graduate(Student):
	pass

g = Graduate()
g.score = 9999

''' 
@property
making method work as attribute
if no setter, read only
'''

class Student(object):
	
	def get_score(self):
		return self._score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must betweeb 0 - 100!')
		self._score = value

s = Student()
s.set_score(60)
print(s.get_score())

#s.set_score(999)

class Student(object):
	
	@property
	def birth(self):
		return self._birth

	@birth.setter	
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2017 - self._birth

s = Student()
s.birth = 1995
print(s.birth)
print(s.age)