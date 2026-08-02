# Minimum Function
def findMinimum(numbers, size):

    temp = numbers[0]

    for i in range(1, size):
        temp = min(temp, numbers[i])

    return temp


# Maximum Function
def findMaximum(numbers, size):

    temp = numbers[0]

    for i in range(1, size):
        temp = max(temp, numbers[i])

    return temp


# Array with different values
numbers = [75, 23, 980, 41, 6, 150, 32]

size = len(numbers)


# Display results
print("Array:", numbers)

print(
    "Minimum element of array:",
    findMinimum(numbers, size)
)

print(
    "Maximum element of array:",
    findMaximum(numbers, size)
)
