# Ask the user to input a string
text_input = input("Enter a string: ")
# Ask the user for the width
width = int(input("Enter your desired width: "))
# Check if string needs extra spaces
if len(text_input) < width:
    # If so, add spaces to the string, 
    # the number of spaces is equal to that of the width minus the length of the string
    num_of_spaces = width - len(text_input)
    text_input += ' ' * num_of_spaces

# Print the result
print(text_input)