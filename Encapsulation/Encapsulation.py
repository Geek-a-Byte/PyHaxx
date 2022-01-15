class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price ## but the private attr can be accessed from within the class

## creating an object 
c = Computer() ## calling the constructor, so c has an private attr called maxprice.
c.sell()

# change the price
c.__maxprice = 1000 ## as it is a private attr it cannot be accessed/changed from main function
c.sell()

# using setter function
c.setMaxPrice(1000) ## the method defined in the class is public so it can be accessed from main
c.sell()
