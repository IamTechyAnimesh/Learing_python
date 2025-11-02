friends = ["Alice", "Bob", "Charlie",1,1.30,True]
print(friends[0])
friends[0] = "David" # strings are immutable, but lists are mutable
print(friends[0])
# you can add, remove, or change items in a list

# slicing list
print(friends[1:4])  # prints from index 1 to index 3
print(friends[-1])  # prints the last item in the list
print(friends[::2])  # prints every second item in the list
