# Ask the user to input a string
text_input = input("Please enter a string: ")
# Ask the user for the width
width = int(input("Please enter the width of the output: "))
# Check if string needs extra spaces
if len(text_input) < width:
    # If so, calculate the total number of spaces, spaces for the left and right side
    total_spaces = width - len(text_input)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    # Add the spaces to left and right side of the string
    output = " " * left_spaces + text_input + " " * right_spaces
else:
    # If not, just print the string
    output = text_input
    
# Print the formatted string
print(output)