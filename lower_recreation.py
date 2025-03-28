# Ask the user for input a string
user_input = input("Please enter a string: ")
# Create a translation table for uppercase to lowercase
upper_to_lower = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
# Convert the input to lowercase using translate
lowercase_input = user_input.translate(upper_to_lower)
# Print the input
print(lowercase_input)