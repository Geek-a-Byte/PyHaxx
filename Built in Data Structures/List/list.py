# Python lists are one of the most versatile data types that allow us to work with multiple elements at once.
# a list of programming languages
# ['Python', 'C++', 'JavaScript']

# list of integers
my_list = [1, 2, 3]

# empty list
my_list = []

# list with mixed data types
my_list = [1, "Hello", 3.4]

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]


my_list = ['p', 'r', 'o', 'b', 'e']

# first item
print(my_list[0])  # p

# third item
print(my_list[2])  # o

# fifth item
print(my_list[4])  # e

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# remember indexing starts at 0
# Nested indexing
print(n_list[0])
print(n_list[0][1])
print(n_list[1][3])

# Negative indexing
# Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.
# Negative indexing in lists

my_list = ['p','r','o','b','e']

# last item
print(my_list[-1])

# fifth last item
print(my_list[-5])

# List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','z']

# elements from index 2 to index 4
print(my_list[2:5])

# elements from index 5 to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])

# When we slice lists, the start index is inclusive but the end index is exclusive. For example, my_list[2: 5] returns a list with elements at index 2, 3 and 4, but not 5.

# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

print(odd)

# Appending and Extending lists in Python
# We can add one item to a list using the append() method or add several items using the extend() method.
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)


# We can also use + operator to combine two lists. This is also called concatenation.

# Concatenating and repeating lists
odd = [1, 3, 5]

print(odd + [9, 7, 5])

# The * operator repeats a list for the given number of times.
print(["re"] * 3)

# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2]

print(my_list)

# delete multiple items
del my_list[1:5]

print(my_list)

# delete the entire list
del my_list

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)

# Example on Python list methods

my_list = [3, 8, 1, 6, 8, 8, 4]

# Add 'a' to the end
my_list.append('a')

# Output: [3, 8, 1, 6, 0, 8, 4, 'a']
print(my_list)

# Index of first occurrence of 8
print(my_list.index(8))   # Output: 1

# Count of 8 in the list
print(my_list.count(8))  # Output: 3 

# Error! Only integer can be used for indexing
print(my_list[4.0])
