# ==========================================
# ITERATIVE BINARY SEARCH
# ==========================================

# Function to search for an element
def binarySearch(numbers, left, right, target):

    while left <= right:

        # Find middle index
        mid = left + (right - left) // 2

        # Target found
        if numbers[mid] == target:
            return mid

        # Target is greater than middle value
        # Search the right half
        elif numbers[mid] < target:
            left = mid + 1

        # Target is smaller than middle value
        # Search the left half
        else:
            right = mid - 1

    # Target was not found
    return -1


# Sorted array
numbers = [5, 12, 18, 27, 35, 48, 63, 79]

# Number to search
target = 48


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

    print(
        "Element is not present in the array."
    )
