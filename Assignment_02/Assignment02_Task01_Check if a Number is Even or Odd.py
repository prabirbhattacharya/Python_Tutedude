# Task: Check if a Number is Even or Odd

# Step 1: Take integer input from the user
# Using int() to ensure we get a whole number (not decimal)
num = int(input("Enter a number: "))

# Step 2: Use an if-else statement to check even or odd
# The modulo operator (%) gives the remainder after division
# If remainder when divided by 2 is 0, then it's even
if num % 2 == 0:
    # Step 3a: If the number is even, print this message
    print(f"{num} is an even number.")
else:
    # Step 3b: If the number is not even (i.e., odd), print this
    print(f"{num} is an odd number.")
