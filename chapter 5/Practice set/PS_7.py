# If the names of 2 friends are same; what will happen to the program in problem 6?
s = {}

name = input("Input your friend name :")
lang = input("Input Lang name :")
s.update({name: lang})
name = input("Input your friend name :")
lang = input("Input Lang name :")
s.update({name: lang})
name = input("Input your friend name :")
lang = input("Input Lang name :")
s.update({name: lang})
name = input("Input your friend name :")
lang = input("Input Lang name :")
s.update({name: lang})
print(s)
# In this case, if two friends have the same name, the latter entry will overwrite the former one in the dictionary since dictionary keys must be unique.