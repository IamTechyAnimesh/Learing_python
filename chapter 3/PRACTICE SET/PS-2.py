
# Write a program to fill in a letter template given below with name and date.

name = input("Enter your name: ")
date = input("Enter the date (e.g., 25th December 2024): ")

# This is not the right way to do it
letter = f"Dear {name},\n You are selected!\n {date}"
print(letter)

# This is the right way to do it using replace() function
letter = ''' Dear <|Name|>, 
You are selected!
<|Date|> '''
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))  # i used method chaining here