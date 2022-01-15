# PyHaxx

<details>
<summary>Object Oriented Programming</summary>
<h3> Object: </h3>
<pre>
An object is simply a collection of data (variables) and methods (functions) that act on those data.
A parrot is an object, as it has the following properties: name, age, color as attributes and singing, dancing as behavior.
An object is also called an instance of a class and the process of creating this object is called instantiation.
The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).
</pre>
<h3>Class:</h3>
<pre>
A class is a blueprint for the object.
We can think of class as a sketch of a parrot with labels. 
It contains all the details about the name, colors, size etc. Based on these descriptions, we can study about the parrot. 
Here, a parrot is an object. From class, we construct instances. 
An instance is a specific object created from a particular class.
When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.
</pre>
<h3>Methods:</h3>
<pre>
Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.
</pre>
<h3>Inheritance:</h3>
<pre>
Inheritance is a way of creating a new class for using details of an existing class without modifying it. 
The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).
<br>
  class BaseClass:
  Body of base class
  class DerivedClass(BaseClass):
  Body of derived class
  
</pre>
  <h3>Method Overriding</h3>
  <pre>
  Generally when overriding a base method by a derived method, we tend to extend the definition of base method rather than replacing it.
  </pre>
  
  <h3>Multiple Inheritance</h3>
  <pre>
  A class can be derived from more than one base class in Python, similar to C++. This is called multiple inheritance.
  In multiple inheritance, the features of all the base classes are inherited into the derived class. 
  <br>
    class Base1:
      pass
    class Base2:
      pass
    class MultiDerived(Base1, Base2):
      pass
<!--     ![Capture](https://user-images.githubusercontent.com/59027621/149613631-b3f75f37-61bb-4c7a-b738-2af5d5c3061a.JPG) -->
  </pre>
  <h3>Multilevel Inheritance</h3>
  <pre>
  We can also inherit from a derived class. This is called multilevel inheritance. It can be of any depth in Python.
In multilevel inheritance, features of the base class and the derived class are inherited into the new derived class.
  <br>
  class Base:
    pass
  class Derived1(Base):
    pass
  class Derived2(Derived1):
    pass
  </pre>
  
<h3>Encapsulation</h3>
<pre>
Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
</pre>
  <h3>Polymorphism</h3>
  <pre>
  Polymorphism allows the same interface for different objects.
  Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.
  </pre>
    
</details>
<details>
  <summary>Dictionary</summary>
</details>
<details>
  <summary>Lists</summary>
</details>
<details>
  <summary>Working with external libraries</summary>
</details>
<details>
  <summary>Exceptions</summary>
</details>
<details>
  <summary>Itertools</summary>
</details>
<details>
  <summary>Map</summary>
</details>
<details>
  <summary>Filter</summary>
</details>


## Motivation ^_^

I know learning a new thing needs the answer to “WHY SHOULD I EVEN LEARN THIS STUFF? HOW CAN I APPLY THIS LEARNING IN PRACTICAL LIFE?”. So here we go for the answer now..

Python is necessary not only for software devs but also for an accountant, an economic expert, a marketer, a finance expert, a genetic engineer and also for higher study enthusiasts.

A common question of newbie programmers these days is  why should I learn python first instead of C/C++?
The simple answer starts with a simple question “Why Shouldn’t You?”  

> Python is easy to learn compared to C, C++ or java. It is one of the top programming languages of 2021.

> Python has a wide range of libraries which are used in big projects. These library functions are customizable.

> Python is an open source language meaning you can develop library functions of python yourself.

> Python supports cross platform development. What is cross platform development? If you develop an android application it would work in IOS as well. Even if you develop a desktop application it can be executed in any operating systems WINDOWS or LINUX

> Python has two very famous frameworks for backend development. Flask and Django (read it jango). So for job preparation one can prepare him/herself learning any of the two frameworks very well. 

> In higher studies , in different sectors python is needed badly. Such as Artificial Intelligence, Machine learning, Data Science.

> The job sector for python is huge. You can be a web dev, software dev, data scientist, business analyst, ML engineer, game dev, network programmer and what not. 

So if you excel in only one programming language python, then your career will have the boost it needs for sure <3.

## Resources

- [Programiz (the easiest explanation so far according to me)](https://www.programiz.com/python-programming)
- [Geeksforgeeks](https://www.geeksforgeeks.org/python-programming-language/?ref=shm)
- [Real Python](https://realpython.com/start-here/)
- [Python 3.10.0 tutorial documentation](https://docs.python.org/3.10/tutorial/index.html)
- [Kaggle](https://www.kaggle.com/learn)
- [Playlist of mahmudul haque bhaiya for MIC python course(last year)](https://www.youtube.com/watch?v=_8I1ZeHgZmQ&list=PLuNlCVN6bOLOaZWFM2MMfauagHqNXgDzs)
- [freecodecamp](https://www.youtube.com/watch?v=rfscVS0vtbw)
- [Sumon's Acamedy](https://www.youtube.com/watch?v=GGO_h-P2TPk)

## Practise Problems

- [Github repo - Python-programming-exercises](https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises%20for%20Python%203.md)
- [Hackerrank](https://www.hackerrank.com/domains/python)
- [W3school](https://www.w3schools.com/python/default.asp)
