friends = ["Alice", "Bob", "Charlie"]
print(friends)
friends.append("David")  # adds "David" to the end of the list
print(friends)

l1 = [1, 2, 3, 4]
l1.append([5, 6])  # adds the list [5, 6] as a single item to the end of l1
l2 = [1, 2, 3, 4]
l2.sort()
l3 = [4, 3, 2, 1]
l3.reverse()  # reverses the order of items in l3
print("after append:", l1)
print("after sort:", l2)
print("after reverse:", l3)
l4 = [3, 1, 4, 2]
l4.insert(2, 5)  # inserts 5 at index 2 in l4
print("after insert:", l4)
l4.pop(2)  # removes and returns the item at index 2 from l4
print("after pop:", l4)
print(l4.pop(3))  # returns the index of the first occurrence of 4 in l4
l5 = [1, 2, 3, 4, 2]
l5.remove(2)  # removes the first occurrence of 2 from l5
print("after remove:", l5)