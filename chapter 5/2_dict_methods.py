marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
print("Output of marks.items():", marks.items())  # Output: dict_items([('Alice', 85), ('Bob', 92), ('Charlie', 78)])
print("Output of marks.keys():", marks.keys())    # Output: dict_keys(['Alice', 'Bob', 'Charlie'])
print("Output of marks.values():", marks.values())  # Output: dict_values([85, 92, 78])
print("Output of marks.get('Alice'):", marks.get("Alice"))  # Output: 85
marks.update({"David": 88})
print("Updated dictionary after adding David:", marks)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 88}
removed_value = marks.pop("Charlie") #pop method removes the specified key and returns the corresponding value
print("Removed value for 'Charlie':", removed_value)  # Output: 78
print("Dictionary after removing 'Charlie':", marks)  # Output: {'Alice': 85, 'Bob': 92, 'David': 88}


# difference between get and accessing directly
print("Accessing 'Eve' directly:", marks.get("Eve"))  # Output: None
print("Accessing 'Eve' directly:", marks["Eve"])  # This would raise a KeyError