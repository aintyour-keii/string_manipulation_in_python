# Ask the user to input a string
text_input = input("Enter a string: ")

# Initialize a boolean to track if the string is in all caps
all_caps = True

# Itterate through the string
for char in text_input:
    # And check if the character is in range of "a-z" then set the boolean to false and break
    if 'a' <= char <= 'z':
        all_caps = False
        break

# Print the value of the boolean
print(all_caps)