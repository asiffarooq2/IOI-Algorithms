# ==========================================
# UNION OF TWO SORTED ARRAYS
# ==========================================


# Function to find the union
# of two sorted arrays
def unionOfArrays(array1, array2, m, n):

    # Initialize two pointers
    i = 0
    j = 0

    # Compare elements from both arrays
    while i < m and j < n:

        # Element in first array is smaller
        if array1[i] < array2[j]:

            print(array1[i], end=" ")
            i += 1

        # Element in second array is smaller
        elif array2[j] < array1[i]:

            print(array2[j], end=" ")
            j += 1

        # Both elements are equal
        else:

            print(array1[i], end=" ")

            i += 1
            j += 1

    # Print remaining elements
    # from the first array
    while i < m:

        print(array1[i], end=" ")
        i += 1

    # Print remaining elements
    # from the second array
    while j < n:

        print(array2[j], end=" ")
        j += 1


# Driver Code
array1 = [2, 4, 6, 10, 14, 18]
array2 = [1, 4, 7, 10, 15, 20]

m = len(array1)
n = len(array2)


print("First Array:", array1)
print("Second Array:", array2)

print("\nUnion of Arrays:")

unionOfArrays(
    array1,
    array2,
    m,
    n
)
