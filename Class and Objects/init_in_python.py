# A Sample class with init method
class Person:
	
	# init method or constructor
	def __init__(self, name):
		self.name = name
	
	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)
	
p = Person('Nikhil')
p.say_hi()

# Understanding the code
# In the above example, a person name Nikhil is created. 
# While creating a person, “Nikhil” is passed as an argument, this argument will be passed to the __init__ method to initialize the object. 
# The keyword self represents the instance of a class and binds the attributes with the given arguments. 
# Similarly, many objects of Person class can be created by passing different names as arguments.
