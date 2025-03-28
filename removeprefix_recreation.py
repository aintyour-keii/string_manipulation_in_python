# Ask for the user input
user_input = input("Enter a string: ")
# Ask for the prefix to be removed
prefix = input("Enter the prefix to be removed: ")
# Check if the string starts with the prefix
if user_input.startswith(prefix):
    # If it does, remove the prefix and print the result
    print(user_input[len(prefix):])
else:
    # If it doesn't, print the string unmodified
    print(user_input)