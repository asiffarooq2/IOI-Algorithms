# ==============================================
# ACTIVITY - STAIRCASE PATH COUNTER
# ==============================================
# Count the number of different ways to climb
# a staircase when you can take:
#
# 1 step at a time
# OR
# 3 steps at a time
# ==============================================


def count_ways(stairs):

    # Base Case 1:
    # We went beyond the staircase
    if stairs < 0:
        return 0

    # Base Case 2:
    # We reached the top successfully
    if stairs == 0:
        return 1

    # Count paths using a 3-step jump
    three_steps = 0

    if stairs >= 3:
        three_steps = count_ways(stairs - 3)

    # Count paths using a 1-step move
    one_step = count_ways(stairs - 1)

    # Total number of possible paths
    return three_steps + one_step


# Ask user for number of stairs
stairs = int(
    input("Enter number of stairs: ")
)


# Display result
print(
    "Number of ways to climb:",
    count_ways(stairs)
)
