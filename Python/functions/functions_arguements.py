# positional arguments in functions

# def add(a, b):
#     return a + b

# c = add(2, 3)  # calling the function with 2 and 3
# print(c)  

# default arguments in functions

# def add(a, b, d=0):
#     return a + b + d

# c = add(2, 3)  # calling the function with 2 and 3
# print(c)  # printing the result of the addition

# c = add(2, 3, 4) #it will override the default value of d

# keyword arguments in functions

def add(a, b, d=0):
    return a + b + d

c = add(3, 5, 2)
print(c)

c1 = add(b=5, a=3)