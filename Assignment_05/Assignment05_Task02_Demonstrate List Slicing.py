# Task 2 — Demonstrate List Slicing
# -------------------------------------------------------------

def first_five_and_reverse(seq: list[int]) -> tuple[list[int], list[int]]:
    """Return (first_five, reversed_first_five) from the given sequence."""
    first_five = seq[:5]
    reversed_first_five = first_five[::-1]
    return first_five, reversed_first_five

def main() -> None:
    # Make the list 1..10
    numbers = list(range(1, 11))
    
    # Make the slice and reverse
    first_five, reversed_first_five = first_five_and_reverse(numbers)
    
    # Results of List and Slice
    print("Original list:", numbers)
    print("Extracted first five elements:", first_five)
    print("Reversed extracted elements:", reversed_first_five)

if __name__ == "__main__":
    main()
