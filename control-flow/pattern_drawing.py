# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")  # Print stars on the same line
    print()  # Move to the next line after each row
    row += 1  # Increment the row counter
