# ==========================================
# SELECTION SORT PROGRAM
# ==========================================

# Array with different values
numbers = [45, 18, 32, 7, 26, 14, 50]


print("Original Array:")

for number in numbers:
    print(number, end=" ")


# Traverse through the array
for i in range(len(numbers)):

    # Assume current position contains
    # the smallest element
    min_index = i

    # Search for the smallest element
    # in the remaining unsorted array
    for j in range(i + 1, len(numbers)):

        if numbers[min_index] > numbers[j]:
            min_index = j

    # Swap the smallest element with
    # the element at current position
    numbers[i], numbers[min_index] = (
        numbers[min_index],
        numbers[i]
    )


# Display sorted array
print("\n\nSorted Array:")

for number in numbers:
    print(number, end=" ")
