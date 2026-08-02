# ==========================================
# MATRIX MULTIPLICATION
# ==========================================


# Initialize first matrix
matrix1 = [
    [2, 3],
    [4, 5]
]


# Initialize second matrix
matrix2 = [
    [6, 7],
    [8, 9]
]


# Initialize result matrix
result = [
    [0, 0],
    [0, 0]
]


# Iterate through rows of matrix1
for i in range(len(matrix1)):

    # Iterate through columns of matrix2
    for j in range(len(matrix2[0])):

        # Multiply corresponding elements
        # and add them
        for k in range(len(matrix2)):

            result[i][j] += (
                matrix1[i][k]
                * matrix2[k][j]
            )


# Display matrices
print("First Matrix:")
for row in matrix1:
    print(row)


print("\nSecond Matrix:")
for row in matrix2:
    print(row)


print("\nMatrix After Multiplication:")
for row in result:
    print(row)
