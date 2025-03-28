# Ask the user to input their full name in incorrect casing
# Use the '.strip()' and '.lower()' method to remove unecessary spaces and conver the string to lower case
# Use the '.replace()' to replace the spaces inside the string with underscore
full_name = input("Enter your full name: ").strip().lower().replace(" ", "_")
# Print the modified input
print(full_name)