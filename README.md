# Assignment 04 - File Handling in Python

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
```
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
```

**File:** `Assignement04_Task2_Write_Append_File.py`

---

Both scripts are beginner-friendly and include comments explaining each part of the process.
