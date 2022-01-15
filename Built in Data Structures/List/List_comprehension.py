# List Comprehension: Elegant way to create Lists

# List comprehension is an elegant and concise way to create a new list from an existing list in Python.

#output:
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
pow2 = [2 ** x for x in range(10)]
print(pow2)

#or 
# pow2 = []
# for x in range(10):
#   pow2.append(2 ** x)
# print(pow2)
pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)
odd = [x for x in range(20) if x % 2 == 1]
print(odd)

# List Membership Test
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# Output: True
print('p' in my_list)

# Output: False
print('a' in my_list)

# Output: True
print('c' not in my_list)

# Iterating Through a List
for fruit in ['apple','banana','mango']:
    print("I like",fruit)
