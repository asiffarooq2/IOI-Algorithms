# ==========================================
# COLUMN-WISE SUM OF A MATRIX
# ==========================================


# Initialize matrix
matrix = [
    [5, 3, 7],
    [2, 8, 4],
    [6, 1, 9]
]


# Variable to store column sum
answer = 0


# Iterate through columns
for i in range(len(matrix)):

    # Iterate through rows
    for j in range(len(matrix[0])):

        # Add elements column-wise
        answer = answer + matrix[j][i]

    # Print sum of current column
    print(answer, end=" ")

    # Reset for next column
    answer = 0
