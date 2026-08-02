# ==========================================
# RECURSION PATTERNS DEMO
# Topics:
# Linear Recursion
# Tail Recursion
# Head Recursion
# Increasing-Decreasing Recursion
# Tree Recursion
# ==========================================


# ------------------------------------------
# PART 1: Linear Recursion
# One recursive call at each level
# ------------------------------------------

def linear_count(n):

    if n == 0:
        return

    print(n, end=" ")

    linear_count(n - 1)


print("Linear Recursion:")

linear_count(6)

print("\n")


# ------------------------------------------
# PART 2: Tail Recursion
# Work happens before recursive call
# Recursive call is the last operation
# ------------------------------------------

def tail_count(n):

    if n == 0:
        return

    print(n, end=" ")

    tail_count(n - 1)


print("Tail Recursion:")

tail_count(7)

print("\n")


# ------------------------------------------
# PART 3: Head Recursion
# Recursive call happens first
# Printing happens while returning
# ------------------------------------------

def head_count(n):

    if n == 0:
        return

    head_count(n - 1)

    print(n, end=" ")


print("Head Recursion:")

head_count(6)

print("\n")


# ------------------------------------------
# PART 4: Increasing-Decreasing Recursion
# Work happens before AND after recursive call
# ------------------------------------------

def up_down(n):

    if n == 0:
        return

    # Going down
    print(n, end=" ")

    up_down(n - 1)

    # Coming back up
    print(n, end=" ")


print("Increasing-Decreasing Recursion:")

up_down(5)

print("\n")


# ------------------------------------------
# PART 5: Tree Recursion
# Each function makes TWO recursive calls
# ------------------------------------------

def tree_pattern(n):

    if n == 0:
        return

    print(n, end=" ")

    # First branch
    tree_pattern(n - 1)

    # Second branch
    tree_pattern(n - 1)


print("Tree Recursion:")

tree_pattern(4)

print("\n")

print("Tree recursion creates multiple branches.")
print("Number of calls increases quickly at each level.")
