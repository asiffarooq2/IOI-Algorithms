# ==========================================
# OPTIMIZED BUBBLE SORT
# ==========================================

# Function to sort an array
# using optimized Bubble Sort
def BubbleSort(numbers):

    n = len(numbers)

    # Traverse through the array
    for i in range(n):

        swapped = False

        # Last i elements are already sorted
        for j in range(0, n - i - 1):

            # Compare adjacent elements
            if numbers[j] > numbers[j + 1]:

                # Swap the elements
                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

                swapped = True

        # If no swapping happened,
        # array is already sorted
        if swapped == False:
            break


# Driver Code
numbers = [48, 15, 72, 9, 36, 21, 60, 12]


print("Original Array:")

for number in numbers:
    print(number, end=" ")


# Sort the array
BubbleSort(numbers)


print("\n\nSorted Array:")

for number in numbers:
    print(number, end=" ")
