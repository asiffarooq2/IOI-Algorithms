# ================================
# ARRAY POWER TRACKER
# ================================
# Topics:
# Subarrays
# Effect of Negative Numbers
# Running Sum with Reset
# Maximum-So-Far Tracker
# Kadane's Algorithm

print("================================")
print("ARRAY POWER TRACKER")
print("================================")


# ------------------------------------------------
# PART 1 - SUBARRAYS
# ------------------------------------------------

power_levels = [6, -4, 2, 8, -5, 3, 7, -9, 5]

print("\nPART 1: Subarrays")
print("Full Array:", power_levels)

print(
    "Subarray [0:4]:",
    power_levels[0:4],
    "Sum:",
    sum(power_levels[0:4])
)

print(
    "Subarray [2:7]:",
    power_levels[2:7],
    "Sum:",
    sum(power_levels[2:7])
)

print(
    "Subarray [5:9]:",
    power_levels[5:9],
    "Sum:",
    sum(power_levels[5:9])
)


# ------------------------------------------------
# PART 2 - EFFECT OF NEGATIVE NUMBERS
# ------------------------------------------------

print("\nPART 2: Effect of Negative Numbers")

running_sum = 0

for power in power_levels:

    running_sum = running_sum + power

    print(
        "Power:",
        power,
        "| Running Sum:",
        running_sum
    )


# ------------------------------------------------
# PART 3 - RUNNING SUM WITH RESET
# ------------------------------------------------

print("\nPART 3: Running Sum with Reset")

running_sum = 0

for power in power_levels:

    running_sum = running_sum + power

    if running_sum < 0:

        print(
            "Power:",
            power,
            "| Running Sum:",
            running_sum,
            "-> Reset to 0"
        )

        running_sum = 0

    else:

        print(
            "Power:",
            power,
            "| Running Sum:",
            running_sum
        )


# ------------------------------------------------
# PART 4 - MAX-SO-FAR TRACKER
# ------------------------------------------------

print("\nPART 4: Maximum-So-Far Tracker")

running_sum = 0
max_so_far = 0

for power in power_levels:

    running_sum = running_sum + power

    if running_sum < 0:
        running_sum = 0

    if running_sum > max_so_far:
        max_so_far = running_sum

    print(
        "Power:",
        power,
        "| Running Sum:",
        running_sum,
        "| Maximum So Far:",
        max_so_far
    )


# ------------------------------------------------
# PART 5 - KADANE'S ALGORITHM
# ------------------------------------------------

def kadane_algorithm(arr):

    running_sum = 0
    max_sum = arr[0]

    for number in arr:

        running_sum = running_sum + number

        if running_sum > max_sum:
            max_sum = running_sum

        if running_sum < 0:
            running_sum = 0

    return max_sum


print("\nPART 5: Kadane's Algorithm")

best_power = kadane_algorithm(power_levels)

print("Power Levels:", power_levels)

print(
    "Maximum Subarray Sum:",
    best_power
)


# ------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------

print("\n================================")
print("ARRAY POWER TRACKER SUMMARY")
print("================================")

print(
    "Subarrays are continuous sections "
    "of an array."
)

print(
    "Negative values can decrease "
    "the running sum."
)

print(
    "The running sum is reset when "
    "it becomes negative."
)

print(
    "Maximum-so-far remembers the "
    "best sum found."
)

print(
    "Kadane's Algorithm finds the maximum "
    "subarray sum efficiently."
)

print("================================")
