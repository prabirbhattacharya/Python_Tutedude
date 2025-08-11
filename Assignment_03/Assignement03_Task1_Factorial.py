# Task: Calculate Factorial Using a Function

# Create the function section for factorial calculation
def factorial(n):
    if n < 0:
        raise ValueError()
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Data Input Segment for Factorial Calculation
try:
    num = int(input("Enter a number: "))
    ans = factorial(num)
    print(f"Factorial of {num} is: {ans}")
except ValueError as e:
    print(f"Invalid input: {e}")

