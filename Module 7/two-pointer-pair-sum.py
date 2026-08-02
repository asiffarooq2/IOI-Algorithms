# ==========================================
# FIND PAIR WITH GIVEN SUM
# USING TWO-POINTER TECHNIQUE
# ==========================================


# Function to find a pair
# whose sum equals the target
def findPairSum(numbers, size, target):

    # First pointer starts from beginning
    left = 0

    # Second pointer starts from end
    right = size - 1

    while left < right:

        # Calculate current sum
        current_sum = (
            numbers[left] + numbers[right]
        )

        # Pair found
        if current_sum == target:

            return [
                numbers[left],
                numbers[right]
            ]

        # Sum is smaller than target
        # Move left pointer forward
        elif current_sum < target:

            left += 1

        # Sum is greater than target
        # Move right pointer backward
        else:

            right -= 1

    # No pair found
    return 0


# Sorted array
numbers = [
    5, 8, 12, 16, 20, 24, 30, 35
]

# Target sum
target = 44


print("Array:", numbers)
print("Target Sum:", target)


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
