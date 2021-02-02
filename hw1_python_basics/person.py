#!/usr/bin/env python

class person:

	def __init__(self,name,age,height):
		self.name=name
		self.age=age
		self.height=height

new_person = person(name='Joe', age=34, height=184)
print("{:} is {:} years old.".format(new_person.name, new_person.age))
	
		
	def __repr__(self):
		return f'{self.name} is {self.age} years old and {self.height} cm tall'


print(new_person.__repr__())




  

