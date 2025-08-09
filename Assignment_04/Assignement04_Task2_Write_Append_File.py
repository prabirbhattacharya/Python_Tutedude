"""
Task 2: Write and Append Data to a File

What this script does:
1) Asks the user for some text and WRITES it to "output.txt" (overwrites old content).
2) Asks for more text and APPENDS it to the same file (keeps existing content).
3) Reads the whole file and prints the final content.

Notes:
- Uses UTF-8 encoding for portability.
- Each user input is saved on a new line for readability.
"""

from pathlib import Path

FILENAME = "output.txt"  # file will be created in the same folder as this script


def write_text(path: str, text: str) -> None:
    """Create/overwrite the file and write the given text."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.rstrip("\n") + "\n")  # ensure single trailing newline


def append_text(path: str, text: str) -> None:
    """Append the given text to the file, creating it if missing."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(text.rstrip("\n") + "\n")  # ensure single trailing newline


def read_all(path: str) -> str:
    """Return the entire file content as a string."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    # 1) Get text to write (overwrite any existing file)
    first = input("Enter text to write to the file: ")
    write_text(FILENAME, first)
    print(f"Data successfully written to {FILENAME}.\n")

    # 2) Get text to append
    second = input("Enter additional text to append: ")
    append_text(FILENAME, second)
    print("Data successfully appended.\n")

    # 3) Read the file back and display
    print(f"Final content of {FILENAME}:")
    print(read_all(FILENAME))


if __name__ == "__main__":
    try:
        main()
    except PermissionError:
        print(f"Error: Permission denied when trying to access '{FILENAME}'.")
    except OSError as e:
        # Handles a wide range of file-related issues
        print(f"File error: {e}")
