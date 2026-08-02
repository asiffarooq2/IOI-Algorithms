# ==========================================
# ARRAY BALANCE AND WINDOW LAB
# Topics:
# Array Slices
# Left and Right Sums
# Equilibrium Point
# Growing Subarray Window
# Target Sum Subarray
# ==========================================


# ------------------------------------------
# PART 1 - SLICES AND THEIR SUMS
# ------------------------------------------

arr = [3, 2, 4, 5, 1, 6, 7]

print("Full Array:", arr)

print("Left of index 3 :", arr[:3])
print("Right of index 3:", arr[4:])

print(
    "Left Sum at index 3 :",
    sum(arr[:3])
)

print(
    "Right Sum at index 3:",
    sum(arr[4:])
)


# ------------------------------------------
# PART 2 - BALANCE AT EVERY INDEX
# ------------------------------------------

print("\nBalance Check:")

for i in range(len(arr)):

    left_sum = sum(arr[:i])

    right_sum = sum(
        arr[i + 1:]
    )

    print(
        "Index",
        i,
        "-> Left:",
        left_sum,
        "Right:",
        right_sum
    )


# ------------------------------------------
# PART 3 - EQUILIBRIUM POINT
# ------------------------------------------

balance_arr = [2, 4, 3, 6, 3]

print("\nEquilibrium Point:")

print(
    "Array:",
    balance_arr
)

found_balance = False

for i in range(len(balance_arr)):

    left_sum = sum(
        balance_arr[:i]
    )

    right_sum = sum(
        balance_arr[i + 1:]
    )

    if left_sum == right_sum:

        print(
            "Index:",
            i,
            "Element:",
            balance_arr[i]
        )

        found_balance = True


if not found_balance:

    print("No equilibrium point found.")


# ------------------------------------------
# PART 4 - GROWING SUBARRAY WINDOW
# ------------------------------------------

numbers = [
    4, 3, 5, 2, 8, 1, 6, 9
]

target = 15

start = 1

print(
    "\nGrowing Window "
    "(start =",
    start,
    ", target =",
    target,
    "):"
)

current_sum = 0


for j in range(
    start,
    len(numbers)
):

    current_sum += numbers[j]

    print(
        "numbers[",
        start,
        "to",
        j,
        "] =",
        numbers[start:j + 1],
        "Sum =",
        current_sum
    )

    if current_sum >= target:
        break


# ------------------------------------------
# PART 5 - FIND SUBARRAY WITH TARGET SUM
# ------------------------------------------

print("\nSearching All Windows:")

found = False


for i in range(len(numbers)):

    if found:
        break

    current_sum = 0

    for j in range(
        i,
        len(numbers)
    ):

        current_sum += numbers[j]

        # Target found
        if current_sum == target:

            print(
                "Found! Indexes",
                i,
                "to",
                j,
                ":",
                numbers[i:j + 1]
            )

            found = True

            break

        # Stop because all values
        # are positive
        if current_sum > target:
            break


if not found:

    print(
        "No subarray with target sum found."
    )
