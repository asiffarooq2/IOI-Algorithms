# ==========================================
# BINARY ARRAY POINTER LAB
# Topics:
# Binary Arrays
# Streak Counter with Reset
# Best-Streak Tracker
# Same-Direction Two Pointers
# Write-Pointer Pattern
# ==========================================


# ------------------------------------------
# PART 1 - STREAK COUNTER WITH RESET
# ------------------------------------------

binary = [
    1, 0, 1, 1, 1, 0,
    1, 1, 0, 1, 1, 1, 1, 1
]

streak = 0

print("PART 1: Streak Counter")

for num in binary:

    if num == 0:

        # Reset streak when 0 appears
        streak = 0

    else:

        # Increase streak when 1 appears
        streak += 1

    print(
        num,
        "->",
        streak
    )

print()


# ------------------------------------------
# PART 2 - BEST-STREAK TRACKER
# ------------------------------------------

streak = 0
best = 0

for num in binary:

    if num == 0:

        streak = 0

    else:

        streak += 1

        if streak > best:

            best = streak


print("Binary Array:", binary)

print(
    "Maximum Consecutive 1s:",
    best
)

print()


# ------------------------------------------
# PART 3 - SAME-DIRECTION TWO POINTERS
# Move all zeros to the end
# ------------------------------------------

numbers = [
    0, 12, 0, 45, 67,
    0, 8, 0, 90, 23, 0
]

print("Before:", numbers)


# Points to position where next
# non-zero value should be placed
write = 0


for current in range(len(numbers)):

    if numbers[current] != 0:

        numbers[current], numbers[write] = (
            numbers[write],
            numbers[current]
        )

        write += 1


print("After: ", numbers)

print()


# ------------------------------------------
# PART 4 - WRITE POINTER RESULT
# ------------------------------------------

print(
    "Write Pointer Stopped At:",
    write
)

print(
    "Non-Zero Elements at Front:",
    write
)

print(
    "Zeros at End:",
    len(numbers) - write
)
