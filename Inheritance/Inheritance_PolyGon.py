class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        # it will create a list and append a 0 for every side
        self.sides = [0 for i in range(no_of_sides)] 
        ## list comprehention
        #  self.sides = []
        #  for i in range(no_of_sides):
        #     self.sides.append(0)
 
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) 
        for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
        
t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()


print(isinstance(t,Triangle))
print(isinstance(t,Polygon))
print(isinstance(t,int))
print(isinstance(t,object))
print(issubclass(Polygon,Triangle))
print(issubclass(Triangle,Polygon))

# Method Overriding in Python
# In the above example, notice that __init__() method was defined in both classes, Triangle as well Polygon. 
# When this happens, the method in the derived class overrides that in the base class. This is to say, __init__() in Triangle gets preference over the __init__ in Polygon.
# Generally when overriding a base method, we tend to extend the definition rather than simply replace it. 
# The same is being done by calling the method in base class from the one in derived class (calling Polygon.__init__() from __init__() in Triangle).
# A better option would be to use the built-in function super(). 
# So, super().__init__(3) is equivalent to Polygon.__init__(self,3) and is preferred.
# Two built-in functions isinstance() and issubclass() are used to check inheritances.
# The function isinstance() returns True if the object is an instance of the class or other classes derived from it. 
# Each and every class in Python inherits from the base class object.
