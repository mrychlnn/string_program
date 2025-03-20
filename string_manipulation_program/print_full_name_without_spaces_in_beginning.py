# Input the users full name
full_name = input("Enter your full name (with several spaces at the beginning): ")

# Remove leading spaces
remove_spaces = full_name.lstrip()

# Print the output w/o spaces in the beginning
print("Output:", remove_spaces)