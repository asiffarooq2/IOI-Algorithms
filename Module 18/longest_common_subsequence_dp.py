
# Dynamic Programming: Longest Common Subsequence (LCS)

def find_lcs_length(first_string, second_string):

    # Get the lengths of both strings
    first_length = len(first_string)
    second_length = len(second_string)

    # Create a table to store LCS lengths
    lcs_table = [
        [0] * (second_length + 1)
        for _ in range(first_length + 1)
    ]

    # Fill the table using Dynamic Programming
    for first_index in range(first_length + 1):
        for second_index in range(second_length + 1):

            # Base case: if either string is empty
            if first_index == 0 or second_index == 0:
                lcs_table[first_index][second_index] = 0

            # If characters match, increase the LCS length
            elif first_string[first_index - 1] == second_string[second_index - 1]:
                lcs_table[first_index][second_index] = (
                    lcs_table[first_index - 1][second_index - 1] + 1
                )

            # Otherwise, take the maximum of the previous results
            else:
                lcs_table[first_index][second_index] = max(
                    lcs_table[first_index - 1][second_index],
                    lcs_table[first_index][second_index - 1]
                )

    # Return the length of the longest common subsequence
    return lcs_table[first_length][second_length]


# Main program
if __name__ == '__main__':
    first_string = "AGGTAB"
    second_string = "GXTXAYB"

    lcs_length = find_lcs_length(first_string, second_string)

    print("Length of LCS is", lcs_length)
