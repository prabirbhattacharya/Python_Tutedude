# Task 1 — Dictionary of Student Marks
# -------------------------------------------------------------
# Example for This Task:
#   Enter the student's name: Alice
#   Alice's marks: 85
#
#   Enter the student's name: John
#   Student not found.
# -------------------------------------------------------------

def lookup_marks(student_name: str, data: dict) -> tuple[bool, str]:
    if not isinstance(student_name, str):
        return False, "Student not found."
    
    # Build a quick case-insensitive index: 'alice' -> ('Alice', 85)
    index = {k.casefold(): (k, v) for k, v in data.items()}
    
    key = student_name.strip().casefold()
    if key in index:
        proper_name, score = index[key]
        return True, f"{proper_name}'s marks: {score}"
    else:
        return False, "Student not found."


def main() -> None:
    # Sample dataset for Student name wise Marks
    marks = {
        'Alice': 85,
        'Bob': 78,
        'Charlie': 92,
        'Diana': 88,
    }
    
    # Format for Input a student name
    name = input("Enter the student's name: ")
    
    # 3) Find and display the result
    found, message = lookup_marks(name, marks)
    print(message)


if __name__ == "__main__":
    main()
