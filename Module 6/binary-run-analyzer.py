# ================================
# BINARY RUN ANALYZER
# ================================
# Topics:
# Binary Arrays
# Streak Counter with Reset
# Best-Streak Tracker
# Same-Direction Two Pointers
# Write-Pointer Pattern

print("================================")
print("BINARY RUN ANALYZER")
print("================================")


# ------------------------------------------------
# PART 1 - BINARY ARRAYS
# ------------------------------------------------

binary_values = [
    1, 0, 1, 1, 0,
    1, 1, 1, 1, 0, 1
]

print("\nPART 1: Binary Arrays")

print("Binary Array:", binary_values)

print(
    "The array contains only "
    "binary values 0 and 1."
)


# ------------------------------------------------
# PART 2 - STREAK COUNTER WITH RESET
# ------------------------------------------------

current_run = 0

print("\nPART 2: Streak Counter with Reset")

for value in binary_values:

    if value == 1:

        current_run = current_run + 1

    else:

        current_run = 0

    print(
        "Value:", value,
        "| Current Run:", current_run
    )


# ------------------------------------------------
# PART 3 - BEST-STREAK TRACKER
# ------------------------------------------------

current_run = 0
longest_run = 0

print("\nPART 3: Best-Streak Tracker")

for value in binary_values:

    if value == 1:

        current_run = current_run + 1

        longest_run = max(
            longest_run,
            current_run
        )

    else:

        current_run = 0


print(
    "Longest Consecutive Run of 1s:",
    longest_run
)


# ------------------------------------------------
# PART 4 - SAME-DIRECTION TWO POINTERS
# ------------------------------------------------

numbers = [
    7, 0, 15, 0,
    0, 24, 8, 0, 36
]

print("\nPART 4: Same-Direction Two Pointers")

print("Original Array:", numbers)

write_position = 0


for read_position in range(len(numbers)):

    if numbers[read_position] != 0:

        numbers[write_position] = (
            numbers[read_position]
        )

        write_position = (
            write_position + 1
        )


print(
    "After Moving Non-Zero Values:",
    numbers
)


# ------------------------------------------------
# PART 5 - WRITE-POINTER PATTERN
# ------------------------------------------------

print("\nPART 5: Write-Pointer Pattern")


while write_position < len(numbers):

    numbers[write_position] = 0

    write_position = (
        write_position + 1
    )


print(
    "Final Array:",
    numbers
)


# ------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------

print("\n================================")
print("BINARY RUN ANALYZER SUMMARY")
print("================================")

print(
    "Binary arrays contain only "
    "0 and 1 values."
)

print(
    "The streak increases when "
    "a 1 is found."
)

print(
    "The streak resets to 0 "
    "when a 0 is found."
)

print(
    "The best-streak tracker remembers "
    "the longest sequence of 1s."
)

print(
    "Read and write pointers move "
    "through the array from left to right."
)

print(
    "The write pointer places non-zero "
    "values at the front of the array."
)

print("================================")
