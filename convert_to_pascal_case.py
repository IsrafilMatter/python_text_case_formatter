# Program to convert text to pascal case
# Author: Israfil Palabay
# Date: March 19, 2025

# Ask the user to enter their name with incorrect casing
name = input("Enter your fullname: ")

# Convert to title case and remove spaces
pascal_case = "".join(name.title().split())
print(pascal_case)