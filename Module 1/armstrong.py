# ==========================================
# M1 Activity: Armstrong Number Checker
# ==========================================

# Take input from the user
number = int(input("Enter a number: "))

# Store the original number
original = number

# Initialize variables
sum = 0

# Count the number of digits
digits = len(str(number))

# Calculate the sum of each digit raised to the power of digits
while number > 0:
    digit = number % 10
    sum = sum + digit ** digits
    number = number // 10

# Check if it is an Armstrong number
if sum == original:
    print(original, "is an Armstrong Number.")
else:
    print(original, "is Not an Armstrong Number.")
