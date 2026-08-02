# ================================
# RECURSION CHALLENGE LAB
# ================================
# Topics:
# Recursive Thinking
# Tower of Hanoi
# Mobile Keypad
# Recursion Tree
# Problem Growth

print("================================")
print("RECURSION CHALLENGE LAB")
print("================================")


# ------------------------------------------------
# PART 1 - RECURSIVE THINKING
# ------------------------------------------------

print("\nPART 1: Recursive Thinking")

print(
    "Recursion solves a large problem by "
    "breaking it into smaller problems."
)

print(
    "Every recursive function needs "
    "a base case to stop."
)


# ------------------------------------------------
# PART 2 - TOWER OF HANOI
# ------------------------------------------------

def move_disks(disks, start, middle, end):

    # Base Case
    if disks == 1:

        print(
            "Move disk 1 from",
            start,
            "to",
            end
        )

        return

    # Move smaller disks to middle rod
    move_disks(
        disks - 1,
        start,
        end,
        middle
    )

    # Move largest disk
    print(
        "Move disk",
        disks,
        "from",
        start,
        "to",
        end
    )

    # Move smaller disks to destination
    move_disks(
        disks - 1,
        middle,
        start,
        end
    )


print("\nPART 2: Tower of Hanoi")

move_disks(
    4,
    "Left",
    "Middle",
    "Right"
)


# ------------------------------------------------
# PART 3 - MOBILE KEYPAD
# ------------------------------------------------

mobile_keypad = {
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"]
}


# ------------------------------------------------
# PART 4 - GENERATE KEYPAD WORDS
# ------------------------------------------------

def create_words(digits, current):

    # Base Case
    if len(digits) == 0:

        print(current)
        return

    # First digit
    first = digits[0]

    # Remaining digits
    remaining = digits[1:]

    # Try every possible letter
    for letter in mobile_keypad[first]:

        create_words(
            remaining,
            current + letter
        )


print("\nPART 4: Keypad Combinations")

number = "56"

print("Digits:", number)

print("Possible combinations:")

create_words(
    number,
    ""
)


# ------------------------------------------------
# PART 5 - SHOW RECURSION TREE
# ------------------------------------------------

def display_tree(digits, current, level):

    indent = "  " * level

    # Base Case
    if len(digits) == 0:

        print(
            indent
            + "Completed: "
            + current
        )

        return

    first = digits[0]

    remaining = digits[1:]

    print(
        indent
        + "Current: "
        + current
        + " | Next Digit: "
        + first
    )

    for letter in mobile_keypad[first]:

        display_tree(
            remaining,
            current + letter,
            level + 1
        )


print("\nPART 5: Recursion Tree")

display_tree(
    "56",
    "",
    0
)


# ------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------

print("\n================================")
print("RECURSION CHALLENGE SUMMARY")
print("================================")

print(
    "Recursion breaks a problem "
    "into smaller versions of itself."
)

print(
    "Tower of Hanoi recursively "
    "moves smaller groups of disks."
)

print(
    "Keypad recursion creates combinations "
    "one letter at a time."
)

print(
    "The recursion tree shows how "
    "each function call creates branches."
)

print(
    "Increasing the input size creates "
    "more recursive calls."
)

print("================================")
