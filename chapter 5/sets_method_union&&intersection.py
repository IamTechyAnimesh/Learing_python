s1 = {1, 2, 3}
s2 = {3, 4, 5}
# Union of two sets
union_set = s1.union(s2) #it will combine both sets and remove duplicates
print(f"Union of s1 and s2: {union_set}")  # Output: {1, 2, 3, 4, 5}
# Intersection of two sets
intersection_set = s1.intersection(s2) #it will return only same elements in both sets 
print(f"Intersection of s1 and s2: {intersection_set}")  # Output: {3}