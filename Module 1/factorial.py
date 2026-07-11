# ==========================================
# M1 Activity: Factorial of a Number
# ==========================================

# Take input from the user
number = int(input("Enter a number: "))

# Initialize factorial
factorial = 1

# Check if the number is negative
if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    # Calculate factorial
    for i in range(1, number + 1):
        factorial = factorial * i

    # Display the result
    print("The factorial of", number, "is", factorial)
