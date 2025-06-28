def sum(a, b):
    # a and b are local variables
    # They are only accessible within this function
    c = a + b
    # print(z)  # z is a global variable, accessible here
    z = 1 # local variable which is destroyed after function execution
    return c

def greet():
    z = 32 # local variable
    print("Hello")

z = 8 # global variable
print(z)
print(sum(4, 6))
print(z)
