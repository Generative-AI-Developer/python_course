#Dictionaries in Python

# A dictionary in Python is a collection of key-value pairs, where each 
# key is unique and maps to a value.
#  It is defined using curly braces {} or the dict() constructor.


# Using curly braces

student = {
    "name": "Asif",
    "age": 22,
    "grade": "A",
    "subjects": ["Math", "Physics"]
}

print(student["name"])
print(student.items())


for key, value in student.items():
    print(key, ":", value)





# Creating a dictionary
sample_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 1. clear() - Removes all elements
sample_dict.clear()
print("After clear():", sample_dict)  # Output: {}

# Recreating dictionary for further examples
sample_dict = {"name": "Alice", "age": 25, "city": "New York"}

# 2. copy() - Returns a shallow copy of the dictionary
copy_dict = sample_dict.copy()
print("Copy of dictionary:", copy_dict)

# 3. fromkeys() - Creates a dictionary from keys with a default value
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("fromkeys example:", new_dict)

# 4. get() - Returns value of a key, or a default value if key does not exist
print("Get 'name':", sample_dict.get("name"))  # Output: Alice
print("Get 'salary' with default:", sample_dict.get("salary", "Not Found"))

# 5. items() - Returns all key-value pairs as tuples
print("Items:", list(sample_dict.items()))

# 6. keys() - Returns all keys in the dictionary
print("Keys:", list(sample_dict.keys()))

# 7. values() - Returns all values in the dictionary
print("Values:", list(sample_dict.values()))

# 8. pop() - Removes a key and returns its value
removed_value = sample_dict.pop("age")
print("After pop('age'):", sample_dict, "| Removed value:", removed_value)

# 9. popitem() - Removes and returns the last inserted key-value pair
removed_item = sample_dict.popitem()
print("After popitem():", sample_dict, "| Removed item:", removed_item)

# 10. setdefault() - Returns value of a key, or inserts it with a default value
print("Set default for 'country':", sample_dict.setdefault("country", "USA"))
print("Dictionary after setdefault:", sample_dict)

# 11. update() - Updates dictionary with another dictionary or key-value pairs
sample_dict.update({"city": "Los Angeles", "profession": "Engineer"})
print("After update():", sample_dict)
