# Ask the user to input a statement
statement = input("Please enter a statement: ")
# Split the statement into words using '.split()'
words = statement.split()
# Get the length of the returned list of the split method and print it
print(len(words))