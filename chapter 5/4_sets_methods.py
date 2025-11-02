set_example = {1, 2, 3, 4, 5} # this is a set
print(set_example)  # Output: {1, 2, 3, 4, 5}
# sets are unordered collections of unique elements
# sets methods
# adding an element to a set
set_example.add(6)
print("Set after adding 6:", set_example)  # Output: {1, 2, 3, 4, 5, 6}
# removing an element from a set
set_example.remove(3)
print("Set after removing 3:", set_example)  # Output: {1, 2, 4, 5, 6}
# checking membership in a set
print("Is 4 in the set?", 4 in set_example)  # Output: True
# clearing all elements from a set
set_example.clear() 
print("Set after clearing:", set_example)  # Output: set()  