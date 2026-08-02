# ==========================================
# MERGE SORT PROGRAM
# ==========================================


# Function to perform Merge Sort
def mergeSorting(numbers):

    # Continue splitting until
    # only one element remains
    if len(numbers) > 1:

        # Find middle position
        mid = len(numbers) // 2

        # Divide array into two halves
        left = numbers[:mid]
        right = numbers[mid:]

        # Recursive calls
        mergeSorting(left)
        mergeSorting(right)

        # Pointers for left and right arrays
        i = 0
        j = 0

        # Pointer for main array
        k = 0

        # Compare elements from both halves
        while i < len(left) and j < len(right):

            if left[i] <= right[j]:

                numbers[k] = left[i]
                i += 1

            else:

                numbers[k] = right[j]
                j += 1

            k += 1

        # Copy remaining elements
        # from the left half
        while i < len(left):

            numbers[k] = left[i]

            i += 1
            k += 1

        # Copy remaining elements
        # from the right half
        while j < len(right):

            numbers[k] = right[j]

            j += 1
            k += 1


# Array with different values
numbers = [
    72, 18, 45, 9, 63,
    27, 81, 36, 12
]


print(
    "Unsorted Array:",
    numbers
)


# Perform Merge Sort
mergeSorting(numbers)


print(
    "Sorted Array:",
    numbers
)
