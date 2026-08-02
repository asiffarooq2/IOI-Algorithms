# ================================
# ARRAY ROTATION LAB
# ================================
# Topics:
# Two-Pointer Swap
# Reverse in Groups
# Left Rotate by 1
# Left Rotate by n
# Leaders in an Array

print("================================")
print("ARRAY ROTATION LAB")
print("================================")


# ------------------------------------------------
# PART 1 - TWO-POINTER SWAP
# ------------------------------------------------

numbers = [15, 25, 35, 45, 55, 65]

print("\nPART 1: Two-Pointer Swap")
print("Original Numbers:", numbers)

start = 0
end = len(numbers) - 1

while start < end:

    numbers[start], numbers[end] = (
        numbers[end],
        numbers[start]
    )

    start = start + 1
    end = end - 1

print("Reversed Numbers:", numbers)


# ------------------------------------------------
# PART 2 - REVERSE IN GROUPS
# ------------------------------------------------

numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]

group_size = 4

print("\nPART 2: Reverse in Groups")
print("Original Numbers:", numbers)
print("Group Size:", group_size)

i = 0

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

        start = start + 1
        end = end - 1

    i = i + group_size

print("Numbers After Group Reverse:", numbers)


# ------------------------------------------------
# PART 3 - LEFT ROTATE BY 1
# ------------------------------------------------

numbers = [5, 10, 15, 20, 25, 30]

print("\nPART 3: Left Rotate by 1")
print("Original Numbers:", numbers)

first_number = numbers[0]

for i in range(len(numbers) - 1):

    numbers[i] = numbers[i + 1]

numbers[-1] = first_number

print("After Left Rotate by 1:", numbers)


# ------------------------------------------------
# PART 4 - LEFT ROTATE BY N
# ------------------------------------------------

numbers = [100, 200, 300, 400, 500, 600, 700]

n = 3

print("\nPART 4: Left Rotate by n")
print("Original Numbers:", numbers)
print("Rotate By:", n)

n = n % len(numbers)

for rotation in range(n):

    first_number = numbers[0]

    for i in range(len(numbers) - 1):

        numbers[i] = numbers[i + 1]

    numbers[-1] = first_number

print("After Left Rotate by n:", numbers)


# ------------------------------------------------
# PART 5 - LEADERS IN AN ARRAY
# ------------------------------------------------

numbers = [30, 25, 28, 12, 15, 8, 4]

leaders = []

print("\nPART 5: Leaders in an Array")
print("Numbers:", numbers)

# Last element is always a leader
max_from_right = numbers[-1]

leaders.append(max_from_right)

i = len(numbers) - 2

while i >= 0:

    if numbers[i] > max_from_right:

        max_from_right = numbers[i]

        leaders.append(numbers[i])

    i = i - 1

# Restore original left-to-right order
leaders.reverse()

print("Leaders:", leaders)


# ------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------

print("\n================================")
print("ARRAY ROTATION LAB SUMMARY")
print("================================")

print("Two-pointer swapping reverses the array.")

print(
    "Reverse in groups reverses elements "
    "inside fixed-size groups."
)

print(
    "Left rotate by 1 moves the first "
    "element to the end."
)

print(
    "Left rotate by n performs the "
    "rotation multiple times."
)

print(
    "A leader is an element greater than "
    "every element to its right."
)

print("================================")
