# Ask the user to input a number from 0-1000
number = int(input("Enter a number between 0 and 1000: "))
# Check if the number is valid
if 0 <= number <= 1000:
# If valid, use the '.zfill()' method to make the input into a 6 digit number then print the modified input
    print("Valid Input")