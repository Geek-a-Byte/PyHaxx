# Iterating Through a Dictionary

# Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])

# Dictionary Built-in Functions
squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# returns true if the dictionary is empty
# Output: False
print(all(squares))

# If the dictionary is empty, returns False.
# Output: True
print(any(squares))

# Return the length (the number of items) in the dictionary.
# Output: 6
print(len(squares))

# Return a new sorted list of keys in the dictionary.
# Output: [0, 1, 3, 5, 7, 9]
print(sorted(squares))
