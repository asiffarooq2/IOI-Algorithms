# ==========================================
# RECURSION PATHS AND BRACKETS
# ==========================================
# Topics:
# Stair Climbing
# Recursive Calls
# Tracing Recursion
# Balanced Brackets
# ==========================================

print("================================")
print("RECURSION PATHS AND BRACKETS")
print("================================")


# ------------------------------------------
# PART 1 - STAIR CLIMBING PROBLEM
# ------------------------------------------

print("\nPART 1: Stair Climbing Problem")

print("You can climb either 1 or 2 steps.")
print("Find the total ways to reach the top.")


# ------------------------------------------
# PART 2 - SOLVE STAIR CLIMB
# ------------------------------------------

def count_paths(n):

    # Base Case 1
    if n == 0:
        return 1

    # Base Case 2
    if n < 0:
        return 0

    # Recursive Case
    return count_paths(n - 1) + count_paths(n - 2)


stairs = 6

print("\nPART 2: Stair Climb Result")
print("Number of stairs:", stairs)
print("Total climbing paths:", count_paths(stairs))


# ------------------------------------------
# PART 3 - TRACE RECURSIVE CALLS
# ------------------------------------------

def trace_paths(n, space=""):

    print(
        space + "count_paths(" + str(n) + ")"
    )

    if n == 0:

        print(
            space + "Reached the top -> return 1"
        )

        return 1

    if n < 0:

        print(
            space + "Passed the top -> return 0"
        )

        return 0

    # Take one step
    one_step = trace_paths(
        n - 1,
        space + "  "
    )

    # Take two steps
    two_steps = trace_paths(
        n - 2,
        space + "  "
    )

    total = one_step + two_steps

    print(
        space
        + "Total paths for "
        + str(n)
        + " stairs = "
        + str(total)
    )

    return total


print("\nPART 3: Tracing Recursive Calls")

trace_paths(4)


# ------------------------------------------
# PART 4 - BALANCED BRACKETS PROBLEM
# ------------------------------------------

print("\nPART 4: Balanced Brackets Problem")

print(
    "Generate valid combinations "
    "of square brackets []."
)


# ------------------------------------------
# PART 5 - GENERATE BALANCED BRACKETS
# ------------------------------------------

def generate_brackets(
    current,
    open_count,
    close_count,
    total_pairs
):

    # Base Case
    if len(current) == total_pairs * 2:

        print(current)

        return

    # Add opening bracket
    if open_count < total_pairs:

        generate_brackets(
            current + "[",
            open_count + 1,
            close_count,
            total_pairs
        )

    # Add closing bracket
    if close_count < open_count:

        generate_brackets(
            current + "]",
            open_count,
            close_count + 1,
            total_pairs
        )


pairs = 2

print("\nPART 5: Balanced Bracket Combinations")
print("Number of pairs:", pairs)

generate_brackets(
    "",
    0,
    0,
    pairs
)


# ------------------------------------------
# FINAL SUMMARY
# ------------------------------------------

print("\n================================")
print("RECURSION LAB SUMMARY")
print("================================")

print(
    "Stair climbing uses 1-step "
    "and 2-step recursive choices."
)

print(
    "The call trace shows how recursion "
    "breaks a problem into smaller problems."
)

print(
    "Balanced brackets keep track of "
    "opening and closing brackets."
)

print(
    "A closing bracket is only added "
    "when the sequence remains balanced."
)

print("================================")
