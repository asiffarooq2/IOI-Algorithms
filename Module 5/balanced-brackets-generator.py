# ==============================================
# ACTIVITY - BALANCED BRACKETS GENERATOR
# ==============================================
# Generate all valid combinations of n pairs
# of square brackets []
#
# Example:
# n = 2
#
# [][]
# [[]]
# ==============================================


def generate_brackets(s, left, right, position, n):

    # Base case:
    # All positions have been filled
    if position == 2 * n:

        for bracket in s:
            print(bracket, end="")

        print()
        return

    # Add closing bracket
    # Only allowed when there are more
    # opening brackets than closing brackets
    if left > right:

        s[position] = "]"

        generate_brackets(
            s,
            left,
            right + 1,
            position + 1,
            n
        )

    # Add opening bracket
    # Only allowed if we have not used
    # all opening brackets
    if left < n:

        s[position] = "["

        generate_brackets(
            s,
            left + 1,
            right,
            position + 1,
            n
        )


# Ask user for number of bracket pairs
n = int(
    input("Enter number of bracket pairs: ")
)


# Create empty list for brackets
s = [""] * (2 * n)


print("\nValid Balanced Brackets:\n")


# Start recursion
generate_brackets(
    s,
    0,
    0,
    0,
    n
)
