# Input the users full name
full_name = input("Enter your full name (incorrect casing): ")

# Convert in snake casing
snake_case_name = full_name.lower().replace(" ", "_")

# Print the full name in snake case
print("Output:", snake_case_name)