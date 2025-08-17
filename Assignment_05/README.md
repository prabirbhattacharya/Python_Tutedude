# Python Assignment 05 — Student Marks & List Slicing

## What's inside
- `Assignment05_Task01_Dictionary of Student Marks.py` — look up a student's marks from a small dictionary.
- `Assignment05_Task02_Demonstrate List Slicing.py` — show how list slicing works by grabbing and reversing the first five numbers.

## Task 1 — Dictionary of Student Marks

**Goal:** Ask for a student's name and print their marks if we have them. Otherwise, say they're not found.

### Section of Data Input of the Students
Open `Assignment05_Task01_Dictionary of Student Marks.py` and edit the `marks` dictionary:
```python
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
```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
```
