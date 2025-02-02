# The `input()` function in Python is used to take input from the user.
# It returns the input as a string by default. You can convert it to another type if needed.

# Syntax:
# input(prompt)  # 'prompt' is optional, it's displayed to the user before input.

# Example 1: Basic input
user_input = input("Enter your name: ")
print(f"Hello, {user_input}!")

# Example 2: Converting input to an integer
age = input("Enter your age: ")
age = int(age)  # Convert to integer
print(f"Your age is {age} years old.")

# Example 3: Handling float input
height = input("Enter your height in meters: ")
height = float(height)  # Convert to float
print(f"Your height is {height} meters.")

# Example 4: Multi-line input loop (exit by entering 'done')
print("Enter multiple lines of text (enter 'done' to stop):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("You entered:")
print("\n".join(lines))
