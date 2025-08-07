# Task: Perform Basic Mathematical Operations

# Step 1: Take two numbers as input from the user
# We use input() to get user input and float() to allow decimal values
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform basic mathematical operations

# Addition
addition = num1 + num2

# Subtraction
subtraction = num1 - num2

# Multiplication
multiplication = num1 * num2

# Division
# We check if the second number is not zero to avoid division by zero error
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (Cannot divide by zero)"

# Step 3: Display the results of each operation
# We use print() statements to show each result clearly

print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
