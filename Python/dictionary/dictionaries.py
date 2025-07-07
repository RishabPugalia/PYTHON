marks = { "Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92, "Eve": 88 }
# print(marks, type(marks))

print(marks["Alice"])  # Access value by key
marks["Bob"] = 95  # Update value for key "Bob"
print(marks)

marks["Frank"] = 80  # Add a new key-value pair
print(marks)