# ==========================================
# MATRIX ADDITION
# ==========================================


# Initialize first matrix
matrix1 = [
    [5, 7],
    [2, 9]
]


# Initialize second matrix
matrix2 = [
    [4, 3],
    [8, 6]
]


# Initialize result matrix
result = [
    [0, 0],
    [0, 0]
]


# Add corresponding elements
# of both matrices
for i in range(len(matrix1)):

    for j in range(len(matrix1[0])):

        result[i][j] = (
            matrix1[i][j]
            + matrix2[i][j]
        )


# Display matrices
print("First Matrix:")
for row in matrix1:
    print(row)


print("\nSecond Matrix:")
for row in matrix2:
    print(row)


print("\nMatrix After Addition:")
for row in result:
    print(row)
