# ==========================================
# INTERSECTION OF TWO SORTED ARRAYS
# ==========================================

# Initialize two sorted arrays
array1 = [2, 4, 6, 8, 11, 14, 18, 20]
array2 = [1, 4, 7, 8, 12, 14, 20, 25]

print("First Array:", array1)
print("Second Array:", array2)


# Store lengths of both arrays
m = len(array1)
n = len(array2)


# Initialize two pointers
i = 0
j = 0


print("\nIntersection:")

# Compare elements of both arrays
while i < m and j < n:

    # First array value is smaller
    if array1[i] < array2[j]:

        i += 1

    # Second array value is smaller
    elif array2[j] < array1[i]:

        j += 1

    # Both values are equal
    else:

        print(array1[i], end=" ")

        i += 1
        j += 1
