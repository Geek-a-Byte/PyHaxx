# Self is always pointing to Current Object.
# self represents the instance of the class. 
# By using the “self” keyword we can access the attributes and methods of the class in python. 
# It binds the attributes with the given arguments.


#it is clearly seen that self and obj is referring to the same object
 
class check:
    def __init__(self):
        print("Address of self = ",id(self))
 
obj = check()
print("Address of class object = ",id(obj))
