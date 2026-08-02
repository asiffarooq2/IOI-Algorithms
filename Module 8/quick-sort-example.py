# ==========================================
# QUICK SORT PROGRAM
# ==========================================


# Function to find the partition position
def partition(numbers, low, high):

    # Choose the rightmost element as pivot
    pivot = numbers[high]

    # Pointer for the smaller element
    i = low - 1

    # Compare each element with the pivot
    for j in range(low, high):

        # If current element is smaller
        # than or equal to pivot
        if numbers[j] <= pivot:

            i = i + 1

            # Swap elements
            numbers[i], numbers[j] = (
                numbers[j],
                numbers[i]
            )

    # Put pivot in its correct position
    numbers[i + 1], numbers[high] = (
        numbers[high],
        numbers[i + 1]
    )

    # Return pivot position
    return i + 1


# Function to perform Quick Sort
def quickSort(numbers, low, high):

    if low < high:

        # Find the pivot position
        pivot_index = partition(
            numbers,
            low,
            high
        )

        # Sort elements before pivot
        quickSort(
            numbers,
            low,
            pivot_index - 1
        )

        # Sort elements after pivot
        quickSort(
            numbers,
            pivot_index + 1,
            high
        )


# Array with different values
numbers = [42, 15, 8, 23, 4, 16, 30, 9]


print("Unsorted Array:")
print(numbers)


# Last index of array
last_index = len(numbers) - 1


# Perform Quick Sort
quickSort(
    numbers,
    0,
    last_index
)


print("\nSorted Array:")
print(numbers)
