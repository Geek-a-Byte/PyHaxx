# program to print the reciprocal of even numbers
# In some situations, you might want to run a certain block of code if the code block inside try ran without any errors.
# For these cases, you can use the optional else keyword with the try statement.
try:
    num = int(input("Enter a number: "))
    # An assert statement checks whether a condition is true. If a condition evaluates to True, a program will keep running.
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

# 1 4 0
