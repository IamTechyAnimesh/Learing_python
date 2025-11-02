# tuple is an immutable ordered collection of items
# blank tuple
empty_tuple = ()
# tuple with single element
single_element_tuple = (42,)
print("the typer of single_element_tuple is:", type(single_element_tuple))
# tuple with multiple elements
multiple_element_tuple = (1, 4, 6, 12, 15)

# method of tuple
a = (1, 2, 3, 4, 2, 5, 2)
print("the count of 2 in tuple is:", a.count(2))  # counts the number of occurrences of 2 in the tuple
print("the index of 5 in tuple is:", a.index(5))  # returns the index of the first occurrence of 5 in the tuple
# slicing tuple
print("slicing from index 1 to 4:", a[1:5])  # prints from index 1 to index 4

