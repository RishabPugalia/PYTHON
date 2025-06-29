s = {1, 2, 3, 4, 5}
print(s)

s.add(6) 
s.add(7)  # Add an element to the set
print(s)

s.remove(2)  # Remove an element from the set
print(s)

s.discard(32)  # Remove an element without raising an error if it doesn't exist
print(s)

s.pop()  # Remove and return an arbitrary element from the set
print(s)

