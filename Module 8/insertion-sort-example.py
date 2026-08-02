# ==========================================
# INSERTION SORT PROGRAM
# ==========================================

# Array with different values
numbers = [24, 8, 17, 5, 31, 12, 20]

print("Original Array:")
print(numbers)


# Traverse through the array
for i in range(1, len(numbers)):

    # Store current element
    value = numbers[i]

    # Start comparing with the
    # previous element
    j = i - 1

    # Move elements that are greater
    # than value one position ahead
    while j >= 0 and value < numbers[j]:

        numbers[j + 1] = numbers[j]

        j -= 1

    # Place value in its correct position
    numbers[j + 1] = value


# Display sorted array
print("\nSorted Array:")

for number in numbers:
    print(number, end=" ")