# # String formatting in Python
# template = "Dear {}, Take this {}$ bag"
# a = "John"
# a1 = 100
# b = "Alice"
# b1 = 200

# s1 = (template.format(a, a1))  # Dear John, Take this 100$ bag
# s2 = (template.format(b, b1))  # Dear Alice, Take this 200$ bag
# print(s1)
# print(s2)

# # F-strings
# print(f"Hey {a}, Take this {a1}$ bag")  # Dear John, Take this 100$ bag
# print(f"Hey {b}, Take this {b1}$ bag")  # Dear Alice, Take this 200$ bag

# x = 10
# y = 5
# print(f"The sum of {x} and {y} is {x + y}")

# pi = 3.14159265
# print(f"Pi rounded to 2 decimal places: {pi:.2f}")

 
text = "Python"
print(f"{text:>10}") # Right align
print(f"{text:<10}") # Left align
print(f"{text:^10}") # Center align
