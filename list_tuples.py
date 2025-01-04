# # List - Array - Ordered collection of values - mutable - indexed

# # numbers = [] # declaring a list : creates a new empty list in memory

# numbers = [2, 10, 50, 90, 60, 71, 40, 90]
# # print(numbers[3])

# # numbers[2] = 15 # Destroys initial value
# # print(numbers)

# # numbers[5] = 60 # error as index out of range
# # numbers.append(60) # instead provide a list method to append the value 60 last
# numbers.insert(2, 70) # inserts value between indexes
# print(numbers)

# # print(numbers[-1]) # Accessing last element in the index - negative indexing

# # numbers.insert(3, 100)
# popped_value = numbers.pop(3)
# print(numbers)
# #print(popped_value) # Remove and return item at default last

# numbers.remove(2)
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# print(numbers.count(90)) # how many times 90 exists

# Tuple - Ordered collection of values just like a list, zero indexed, its a list but only diff is its immutable
names = ("Wangari", "Maina", "Wanjiru") # use regular parenthesis to make a tuple
print(names)
print(type(names))

print(names[1]) # Square brackets to access the elements
# names[2] = 'Somebody' # Error bc tuple is immutable

print(names.index("Wangari"))
print(len(names))
