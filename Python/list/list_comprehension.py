# # List Comprehension Example
# # Creating a multiplication table for the number 5 using list comprehension
# a = 5
# table = []
# # Using a for loop to create a multiplication table

# for i in range(1, 11):
#     table.append(5 * i)

# print(table)

# Using list comprehension to create the multiplication table
table = [5 * i for i in range(1, 11)]
print(table)