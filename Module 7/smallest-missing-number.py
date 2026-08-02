# ==========================================
# SMALLEST MISSING NUMBER
# ==========================================

# Function to find the smallest missing number
# in a sorted list of distinct
# non-negative integers

def findSmallestMissing(numbers, left=None, right=None):

    # Initialize left and right indexes
    if left is None and right is None:

        left = 0
        right = len(numbers) - 1

    # Base case
    if left > right:

        return left

    # Find middle index
    mid = left + (right - left) // 2

    # If index and value are equal,
    # missing number must be on the right
    if numbers[mid] == mid:

        return findSmallestMissing(
            numbers,
            mid + 1,
            right
        )

    # Otherwise missing number
    # must be on the left
    else:

        return findSmallestMissing(
            numbers,
            left,
            mid - 1
        )


# Driver Code
if __name__ == '__main__':

    numbers = [
        0, 1, 2, 3, 4,
        6, 7, 9, 12
    ]

    print(
        "Numbers:",
        numbers
    )

    print(
        "The smallest missing number is:",
        findSmallestMissing(numbers)
    )
