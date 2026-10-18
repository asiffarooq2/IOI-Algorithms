
# Calculate factorial using Dynamic Programming
def calculate_factorial_dp(number):

    # Create a list to store factorial values
    factorial_values = [0] * (number + 1)

    # Base case: factorial of 0 is 1
    factorial_values[0] = 1

    # Calculate factorial values from 1 to the given number
    for current_number in range(1, number + 1):
        factorial_values[current_number] = (
            current_number * factorial_values[current_number - 1]
        )

    return factorial_values[number]


# Example usage
input_number = 5
factorial_result = calculate_factorial_dp(input_number)

print(f"The factorial of {input_number} is: {factorial_result}")
