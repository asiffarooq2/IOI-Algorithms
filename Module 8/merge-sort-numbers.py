# ==========================================
# MERGE SORT PROGRAM
# ==========================================

def mergeSorting(A):

    if len(A) > 1:

        # Find the middle of the array
        mid = len(A) // 2

        # Divide array into two halves
        left = A[:mid]
        right = A[mid:]

        # Recursive call on each half
        mergeSorting(left)
        mergeSorting(right)

        # Iterators for left and right halves
        i = 0
        j = 0

        # Iterator for the main array
        k = 0

        # Compare elements from both halves
        while i < len(left) and j < len(right):

            if left[i] <= right[j]:

                A[k] = left[i]
                i += 1

            else:

                A[k] = right[j]
                j += 1

            k += 1

        # Copy remaining values
        # from the left half
        while i < len(left):

            A[k] = left[i]
            i += 1
            k += 1

        # Copy remaining values
        # from the right half
        while j < len(right):

            A[k] = right[j]
            j += 1
            k += 1


# Array with different values
A = [74, 29, 91, 16, 53, 8, 67, 42, 35]


print("Unsorted Array: {}".format(A))


# Perform Merge Sort
mergeSorting(A)


print("Sorted Array: {}".format(A))
