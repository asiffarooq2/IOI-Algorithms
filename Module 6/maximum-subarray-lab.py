# ==========================================
# MAXIMUM SUBARRAY LAB
# Topics:
# Subarrays
# Negative Values
# Running Sum with Reset
# Maximum Sum Tracker
# Kadane's Algorithm
# ==========================================


# ------------------------------------------
# PART 1 - SUBARRAYS
# ------------------------------------------

numbers = [4, -7, 5, 2, -3, 8, -2]

print("Full Array:", numbers)

print("\nSome Subarrays:")

print(
    "[0:3] =",
    numbers[0:3],
    "Sum =",
    sum(numbers[0:3])
)

print(
    "[2:6] =",
    numbers[2:6],
    "Sum =",
    sum(numbers[2:6])
)

print(
    "[4:7] =",
    numbers[4:7],
    "Sum =",
    sum(numbers[4:7])
)


# ------------------------------------------
# PART 2 - RUNNING SUM WITH RESET
# ------------------------------------------

print("\nRunning Sum Trace:")

running_sum = 0

for value in numbers:

    running_sum += value

    if running_sum < 0:

        print(
            value,
            "-> Sum =",
            running_sum,
            "<-- Negative! Reset to 0"
        )

        running_sum = 0

    else:

        print(
            value,
            "-> Sum =",
            running_sum
        )


# ------------------------------------------
# PART 3 - MAXIMUM SUM TRACKER
# ------------------------------------------

running_sum = 0
maximum_sum = 0

for value in numbers:

    running_sum += value

    if running_sum < 0:
        running_sum = 0

    if running_sum > maximum_sum:
        maximum_sum = running_sum


print("\nArray:", numbers)

print(
    "Maximum Subarray Sum:",
    maximum_sum
)


# ------------------------------------------
# PART 4 - KADANE'S ALGORITHM
# ------------------------------------------

challenge = [
    3, -2, 6, -8, 4,
    7, -3, 5, -12, 9
]

running_sum = 0
maximum_sum = 0


for value in challenge:

    running_sum += value

    # Drop a negative running sum
    if running_sum < 0:
        running_sum = 0

    # Remember the best sum found
    if running_sum > maximum_sum:
        maximum_sum = running_sum


print("\nChallenge Array:", challenge)

print(
    "Maximum Subarray Sum:",
    maximum_sum
)
