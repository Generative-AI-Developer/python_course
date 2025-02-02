# Arithmetic Operators
a, b = 10, 5
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("-" * 40)

# Comparison Operators
x, y = 10, 20
print("Comparison Operators:")
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater:", x > y)
print("Less:", x < y)
print("Greater or Equal:", x >= y)
print("Less or Equal:", x <= y)
print("-" * 40)

# Logical Operators
p, q = True, False
print("Logical Operators:")
print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)
print("-" * 40)

# Bitwise Operators
m, n = 5, 3  # 5 -> 0101, 3 -> 0011
print("Bitwise Operators:")
print("AND:", m & n)
print("OR:", m | n)
print("XOR:", m ^ n)
print("NOT (~m):", ~m)
print("Left Shift:", m << 1)
print("Right Shift:", m >> 1)
print("-" * 40)

# Assignment Operators
x = 10
print("Assignment Operators:")
x += 5
print("x += 5:", x)
x -= 2
print("x -= 2:", x)
x *= 3
print("x *= 3:", x)
x /= 2
print("x /= 2:", x)
x %= 4
print("x %= 4:", x)
x **= 2
print("x **= 2:", x)
print("-" * 40)

# Identity Operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("Identity Operators:")
print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)
print("-" * 40)

# Membership Operators
numbers = [1, 2, 3, 4, 5]
print("Membership Operators:")
print("3 in numbers:", 3 in numbers)
print("10 not in numbers:", 10 not in numbers)
print("-" * 40)
