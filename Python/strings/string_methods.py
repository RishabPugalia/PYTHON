s = "hello world"

a = len(s)
# print(a)

# print(s.upper())  # Convert to uppercase

# print(s.lower())  # Convert to lowercase
# print(s.capitalize())  # Capitalize the first letter
# print(s.title())  # Capitalize the first letter of each word

# text = "  Hello World  "
# print(text.strip())  # Remove leading and trailing whitespace
# print(text.lstrip())  # Remove leading whitespace
# print(text.rstrip())  # Remove trailing whitespace

# text ="Python is fun & fun"
# print(text.find("is"))  # Find the index of the first occurrence of "is"
# print(text.replace("fun", "awesome"))  # Replace "fun" with "awesome"


# text = "Apples,oranges,bananas"
# print(text.split(","))  # Split the string into a list at each comma
# print(",".join(["Apples", "oranges", "bananas"]))  # Join the list into a string with commas

text = "Python123"
print(text.isalpha())  # Check if all characters are alphabetic
print(text.isalnum())  # Check if all characters are alphanumeric
print(text.isdigit())  # Check if all characters are digits
print(text.isspace())  # Check if all characters are whitespace