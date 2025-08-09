"""
Task 2: Using the Math Module for Calculations

- Ask the user for a number
- Compute:
    * Square root (real numbers only)
    * Natural logarithm, ln(x) (x must be > 0)
    * Sine of the number (input is treated as radians)
- Display results with clear messages
"""

import math  # standard math library: sqrt, log, sin, etc.

# ---- Input ----
# Use float() so the user can enter integers or decimals
raw = input("Enter a number: ")
try:
    x = float(raw)
except ValueError:
    print("Invalid input: please enter a numeric value (e.g., 12 or 3.14).")
    raise SystemExit(1)

# ---- Calculations ----
# Square root: only defined for x >= 0 in the real number system
if x >= 0:
    sqrt_x = math.sqrt(x)
else:
    sqrt_x = "Undefined for negative numbers (real domain only)"

# Natural logarithm ln(x): only defined for x > 0
if x > 0:
    ln_x = math.log(x)  # math.log is natural logarithm (base e)
else:
    ln_x = "Undefined for zero/negative numbers"

# Sine: math.sin expects radians
sin_x = math.sin(x)

# ---- Output ----
print()  # blank line for readability
print("Results:")

# Use formatting for numbers where applicable
def fmt(value):
    return f"{value:.12g}" if isinstance(value, (int, float)) else str(value)

print(f"Square root: {fmt(sqrt_x)}")
print(f"Logarithm: {fmt(ln_x)}  # natural log (base e)")
print(f"Sine (radians): {fmt(sin_x)}")

# Tip: If you have degrees and want sine, convert first:
# radians = math.radians(degrees); math.sin(radians)
