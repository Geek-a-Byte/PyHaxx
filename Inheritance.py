# parent class
class Bird:
    
    ## Constructor with instance attributes
    def __init__(self):
        print("Bird is ready")

    ## user defined method of this class
    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
# The child class inherits all the functions of parent class. __init__(), swim(), whoisThis() method.
# the child class can modify the behavior of the parent class. 
# We can see this from the whoisThis() method. Furthermore, we extend the functions of the parent class, by creating a new run() method.

class Penguin(Bird):
    
    def __init__(self):
        # call super() function. This allows us to run the __init__() method of the parent class inside the child class.
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
