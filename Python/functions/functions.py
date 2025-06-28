# a = 4
# b = 2
# c = 1

# average = (a + b + c) / 3
# print(average)

# a1 = 5
# b1 = 3
# c1 = 2

# average1 = (a1 + b1 + c1) / 3
# print(average1)

def average(a, b, c):
    d = (a + b + c) / 3
    # print(d) # without variable assignment, this would print the average directly
    return d  # returning the average value

o1 = average(4, 2, 1) # calling the function with 4, 2, 1
o2 = average(5, 3, 2) # calling the function with 5, 3, 2
print(o1)  # printing the first average
print(o2)  # printing the second average
