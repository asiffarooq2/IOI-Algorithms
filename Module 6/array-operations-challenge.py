# ==========================================
# ARRAY OPERATIONS CHALLENGE
# Topics:
# Two-Pointer Swap
# Reverse in Groups
# Left Rotate by N
# Leaders in an Array
# ==========================================


# ------------------------------------------
# PART 1 - TWO-POINTER SWAP
# ------------------------------------------

numbers = [15, 25, 35, 45, 55, 65]

print("Original Array:", numbers)

start = 0
end = len(numbers) - 1

while start < end:

    numbers[start], numbers[end] = (
        numbers[end],
        numbers[start]
    )

    start += 1
    end -= 1

print("Swapped Array:", numbers)
print()


# ------------------------------------------
# PART 2 - REVERSE IN GROUPS
# ------------------------------------------

numbers = [
    10, 20, 30, 40,
    50, 60, 70, 80
]

group_size = 4
i = 0

print("Original Array:", numbers)

while i < len(numbers):

    start = i

    end = min(
        i + group_size - 1,
        len(numbers) - 1
    )

    while start < end:

        numbers[start], numbers[end] = (
            numbers[end],
            numbers[start]
        )

        start += 1
        end -= 1

    i += group_size


print(
    "Reversed in groups of 4:",
    numbers
)

print()


# ------------------------------------------
# PART 3 - LEFT ROTATE BY N
# ------------------------------------------

numbers = [5, 10, 15, 20, 25, 30]

rotate_by = 3

print("Original Array:", numbers)

for _ in range(rotate_by):

    temp = numbers[0]

    for i in range(1, len(numbers)):

        numbers[i - 1] = numbers[i]

    numbers[-1] = temp


print(
    "Rotated left by 3:",
    numbers
)

print()


# ------------------------------------------
# PART 4 - LEADERS IN AN ARRAY
# ------------------------------------------

numbers = [
    25, 18, 20, 7, 12, 6, 3
]

print("Array:", numbers)

max_right = numbers[-1]

leaders = [max_right]


# Start from second-last element
for i in range(
    len(numbers) - 2,
    -1,
    -1
):

    if numbers[i] > max_right:

        max_right = numbers[i]

        leaders.append(
            numbers[i]
        )


# Reverse leaders to restore
# their original order
leaders.reverse()


print("Leaders:", leaders)
