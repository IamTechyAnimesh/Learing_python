meaning = {
   "सेब" : "apple",
   "केला" : "banana",
   "संतरा" : "orange",
   "अंगूर" : "grape",
   "पपीता" : "papaya"
}

name = input("word :")
print(f"here is the meaning of {name} : ", meaning.get(name)) #using get method to avoid error if key not found
print("Here is your ans :", meaning[name])  #this will raise an error if key not found
# use get method is better than direct access