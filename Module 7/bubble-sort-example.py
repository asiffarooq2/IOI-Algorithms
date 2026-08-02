# ==========================================
# BUBBLE SORT PROGRAM
# ==========================================

# Function to sort an array using Bubble Sort
def BubbleSort(numbers):

    n = len(numbers)

    # Traverse through the array
    for i in range(n):

        # Last i elements are already sorted
        for j in range(0, n - i - 1):

            # Compare two adjacent elements
            if numbers[j] > numbers[j + 1]:

                # Swap the elements
                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )


# Driver Code
numbers = [75, 18, 42, 9, 56, 31, 84, 15]


print("Original Array:")
for number in numbers:
    print(number, end=" ")


# Sort the array
BubbleSort(numbers)


print("\n\nSorted Array:")
for number in numbers:
    print(number, end=" ")
