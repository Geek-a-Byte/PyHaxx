# The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns an iterator.
numbers_list = [2, 4, 6, 8, 10]
numbers_set = (1, 2, 3, 4)
# returns square of a number
def square(number):
  return number * number

# apply square() function to each item of the numbers list and set
result_list = map(square, numbers_list)
result_set = map(square, numbers_set)
print(result_list)
print(result_set)

# converting to list and set
squared_numbers_list = list(result_list)
squared_numbers_set = list(result_set)
print(squared_numbers_list)
print(squared_numbers_set)
