# Task: Calculate Factorial Using a Function

def factorial(n):
    """
    Return n! (n factorial) computed with a loop.
    Rules:
      - 0! = 1 by definition
      - n! = 1 * 2 * 3 * ... * n  for n >= 1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    # multiply result by each integer from 2 up to n
    for i in range(2, n + 1):
        result *= i
    return result


# --- main / user interaction ---
# 1) Ask the user for an integer
# 2) Convert the input string to int (this can raise ValueError if not a number)
# 3) Call factorial() and print the answer

try:
    num = int(input("Enter a number: "))
    ans = factorial(num)
    print(f"Factorial of {num} is: {ans}")
except ValueError as e:
    # Catches:
    #  - non-numeric input (e.g., "abc")
    #  - negative numbers (raised inside factorial)
    print(f"Invalid input: {e}")
