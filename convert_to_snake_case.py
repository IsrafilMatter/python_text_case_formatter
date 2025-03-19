# Program to convert text to snake case
# Author: Israfil Palabay
# Date: March 19, 2025

# Ask the user to enter their name with incorrect casing
name = input("Enter your fullname in incorrect casing: ")

# Convert to lowercase and replace spaces with underscores
snake_case = "_".join(name.lower().split())
print(snake_case) # Print the snake_case formatted name.