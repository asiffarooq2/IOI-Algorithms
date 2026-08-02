# ==========================================
# SHELL SORT PROGRAM
# ==========================================

# Array with different values
numbers = [23, 12, 1, 8, 34, 54, 2, 15]

print("Original Array:")
print(numbers)


# Initialize array size
n = len(numbers)


# Start with half of the array size
interval = n // 2


# Rearrange elements at
# n/2, n/4, n/8 ... intervals
while interval > 0:

    for i in range(interval, n):

        # Store current element
        temp = numbers[i]

        j = i

        # Shift larger elements
        # toward the right
        while (
            j >= interval
            and numbers[j - interval] > temp
        ):

            numbers[j] = numbers[j - interval]

            j -= interval

        # Place element in correct position
        numbers[j] = temp

    # Reduce the interval
    interval //= 2


# Display sorted array
print("\nSorted Array:")
print(numbers)
