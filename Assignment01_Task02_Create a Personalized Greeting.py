# Task: Create a Personalized Greeting

# Step 1: Ask the user for their first name
# The input() function collects text input from the user
first_name = input("Enter your first name: ")

# Step 2: Ask the user for their last name
last_name = input("Enter your last name: ")

# Step 3: Combine first and last name into one full name
# We use string concatenation and a space between names
full_name = first_name + " " + last_name

# Step 4: Display a greeting message using the full name
# The f-string (formatted string) makes it easy to insert variables in text
print(f"\nHello, {full_name}! Welcome to the Python program.")
