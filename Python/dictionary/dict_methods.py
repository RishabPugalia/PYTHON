marks = { "Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92, "Eve": 88 }

print(marks.keys())  # Get all keys
print(marks.values())  # Get all values
print(marks.items())  # Get all key-value pairs
# marks.clear()  # Clear the dictionary
marks.pop("Charlie")  # Remove a key-value pair by key
print(marks)
marks.popitem()  # Remove the last inserted key-value pair
print(marks)