# ==========================================
# LINEAR SEARCH PROGRAM
# ==========================================

# Function to search for an element
def search(numbers, size, target):

    # Check each element one by one
    for i in range(0, size):

        if numbers[i] == target:
            return i

    # Element was not found
    return -1


# Array with different values
numbers = [15, 28, 42, 67, 89, 105]

# Element to search
target = 67

# Size of array
size = len(numbers)


print("Array:", numbers)
print("Element to Search:", target)


# Function call
result = search(
    numbers,
    size,
    target
)


# Check the returned result
if result == -1:

    print(
        "Element is not present in the array."
    )

else:

    print(
        "Element is present at index",
        result
    )