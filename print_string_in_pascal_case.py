# Ask the user to input their full name in incorrect casing
# Use the '.title()' to correct the casing
# Use the '.replace()' to replace the spaces with empty string
full_name = input("Please enter your full name: ").title().replace(" ", "")
# Print the modified input
print(full_name)