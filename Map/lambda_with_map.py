# Since map() expects a function to be passed in, lambda functions are commonly used while working with map() functions.

# A lambda function is a short function without a name.

numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
