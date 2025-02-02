# The `type()` function in Python is used to return the type of an object.
# Syntax: type(object)
# It returns the class of the object passed as an argument.

# Example:
x = 5
print(type(x))  # Output: <class 'int'>


s = "Hello"
print(type(s))  # Output: <class 'str'>

lst = [1, 2, 3]
print(type(lst))  # Output: <class 'list'>

# You can also use `type()` to define a new class dynamically
MyClass = type('MyClass', (object,), {})
obj = MyClass()
print(type(obj))  # Output: <class '__main__.MyClass'>

# Note: `isinstance()` is often preferred over `type()` for type checking, especially with inheritance.
