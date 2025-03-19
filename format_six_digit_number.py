# Program to format number to 6 digits
# Author: Israfil Palabay
# Date: March 19, 2025

# Ask the user to enter a number between 0 and 1000
number = int(input("Enter a number (0-1000): "))

# Print the number formatted with exactly 6 digits, adding leading zeros if necessary
print(f"{number:06d}") 