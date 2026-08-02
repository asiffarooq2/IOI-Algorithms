# ==========================================
# FIND PAIR WITH GIVEN SUM
# ==========================================

# Function to find a pair
# whose sum equals the target value
def findPairSum(numbers, size, target):

    for i in range(size):

        for j in range(size):

            # Same element cannot be used twice
            if i == j:
                continue

            # Check if pair gives target sum
            if numbers[i] + numbers[j] == target:

                return [
                    numbers[i],
                    numbers[j]
                ]

            # Since array is sorted,
            # stop if sum becomes too large
            if numbers[i] + numbers[j] > target:
                break

    # No pair found
    return 0


# Sorted array
numbers = [
    4, 7, 9, 12, 15, 18, 21, 25
]

# Target sum
target = 30


print("Array:", numbers)

print(
    "Target Sum:",
    target
)


# Function call
result = findPairSum(
    numbers,
    len(numbers),
    target
)


print(
    "Pair with sum equal to {} is: {}".format(
        target,
        result
    )
)
