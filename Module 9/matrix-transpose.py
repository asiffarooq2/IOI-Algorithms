# ==========================================
# MATRIX TRANSPOSE
# ==========================================


# Initialize matrix
matrix = [
    [5, 2, 7],
    [8, 4, 1],
    [6, 9, 3]
]


# Initialize result matrix
transpose = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


# Find transpose of matrix
for i in range(len(matrix)):

    for j in range(len(matrix[0])):

        # Convert rows into columns
        transpose[i][j] = matrix[j][i]


# Display original matrix
print("Original Matrix:")

for row in matrix:
    print(row)


# Display transpose matrix
print("\nTranspose Matrix:")

for row in transpose:
    print(row)
