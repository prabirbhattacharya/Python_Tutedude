# Task: Sum of Integers from 1 to 50 Using a Loop

# Step 1: Initialize a variable to hold the total sum
total_sum = 0  # Starting from 0

# Step 2: Use a for loop to iterate through numbers 1 to 50
for num in range(1, 51):
    total_sum += num  # Add each number to total_sum

# Step 3: Print the final result
# Use f-string to insert values into the output sentence
print(f"The sum of numbers from 1 to 50 is: {total_sum}")
