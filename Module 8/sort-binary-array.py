# ==========================================
# SORT 0s AND 1s IN AN ARRAY
# ==========================================


# Function to sort 0s and 1s
def sortZeroOne(numbers, size):

    # Count the number of zeros
    zero_count = 0

    for i in range(0, size):

        if numbers[i] == 0:
            zero_count += 1

    # Fill the beginning of the
    # array with zeros
    for i in range(0, zero_count):

        numbers[i] = 0

    # Fill the remaining positions
    # with ones
    for i in range(zero_count, size):

        numbers[i] = 1


# Driver Code
numbers = [1, 0, 1, 1, 0, 1, 0, 0, 1]

size = len(numbers)


print("Original Array:", numbers)


# Function call
sortZeroOne(
    numbers,
    size
)


# Display sorted array
print("Sorted Array:", end=" ")

for i in range(0, size):

    print(numbers[i], end=" ")
