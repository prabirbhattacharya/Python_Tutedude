# Python_Tutedude
Learning Python in TuteDude

# Assignment 01 :  Basic Python Concepts

This repository contains two beginner Python scripts:

## Asignment 01_Task 1: Perform Basic Mathematical Operations
- Takes two numbers as input.
- Performs addition, subtraction, multiplication, and division.
- Displays results with error handling for division.

## Assignment 01_Task 2: Create a Personalized Greeting
- Asks for user’s first and last name.
- Combines them and prints a greeting message.

---
Created as part of a programming exercise.



# Assignment 02 : Control Structures in Python

This repository contains beginner-level Python tasks focused on basic programming concepts including mathematical operations, conditionals, and loops.

---

## 📘 Task 1: Check if a Number is Even or Odd

**Description:**  
This script takes an integer input from the user and checks whether the number is even or odd using an `if-else` statement.

**How it works:**
- Takes user input using `input()`
- Converts it to an integer using `int()`
- Uses the modulo operator `%` to check for evenness
- Displays the result using a formatted message

**Sample Output:**
```
Enter a number: 7
7 is an odd number.
```

---

## 📘 Task 2: Sum of Integers from 1 to 50 Using a Loop

**Description:**  
This script calculates the sum of all integers from 1 to 50 using a `for` loop.

**How it works:**
- Initializes a variable `total_sum = 0`
- Iterates from 1 to 50 using `range()`
- Adds each number to `total_sum` inside the loop
- Prints the final result using an `f-string`

**Sample Output:**
```
The sum of numbers from 1 to 50 is: 1275
```

---


# Assignment 03 : Functions & Modules in Python 

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



# Assignment 04 : Files, Exceptions, and Errors in Python

This repository contains two Python scripts that demonstrate **file handling** in Python, including reading, writing, appending, and handling errors.

---

## 📘 Task 1: Read a File and Handle Errors

**Description:**  
This script attempts to open and read a file named `sample.txt`, printing its content line by line. It also handles common file-related errors gracefully.

**Features:**
- Reads file line by line with line numbers.
- Handles:
  - Missing file (`FileNotFoundError`)
  - Permission issues (`PermissionError`)
  - Decoding problems (`UnicodeDecodeError`)
- Friendly error messages instead of crashes.

**How it works:**
1. Tries to open `sample.txt` in the same directory.
2. Reads and prints each line with its line number.
3. Displays helpful error messages if issues occur.

**Sample Output (File exists):**
```
Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.
```

**Sample Output (File missing):**
```
Error: The file 'sample.txt' was not found.
Tip: Put 'sample.txt' in the same folder and run again.
```

**File:** `Assignement04_Task1_Read_File_with_Errors`

---

## 📘 Task 2: Write and Append Data to a File

**Description:**  
This script demonstrates how to write new content to a file (`output.txt`), append additional content, and read the final file content.

**Features:**
- Overwrites existing content when writing.
- Appends text without removing previous data.
- Reads and displays final file content.

**How it works:**
1. Takes user input and writes it to `output.txt` (overwriting any previous content).
2. Takes another input and appends it to the same file.
3. Reads and displays the full content.

**Sample Output:**

Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.


# Python Assignment 05 — Student Marks & List Slicing

## What's inside
- `Assignment05_Task01_Dictionary of Student Marks.py` — look up a student's marks from a small dictionary.
- `Assignment05_Task02_Demonstrate List Slicing.py` — show how list slicing works by grabbing and reversing the first five numbers.

## Task 1 — Dictionary of Student Marks

**Goal:** Ask for a student's name and print their marks if we have them. Otherwise, say they're not found.

### Section of Data Input of the Students
Open `Assignment05_Task01_Dictionary of Student Marks.py` and edit the `marks` dictionary:
python
marks = {
    'Alice': 85,
    'Bob': 78,
    'Charlie': 92,
    'Diana': 88,
}


## Task 2 — Demonstrate List Slicing

**Task:** Build a list from 1 to 10, take the first five elements, reverse them, and print everything.

### Script for Listing and Slicing
- Slices look like `seq[start:stop:step]`.
- `start` defaults to the beginning.
- `stop` is **exclusive** (so `[:5]` returns indices `0..4`).
- Reversing is as simple as `seq[::-1]`.

### Expected output
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]


**File:** `Assignment05_Task02_Demonstrate List Slicing.py`

