# Subscripting
print("Hello"[4])  

# String Concatenation
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large integers
print(123_456_678)

# Float = Decimal number
print(3.14159)

# Boolean = True or False
print(True)
print(False)

# Check data type
print(type("123"))
print(type(1))
print(type(3.12))
print(type(True))

#Type conversion, You can convert data into different data types using special functions. e.g
print(int("1234") + int("12"))
int()
float()
str()
bool()

# Mathematical operations
print(3 + 5)    # Addition
print(7 - 4)    # Subtraction    
print(3 * 2)    # Multiplication
print(6 / 3)    # Division (you will always get a float)
print(3 // 2)   # Floor division (you will always get an integer, careful because it removes decimals)
print(2 ** 2)   # Exponent (two times two)

# PEMDASLR
# Parentheses () use it to isolate calculations
# Exponents **
# Multiplication * and Division /
# Addition + and Subtraction -
# Left to right

# BMI Calculator
height = 1.70 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / height** 2

print(bmi)

# Flooring a number to the lowest whole number
print(int(bmi))

# Flooring a number but usind round() function, this checks if its closer to the whole number up and down.
print(round(bmi))

# Round to a specific number of decimal places
print(round(bmi, 2))

# Manipulate a previos value 
score = 0
score += 1

# F-String
score = 0
height = 1.70
isWinning = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")