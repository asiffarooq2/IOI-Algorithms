
# Calculate factorial using recursion
def calculate_factorial(number):
    if number == 0:
        return 1
    else:
        return number * calculate_factorial(number - 1)


# Example usage
input_number = 5
factorial_result = calculate_factorial(input_number)

print(f"The factorial of {input_number} is: {factorial_result}")
