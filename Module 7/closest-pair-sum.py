# ==========================================
# FIND PAIR WITH SUM CLOSEST TO TARGET
# Using Two-Pointer Technique
# ==========================================

MAX_VALUE = 100000000


# Function to find the pair
# whose sum is closest to target
def findClosestPair(numbers, size, target):

    # Store indexes of closest pair
    result_left = 0
    result_right = 0

    # Left and right pointers
    left = 0
    right = size - 1

    # Initial large difference
    difference = MAX_VALUE

    while right > left:

        # Calculate current pair sum
        current_sum = (
            numbers[left] + numbers[right]
        )

        # Calculate difference from target
        current_difference = abs(
            current_sum - target
        )

        # Check if current pair is closer
        if current_difference < difference:

            result_left = left
            result_right = right

            difference = current_difference

        # Current sum is greater than target
        # Move right pointer left
        if current_sum > target:

            right -= 1

        # Current sum is smaller than target
        # Move left pointer right
        else:

            left += 1

    print(
        "The closest pair to sum {} is {} and {}".format(
            target,
            numbers[result_left],
            numbers[result_right]
        )
    )


# Driver Code
if __name__ == "__main__":

    # Sorted array
    numbers = [
        5, 12, 18, 25, 32, 45, 60
    ]

    target = 50

    size = len(numbers)

    print("Array:", numbers)
    print("Target Sum:", target)

    findClosestPair(
        numbers,
        size,
        target
    )
