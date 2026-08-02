# ==========================================
# FIX A NEARLY SORTED ARRAY
# ==========================================


# Function to sort an array where
# two elements are in the wrong positions
def sortArray(numbers):

    # Base case
    if len(numbers) <= 1:
        return

    first = -1
    second = -1

    previous = numbers[0]

    # Check adjacent elements
    for i in range(1, len(numbers)):

        # Find where sorting order breaks
        if previous > numbers[i]:

            # First conflict
            if first == -1:

                first = i - 1
                second = i

            # Second conflict
            else:

                second = i

        previous = numbers[i]

    # Swap the misplaced elements
    swap(
        numbers,
        first,
        second
    )


# Function to swap two elements
def swap(numbers, i, j):

    temp = numbers[i]

    numbers[i] = numbers[j]

    numbers[j] = temp


# Driver Code
if __name__ == '__main__':

    numbers = [
        10, 20, 50, 40, 30, 60, 70
    ]

    print(
        "Original Array:",
        numbers
    )

    sortArray(numbers)

    print(
        "Sorted Array:",
        numbers
    )
