# Check that a tuple type cannot be changed in python.
my_tuple = (1, 2, 3, 4, 5)
my_tuple[4] = 10  # trying to change the value at index 4
print(my_tuple)