# ==========================================
# REVERSE RECURSION LAB
# Topics:
# Digit Extraction
# Reverse Number
# Reverse String
# Power of 3
# ==========================================

print("=== Reverse Recursion Lab ===")
print()


# PART 1 - DIGIT EXTRACTOR

number = int(input("Enter a number: "))

temp = number

while temp > 0:

    last_digit = temp % 10
    remaining = temp // 10

    print(
        "Last Digit:",
        last_digit,
        " Remaining:",
        remaining
    )

    temp = temp // 10

print()


# PART 2 - REVERSE A NUMBER USING RECURSION

def reverse_number(num):

    # Base case
    if num // 10 == 0:
        return num

    # Get last digit
    last = num % 10

    # Reverse remaining number
    rest = reverse_number(num // 10)

    # Join digits in reverse order
    return last * pow(
        10,
        len(str(rest))
    ) + rest


num2 = int(
    input("Enter a number to reverse: ")
)

print(
    num2,
    "reversed ->",
    reverse_number(num2)
)

print()


# PART 3 - REVERSE A WORD

def reverse_word(word):

    # Base case
    if len(word) <= 1:
        return word

    # Recursive call
    return (
        reverse_word(word[1:])
        + word[0]
    )


word = input("Enter a word: ")

print(
    word,
    "->",
    reverse_word(word)
)

print()


# PART 4 - CHECK POWER OF 3

def is_power_of_3(n):

    # Invalid number
    if n <= 0:
        return False

    # Base case
    if n == 1:
        return True

    # Recursive case
    if n % 3 == 0:
        return is_power_of_3(n // 3)

    return False


# Test values
print(
    "27 ->",
    is_power_of_3(27)
)

print(
    "20 ->",
    is_power_of_3(20)
)


# User test
guess = int(
    input("Test your own number: ")
)

print(
    guess,
    "-> Power of 3?",
    is_power_of_3(guess)
)
