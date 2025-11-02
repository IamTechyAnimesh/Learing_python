# If languages of two friends are same; what will happen to the program in problem 6?

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
# In this case, if two friends have the same language, both entries will be stored in the dictionary since the keys (friend names) are different.