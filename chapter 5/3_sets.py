set_example = {1, 2, 3, 4, 5} # this is a set
print(set_example)  # Output: {1, 2, 3, 4, 5}

# how to make an empty set
empty_set = set() # using set() function to create an empty set dont use {} as it creates an empty dictionary
print(empty_set)  # Output: set()

#rules of sets
#1. we cannot have duplicate values in a set
unique_set = {1, 2, 2, 3, 4, 4, 5}
print(f"set cannot have duplicates values: {unique_set}")  # Output: {1, 2, 3, 4, 5} duplicates are removed

# difference between set and list
list_example = [1, 2, 2, 3, 4, 4, 5]
print(f"list can have duplicate values: {list_example}")  # Output: [1, 2, 2, 3, 4, 4, 5] duplicates are retained
#2. sets are unordered collections
unordered_set = {3, 1, 4, 2, 5}
print(f"sets are unordered: {unordered_set}")  # Output: {1, 2, 3, 4, 5} order may vary
