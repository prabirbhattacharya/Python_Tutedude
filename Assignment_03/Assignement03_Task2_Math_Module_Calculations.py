# Task 2: Using the Math Module for Calculations

import math
raw = input("Enter a number: ")
try:
    x = float(raw)
except ValueError:
    print()
    raise SystemExit(1)

# Calculation for Square root
if x >= 0:
    sqrt_x = math.sqrt(x)
else:
    sqrt_x = "Undefined for negative numbers"

# Natural logarithm ln(x)
if x > 0:
    ln_x = math.log(x)
else:
    ln_x = "Undefined for zero/negative numbers"

# Sine: math.sin expects radians
sin_x = math.sin(x)

# ---- Output ----
print()
print("Results:")

# Use formatting for numbers where applicable
def fmt(value):
    return f"{value:.12g}" if isinstance(value, (int, float)) else str(value)

print(f"Square root: {fmt(sqrt_x)}")
print(f"Logarithm: {fmt(ln_x)}")
print(f"Sine: {fmt(sin_x)}")

