# ================================
# REVERSE AND POWER RECURSION
# ================================
# Topics:
# Extracting Digits with % and //
# Reversing a Number with Recursion
# Reversing a String with Recursion
# Checking Powers of 5 with Recursion
# Stopping Conditions

print("================================")
print("REVERSE AND POWER RECURSION")
print("================================")


# ------------------------------------------------
# PART 1 - EXTRACTING DIGITS WITH % AND //
# ------------------------------------------------

number = 7359
temp = number

print("\nPART 1: Extracting Digits")
print("Original Number:", number)

while temp > 0:

    last_digit = temp % 10
    remaining_number = temp // 10

    print(
        "Last Digit:", last_digit,
        "| Remaining Number:", remaining_number
    )

    temp = remaining_number


# ------------------------------------------------
# PART 2 - REVERSING A NUMBER WITH RECURSION
# ------------------------------------------------

def count_digits(num):

    # Base case
    if num < 10:
        return 1

    return 1 + count_digits(num // 10)


def reverse_number(num):

    # Base case
    if num < 10:
        return num

    last_digit = num % 10
    remaining_number = num // 10

    digits_left = count_digits(remaining_number)

    return (
        last_digit * (10 ** digits_left)
        + reverse_number(remaining_number)
    )


print("\nPART 2: Reversing a Number")

num = 7359

print("Original Number:", num)
print("Reversed Number:", reverse_number(num))


# ------------------------------------------------
# PART 3 - REVERSING A STRING WITH RECURSION
# ------------------------------------------------

def reverse_string(text):

    # Base case
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


print("\nPART 3: Reversing a String")

word = "PYTHON"

print("Original String:", word)
print("Reversed String:", reverse_string(word))


# ------------------------------------------------
# PART 4 - CHECKING POWERS OF 5
# ------------------------------------------------

def is_power_of_5(num):

    # Stopping condition 1
    if num <= 0:
        return False

    # Stopping condition 2
    if num == 1:
        return True

    # If not divisible by 5
    if num % 5 != 0:
        return False

    # Recursive call
    return is_power_of_5(num // 5)


print("\nPART 4: Checking Powers of 5")

numbers = [
    1,
    5,
    10,
    25,
    50,
    125,
    200,
    625
]

for value in numbers:

    print(
        value,
        "is power of 5:",
        is_power_of_5(value)
    )


# ------------------------------------------------
# PART 5 - STOPPING CONDITIONS
# ------------------------------------------------

print("\nPART 5: Stopping Conditions")

print(
    "Stopping condition 1: "
    "num <= 0 returns False."
)

print(
    "Stopping condition 2: "
    "num == 1 returns True."
)

print(
    "String recursion stops when "
    "the string has 0 or 1 character."
)


# ------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------

print("\n================================")
print("REVERSE AND POWER SUMMARY")
print("================================")

print("% gives the last digit of a number.")

print("// removes the last digit of a number.")

print(
    "Recursion can be used to reverse "
    "numbers and strings."
)

print(
    "A power of 5 can be checked by "
    "repeatedly dividing the number by 5."
)

print(
    "Every recursive function needs "
    "a stopping condition."
)

print("================================")
