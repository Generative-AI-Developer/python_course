# Valid variable names
name = "Alice"  # Starts with a letter
_value = 10  # Starts with an underscore
age_25 = 30  # Contains letters, numbers, and underscores
user_name = "John"  # Uses underscores for readability

# Case sensitivity
age = 25
Age = 30
print("Case-Sensitive Variables:", age, Age)  # Output: 25 30

# Descriptive naming
total_price = 100.5
print("Descriptive Variable:", total_price)

# Invalid examples (Uncomment to see errors)
# 1st_name = "Bob"  # Cannot start with a number
# class = "Math"  # Cannot use a Python keyword
# user@name = "Alice"  # Cannot use special characters

print("Valid Variables:")
print("Name:", name)
print("Underscore Variable:", _value)
print("Alphanumeric Variable:", age_25)
print("Underscore Naming:", user_name)
print("Descriptive Naming:", total_price)
