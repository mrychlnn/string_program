# Input numbers from 0-1000
num = int(input("Enter a number (0-1000): "))

# Format the number as 6 digits string with leading zeros
six_digits = f"{num:06d}"

# Print the inputted numbers with leading zeros to fulfill the 6 digits format
print("Output:", six_digits)
