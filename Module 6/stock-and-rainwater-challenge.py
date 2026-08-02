# ==========================================
# STOCK AND RAINWATER CHALLENGE
# Topics:
# Stock Buy-Sell
# Left Tallest Bars
# Right Tallest Bars
# Rainwater Trapped
# ==========================================


# ------------------------------------------
# PART 1 - STOCK BUY-SELL
# ------------------------------------------

prices = [120, 150, 110, 190, 220, 180, 260]

profit = 0

for i in range(1, len(prices)):

    # Buy when previous price is lower
    # and sell when current price is higher
    if prices[i] > prices[i - 1]:

        profit += (
            prices[i] - prices[i - 1]
        )


print("Stock Prices:", prices)

print(
    "Maximum Profit:",
    profit
)

print()


# ------------------------------------------
# PART 2 - LEFT TALLEST BARS
# ------------------------------------------

heights = [
    2, 0, 1, 3, 0, 2, 1, 4, 1, 2
]

n = len(heights)

left_tallest = [0] * n

# First bar
left_tallest[0] = heights[0]


for i in range(1, n):

    left_tallest[i] = max(
        left_tallest[i - 1],
        heights[i]
    )


print("Bar Heights:   ", heights)

print(
    "Left Tallest:  ",
    left_tallest
)

print()


# ------------------------------------------
# PART 3 - RIGHT TALLEST BARS
# ------------------------------------------

right_tallest = [0] * n

# Last bar
right_tallest[n - 1] = heights[n - 1]


for i in range(
    n - 2,
    -1,
    -1
):

    right_tallest[i] = max(
        right_tallest[i + 1],
        heights[i]
    )


print(
    "Right Tallest: ",
    right_tallest
)

print()


# ------------------------------------------
# PART 4 - RAINWATER TRAPPED
# ------------------------------------------

water = 0


for i in range(n):

    water_at_bar = (
        min(
            left_tallest[i],
            right_tallest[i]
        )
        - heights[i]
    )

    water += water_at_bar


print(
    "Total Water Trapped:",
    water
)
