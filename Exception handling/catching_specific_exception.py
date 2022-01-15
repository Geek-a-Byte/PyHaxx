# In the above example, we did not mention any specific exception in the except clause.
# This is not a good programming practice as it will catch all exceptions and handle every case in the same way. 
# We can specify which exceptions an except clause should catch.
# A try clause can have any number of except clauses to handle different exceptions, however, only one will be executed in case an exception occurs.


# try:
#    # do something
#    pass

# except ValueError:
#    # handle ValueError exception
#    pass

# except (TypeError, ZeroDivisionError):
#    # handle multiple exceptions
#    # TypeError and ZeroDivisionError
#    pass

# except:
#    # handle all other exceptions
#    pass


# raise KeyboardInterrupt
# raise MemoryError("This is an argument")

# In Python programming, exceptions are raised when errors occur at runtime. We can also manually raise exceptions using the raise keyword.
# We can optionally pass values to the exception to clarify why that exception was raised.

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
