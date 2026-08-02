# ==========================================
# RECURSION NUMBER LAB
# Topics:
# What is Recursion
# Base Case
# Recursive Case
# Counting
# Sum of Numbers
# Stack Overflow
# ==========================================

print("=== Recursion Number Lab ===")
print("Rules of Recursion:")
print("1. Solve a smaller version of the problem.")
print("2. Always include a base case.")
print()


# ------------------------------------------
# PART 1 - Count from 1 to 8
# ------------------------------------------

def count_numbers(n):

    if n > 8:
        return

    print(n, end=" ")

    count_numbers(n + 1)


print("Counting from 1 to 8:")
count_numbers(1)
print("\n")


# ------------------------------------------
# PART 2 - Reverse Countdown
# ------------------------------------------

def reverse_count(n):

    if n == 0:
        print("Finished!")
        return

    print(n, end=" ")

    reverse_count(n - 1)


print("Reverse Countdown:")
reverse_count(6)
print("\n")


# ------------------------------------------
# PART 3 - Sum of Numbers
# Example:
# sum_numbers(5)
# = 5 + 4 + 3 + 2 + 1
# = 15
# ------------------------------------------

def sum_numbers(n):

    if n == 1:
        return 1

    return n + sum_numbers(n - 1)


print("Sum using recursion:")
print("sum_numbers(5) =", sum_numbers(5))
print("sum_numbers(8) =", sum_numbers(8))
print()


# ------------------------------------------
# PART 4 - Demonstrating Stack Overflow
# ------------------------------------------

import sys

print("Python Recursion Limit:", sys.getrecursionlimit())

sys.setrecursionlimit(25)


def infinite_recursion(n):

    print("Call", n)

    infinite_recursion(n + 1)


try:

    infinite_recursion(1)

except RecursionError:

    print("\nRecursionError!")
    print("A recursive function must always have a base case.")


# Restore recursion limit
sys.setrecursionlimit(1000)

print("\nProgram Finished Successfully!")