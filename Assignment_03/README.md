# Python Tasks - Module 3

This repository contains two Python scripts that demonstrate basic programming skills with **functions** and the **math module**.

---

## 📘 Task 1: Calculate Factorial Using a Function

**Description:**  
This script defines a `factorial` function that takes an integer as input and returns its factorial using a loop.

**Features:**
- Validates input to ensure it's a non-negative integer.
- Uses a loop to calculate factorial.
- Handles invalid or negative inputs gracefully.

**How it works:**
1. Ask the user for a number.
2. Validate the input.
3. Call the `factorial()` function.
4. Print the result.

**Sample Output:**
```
Enter a number: 5
Factorial of 5 is: 120
```

**File:** `Assignement03_Task1_Factorial.py`

---

## 📘 Task 2: Using the Math Module for Calculations

**Description:**  
This script asks the user for a number and calculates:
- Square root of the number
- Natural logarithm (log base e)
- Sine of the number (in radians)

**Features:**
- Uses the built-in `math` module.
- Handles invalid input types and domain errors (e.g., sqrt of a negative number).
- Displays results clearly.

**How it works:**
1. Ask the user for a number (integer or decimal).
2. Compute the square root if number >= 0.
3. Compute the natural log if number > 0.
4. Compute sine (in radians).
5. Display results.

**Sample Output:**
```
Enter a number: 25

Results:
Square root: 5
Logarithm: 3.21887582487  # natural log (base e)
Sine (radians): -0.132351750098
```

**File:** `Assignement03_Task2_Math_Module_Calculations.py`

---

Both scripts are simple, beginner-friendly, and include comments explaining each step.
