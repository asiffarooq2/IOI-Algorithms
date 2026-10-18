
# Recursive solution to the Minimum Edit Distance Problem

def calculate_edit_distance(first_string, second_string,
                            first_length, second_length):

    # If the first string is empty, insert all characters
    # of the second string
    if first_length == 0:
        return second_length

    # If the second string is empty, delete all characters
    # of the first string
    if second_length == 0:
        return first_length

    # If the last characters match, ignore them
    # and solve the remaining subproblem
    if first_string[first_length - 1] == second_string[second_length - 1]:
        return calculate_edit_distance(
            first_string, second_string,
            first_length - 1, second_length - 1
        )

    # Consider insertion, deletion, and replacement
    insertion_cost = calculate_edit_distance(
        first_string, second_string,
        first_length, second_length - 1
    )

    deletion_cost = calculate_edit_distance(
        first_string, second_string,
        first_length - 1, second_length
    )

    replacement_cost = calculate_edit_distance(
        first_string, second_string,
        first_length - 1, second_length - 1
    )

    # Return the minimum cost among the three operations
    return 1 + min(
        insertion_cost,
        deletion_cost,
        replacement_cost
    )


# Main program
first_string = "sunday"
second_string = "saturday"

minimum_edit_distance = calculate_edit_distance(
    first_string,
    second_string,
    len(first_string),
    len(second_string)
)

print("Minimum edit distance:", minimum_edit_distance)
