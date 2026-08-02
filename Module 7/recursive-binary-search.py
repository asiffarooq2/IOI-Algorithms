# ==========================================
# RECURSIVE BINARY SEARCH
# ==========================================

# Function to perform binary search recursively
def binarySearch(numbers, left, right, target):

    # Check if search range is valid
    if right >= left:

        # Find the middle index
        mid = left + (right - left) // 2

        # Target found
        if numbers[mid] == target:
            return mid

        # Target is smaller than middle element
        # Search in the left half
        elif numbers[mid] > target:

            return binarySearch(
                numbers,
                left,
                mid - 1,
                target
            )

        # Target is greater than middle element
        # Search in the right half
        else:

            return binarySearch(
                numbers,
                mid + 1,
                right,
                target
            )

    # Target was not found
    else:
        return -1


# Sorted array
numbers = [8, 14, 21, 29, 36, 47, 58, 72, 90]

# Number to search
target = 58


print("Array:", numbers)
print("Number to Search:", target)


# Function call
result = binarySearch(
    numbers,
    0,
    len(numbers) - 1,
    target
)


# Display result
if result != -1:

    print(
        "Element {} is present at index {}".format(
            target,
            result
        )
    )

else:

    print("Element is not present in the array.")
