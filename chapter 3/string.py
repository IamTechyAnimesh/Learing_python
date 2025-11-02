# 1. we can use "", '', or ''' ''' to represent strings in Python.
single_quote_str = 'Hello, World!'
double_quote_str = "Hello, World!"  
triple_quote_str = '''Hello World!'''
# 2. HOW TO CHECK THE LENGTH OF A STRING
str = "hello animesh"
print(len(str)) # the str length is 13 but the index will be from 0 to 12
# 3. string_slicing = str[1:5] slicing from index 1 to 4
string_slicing = str[1:5] # it will print from index 1 to index 4 not including index 5
print(string_slicing)
string_slicing2 = str[0:13:2] # it will print from index 0 to index 12 with a step of 2
print(string_slicing2) # it will print hloanmh
string_slicing3 = str[-1:-6:-1] # it will print from index -1 to index -6 with a step of -1
print(string_slicing3) # it will print hsemna
string_slicing4 = str[:5] # it will print from index 0 to index 4
print(string_slicing4) # it will print hello
string_slicing5 = str[5:] # it will print from index 5 to the end of the string
print(string_slicing5) # it will print  animesh
string_slicing6 = str[:] # it will print the whole string
print(string_slicing6) # it will print hello animesh

