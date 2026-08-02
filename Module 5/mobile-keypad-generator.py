# ================================
# MOBILE KEYPAD GENERATOR
# File: mobile-keypad-generator.py
# ================================


# PART 1 - KEYPAD MAPPING

mobile_keys = {
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"]
}


# PART 2 - RECURSIVE FUNCTION

def generate_words(digits, word):

    # Base Case
    if len(digits) == 0:

        print(word)
        return

    # Get first digit
    first = digits[0]

    # Get remaining digits
    remaining_digits = digits[1:]

    # PART 3 - TRY EVERY LETTER

    for letter in mobile_keys[first]:

        generate_words(
            remaining_digits,
            word + letter
        )


# PART 4 - TAKE USER INPUT

number = input(
    "Enter keypad digits (example 34): "
)

print("\nPossible Letter Combinations:")

generate_words(
    number,
    ""
)


# PART 5 - COUNT TOTAL COMBINATIONS

total = 1

for digit in number:

    total = (
        total
        * len(mobile_keys[digit])
    )


print(
    "\nTotal Number of Combinations:",
    total
)
