class Parrot:
    ## docstring is a brief description of the class. Although not mandatory, this is highly recommended.
    '''This is a docstring. I have created a new class'''
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

# In the above program, we created a class with the name Parrot. Then, we define attributes. The attributes are a characteristic of an object.
# These attributes are defined inside the __init__ method of the class. It is the initializer method that is first run as soon as the object is created.
# Then, we create instances of the Parrot class. Here, blu and woo are references (value) to our new objects.
# We can access the class attribute using __class__.species. Class attributes are the same for all instances of a class. Similarly, we access the instance attributes using blu.name and blu.age. However, instance attributes are different for every instance of a class.
