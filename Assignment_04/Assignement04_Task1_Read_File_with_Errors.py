"""
Task 1: Read a File and Handle Errors
"""

from pathlib import Path

FILENAME = "sample.txt"  # expected in the same folder as this script

def read_file_line_by_line(path: str) -> None:
    """
    Read the file at `path` and print its content line by line.
    """
    print("Reading file content:")
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            clean_line = line.rstrip("\n")  # remove newline first
            print(f"Line {i}: {clean_line}")

def main():
    try:
        here = Path.cwd()
        read_file_line_by_line(FILENAME)
    except FileNotFoundError:
        print(f"Error: The file '{FILENAME}' was not found.")
        print("Tip: Put 'sample.txt' in the same folder and run again.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{FILENAME}'.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode '{FILENAME}'. Is it plain UTF-8 text?")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
