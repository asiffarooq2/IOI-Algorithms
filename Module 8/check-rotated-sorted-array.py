# ==========================================
# CHECK IF ARRAY IS ROTATED AND SORTED
# ==========================================

# Array with different values
numbers = [40, 50, 60, 10, 20, 30]

n = len(numbers)

# Count positions where
# sorting order breaks
count = 0


print("Array:", numbers)


# Compare adjacent elements
for i in range(1, n):

    if numbers[i - 1] > numbers[i]:

        count += 1


# Compare the last element
# with the first element
if numbers[n - 1] > numbers[0]:

    count += 1


# Display result
print(
    "Is the array rotated and sorted?",
    count <= 1
)
