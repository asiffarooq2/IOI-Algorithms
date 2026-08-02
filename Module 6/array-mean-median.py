# Mean of an array = sum of elements / number of elements
def arrayMean(arr, arr_size):

    total_sum = 0

    for i in range(0, arr_size):
        total_sum += arr[i]

    return float(total_sum / arr_size)


# Median depends on whether
# the array size is even or odd
def arrayMedian(arr, arr_size):

    # Sort the array
    arr = sorted(arr)

    # Odd number of elements
    if arr_size % 2 != 0:
        return float(arr[int(arr_size / 2)])

    # Even number of elements
    return float(
        (
            arr[int((arr_size - 1) / 2)]
            + arr[int(arr_size / 2)]
        ) / 2.0
    )


# Array with different values
arr = [12, 7, 15, 9, 20, 5, 18, 11]

arr_size = len(arr)


print("Array =", arr)

print(
    "Mean =",
    arrayMean(arr, arr_size)
)

print(
    "Median =",
    arrayMedian(arr, arr_size)
)