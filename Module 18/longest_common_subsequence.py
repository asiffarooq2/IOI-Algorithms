
# Dynamic Programming: Find the Longest Common Subsequence

def find_longest_common_subsequence(first_string, second_string):
    first_length = len(first_string)
    second_length = len(second_string)

    # Create a table to store LCS lengths
    lcs_table = [
        [0] * (second_length + 1)
        for _ in range(first_length + 1)
    ]

    # Fill the table using Dynamic Programming
    for first_index in range(1, first_length + 1):
        for second_index in range(1, second_length + 1):

            if first_string[first_index - 1] == second_string[second_index - 1]:
                lcs_table[first_index][second_index] = (
                    lcs_table[first_index - 1][second_index - 1] + 1
                )
            else:
                lcs_table[first_index][second_index] = max(
                    lcs_table[first_index - 1][second_index],
                    lcs_table[first_index][second_index - 1]
                )

    # Reconstruct the longest common subsequence
    common_subsequence = ""
    first_index = first_length
    second_index = second_length

    while first_index > 0 and second_index > 0:

        if first_string[first_index - 1] == second_string[second_index - 1]:
            common_subsequence = (
                first_string[first_index - 1] + common_subsequence
            )
            first_index -= 1
            second_index -= 1

        elif (
            lcs_table[first_index - 1][second_index]
            > lcs_table[first_index][second_index - 1]
        ):
            first_index -= 1

        else:
            second_index -= 1

    return common_subsequence


# Example usage
first_string = "ABCDGH"
second_string = "AEDFHR"

longest_subsequence = find_longest_common_subsequence(
    first_string, second_string
)

print(f"The longest common subsequence: {longest_subsequence}")
