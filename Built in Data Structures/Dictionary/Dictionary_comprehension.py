# Dictionary comprehension consists of an expression pair (key: value) followed by a for statement inside curly braces {}.

# Dictionary Comprehension
squares = {x: x*x for x in range(6)}
print(squares)
# or
squares = {}
for x in range(6):
    squares[x] = x*x
    # print(x,end=' ')
print(squares)
# print(end='\n')
# An optional if statement can filter out items to form the new dictionary.

# Dictionary Comprehension with if conditional
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares)
