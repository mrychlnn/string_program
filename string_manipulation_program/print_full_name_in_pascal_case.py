# Input the users full name
full_name = input("Enter your full name (incorrect casing): ")

# Convert name in Pascal case
pascal_case_name = full_name.title().replace(" ", "")

# Print the full name in pascal casing
print("Output:", pascal_case_name)