# ================================
# ARRAY TARGET SEARCH LAB
# ================================
# Topics:
# Slices and Their Sums
# Left-Right Balance
# Equilibrium Point
# Subarray Window
# Target Sum Search

print("================================")
print("ARRAY TARGET SEARCH LAB")
print("================================")


# ------------------------------------------------
# PART 1 - SLICES AND THEIR SUMS
# ------------------------------------------------

numbers = [5, 3, -2, 4, 1, 2, 3]

print("\nPART 1: Slices and Their Sums")
print("Full Array:", numbers)

index = 3

left_slice = numbers[:index]
right_slice = numbers[index + 1:]

print(
    "Left of index",
    index,
    ":",
    left_slice
)

print(
    "Right of index",
    index,
    ":",
    right_slice
)

print(
    "Left Sum:",
    sum(left_slice)
)

print(
    "Right Sum:",
    sum(right_slice)
)


# ------------------------------------------------
# PART 2 - LEFT-RIGHT BALANCE
# ------------------------------------------------

print("\nPART 2: Left-Right Balance")

for i in range(len(numbers)):

    left_sum = sum(
        numbers[:i]
    )

    right_sum = sum(
        numbers[i + 1:]
    )

    print(
        "Index",
        i,
        "-> Left Sum:",
        left_sum,
        "| Right Sum:",
        right_sum
    )


# ------------------------------------------------
# PART 3 - EQUILIBRIUM POINT
# ------------------------------------------------

balance_numbers = [4, 2, 3, 9, 5, 4]

print("\nPART 3: Equilibrium Point")
print("Array:", balance_numbers)

equilibrium_found = False

for i in range(len(balance_numbers)):

    left_sum = sum(
        balance_numbers[:i]
    )

    right_sum = sum(
        balance_numbers[i + 1:]
    )

    if left_sum == right_sum:

        print(
            "Equilibrium found at index:",
            i
        )

        print(
            "Element:",
            balance_numbers[i]
        )

        equilibrium_found = True


if equilibrium_found == False:

    print("No equilibrium point found.")


# ------------------------------------------------
# PART 4 - SUBARRAY WINDOW
# ------------------------------------------------

values = [2, 5, 3, 4, 6, 1]

print("\nPART 4: Subarray Window")
print("Array:", values)

window_sum = 0

for i in range(len(values)):

    window_sum = (
        window_sum + values[i]
    )

    print(
        "Window from index 0 to",
        i,
        ":",
        values[:i + 1],
        "| Sum:",
        window_sum
    )


# ------------------------------------------------
# PART 5 - TARGET SUM SEARCH
# ------------------------------------------------

target = 12

print("\nPART 5: Target Sum Search")

print(
    "Target Sum:",
    target
)

found = False

for start in range(len(values)):

    current_sum = 0

    for end in range(
        start,
        len(values)
    ):

        current_sum = (
            current_sum + values[end]
        )

        if current_sum == target:

            print(
                "Target Subarray Found:",
                values[start:end + 1]
            )

            print(
                "Start Index:",
                start
            )

            print(
                "End Index:",
                end
            )

            found = True


if found == False:

    print(
        "No subarray found "
        "with target sum."
    )


# ------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------

print("\n================================")
print("ARRAY TARGET SEARCH SUMMARY")
print("================================")

print(
    "Slices divide an array "
    "into smaller sections."
)

print(
    "Left-right balance compares "
    "the sums on both sides."
)

print(
    "An equilibrium point has equal "
    "left and right sums."
)

print(
    "A subarray is a continuous "
    "section of an array."
)

print(
    "Target sum search finds a "
    "continuous subarray with the "
    "required total."
)

print("================================")
