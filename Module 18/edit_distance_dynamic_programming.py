
# Dynamic Programming: Minimum Edit Distance Problem

def calculate_edit_distance(first_string, second_string):

    # Get the lengths of both strings
    first_length = len(first_string)
    second_length = len(second_string)

    # Create a table to store minimum edit operations
    edit_distance_table = [
        [0] * (second_length + 1)
        for _ in range(first_length + 1)
    ]

    # Initialize the first column (deletion operations)
    for row in range(first_length + 1):
        edit_distance_table[row][0] = row

    # Initialize the first row (insertion operations)
    for column in range(second_length + 1):
        edit_distance_table[0][column] = column

    # Fill the table using Dynamic Programming
    for row in range(1, first_length + 1):
        for column in range(1, second_length + 1):

            # If characters match, no additional operation is needed
            if first_string[row - 1] == second_string[column - 1]:
                edit_distance_table[row][column] = (
                    edit_distance_table[row - 1][column - 1]
                )

            # Otherwise, choose the minimum cost operation
            else:
                insertion = edit_distance_table[row][column - 1]
                deletion = edit_distance_table[row - 1][column]
                replacement = edit_distance_table[row - 1][column - 1]

                edit_distance_table[row][column] = (
                    1 + min(insertion, deletion, replacement)
                )

    # Return the minimum number of edit operations
    return edit_distance_table[first_length][second_length]


# Main program
if __name__ == "__main__":
    first_string = "kitten"
    second_string = "sitting"

    minimum_edit_distance = calculate_edit_distance(
        first_string, second_string
    )

    print("The minimum edit distance:", minimum_edit_distance)
