# ==========================================
# LEFT ROTATE ARRAY N TIMES
# ==========================================


# Function to rotate array n times
def rotations(numbers, n, size):

    for i in range(n):

        rotate(numbers, size)


# Function to rotate array
# to the left by one position
def rotate(numbers, size):

    # Store the first element
    temp = numbers[0]

    # Shift all elements one
    # position to the left
    for i in range(size - 1):

        numbers[i] = numbers[i + 1]

    # Move first element to the end
    numbers[size - 1] = temp


# Function to print the array
def printArray(numbers, size):

    for i in range(size):

        print(numbers[i], end=" ")

    print()


# Driver Code
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# Number of left rotations
n = 3


print("Original Array:")
printArray(
    numbers,
    len(numbers)
)


# Rotate the array
rotations(
    numbers,
    n,
    len(numbers)
)


print("\nArray After", n, "Left Rotations:")

printArray(
    numbers,
    len(numbers)
)
