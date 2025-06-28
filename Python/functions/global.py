def sum(a, b):
    print("Inside sum function")
    c = a + b
    global z  # Declare z as a global variable
    z = 1  # This modifies the global variable z
    return c

z =  3
print(sum(4, 6))
print(z)
