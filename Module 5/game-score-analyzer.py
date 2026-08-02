# ================================================
# ACTIVITY - GAME SCORE ANALYZER
# File: game-score-analyzer.py
# ================================================


# PART 1 - HEAD-TAIL PATTERN

scores = [450, 180, 320, 95, 500, 240, 130]

print("=== PART 1: HEAD-TAIL PATTERN ===")

print("Full Score List :", scores)
print("Head            :", scores[0])
print("Tail            :", scores[1:])
print("Head of Tail    :", scores[1:][0])
print("Tail of Tail    :", scores[1:][1:])


# PART 2 - BASE CASE FOR LISTS

def show_list_shrink(a, depth=0):

    indent = "  " * depth

    print(
        f"{indent}List: {a} -> Length = {len(a)}"
    )

    # Base case
    if len(a) == 1:

        print(
            f"{indent}Base Case! "
            f"Only one score remains: {a[0]}"
        )

        return

    # Recursive call
    show_list_shrink(a[1:], depth + 1)


print("\n=== PART 2: BASE CASE ===")

show_list_shrink([500, 320, 240, 130])


# PART 3 - CHECK IF LIST IS SORTED

def check_sorted(a):

    # Base case
    if len(a) <= 1:
        return True

    # Compare first two elements
    return (
        a[0] <= a[1]
        and check_sorted(a[1:])
    )


print("\n=== PART 3: SORTED CHECK ===")

print("Scores:", scores)

print(
    "Is Scores List Sorted?",
    check_sorted(scores)
)


sorted_scores = [
    95,
    130,
    180,
    240,
    320,
    450,
    500
]

print("Sorted Scores:", sorted_scores)

print(
    "Is Sorted List Correct?",
    check_sorted(sorted_scores)
)


# PART 4 - SUM OF LIST USING RECURSION

def calculate_total(a):

    # Base case
    if len(a) == 1:
        return a[0]

    # Head + sum of tail
    return (
        a[0]
        + calculate_total(a[1:])
    )


print("\n=== PART 4: TOTAL SCORE ===")

print("Scores:", scores)

print(
    "Total Score:",
    calculate_total(scores)
)


# PART 5 - FIND LARGEST SCORE

def find_highest(a):

    # Base case
    if len(a) == 1:
        return a[0]

    # Compare head with largest
    # value from the tail
    return max(
        a[0],
        find_highest(a[1:])
    )


print("\n=== PART 5: HIGHEST SCORE ===")

print("Scores:", scores)

highest = find_highest(scores)

print("Highest Score:", highest)

print(
    "Winning Player:",
    scores.index(highest) + 1
)
