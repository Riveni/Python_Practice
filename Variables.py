# Variables are pointers that points on object
# Variables in python are dynamic and there is no need to declare them
# since their type is defined while the program run
# each object has a defined type ( int, string, float... )

x = 'object'  # string type
y = "learner"  # string type
z = 5  # int type
w = 5.0  # float type
n = None  # NULL

type(x)  # function that returns variable type

# Output data to screen
print("Hello " + y + "!")

# Input data to variable
x = input("text you can print:")  # input defined as string!

# Casting: converting variable from one type to another
y = int(x)  # cast string to int

# Switching variables:
v1 = 5
v2 = 7
v1, v2 = v2, v1
