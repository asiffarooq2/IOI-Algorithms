# ================================
# PROFIT AND WATER ANALYZER
# ================================
# Topics:
# Stock Buy-Sell
# Profit Accumulation
# Left Tallest Bars
# Right Tallest Bars
# Rainwater Trapped

print("================================")
print("PROFIT AND WATER ANALYZER")
print("================================")


# ------------------------------------------------
# PART 1 - STOCK BUY-SELL
# ------------------------------------------------

prices = [90, 140, 125, 200, 175, 250, 300]

print("\nPART 1: Stock Buy-Sell")
print("Stock Prices:", prices)

profit = 0

for i in range(1, len(prices)):

    if prices[i] > prices[i - 1]:

        gain = prices[i] - prices[i - 1]

        profit = profit + gain

        print(
            "Buy at",
            prices[i - 1],
            "Sell at",
            prices[i],
            "Gain:",
            gain
        )

print("Maximum Profit:", profit)


# ------------------------------------------------
# PART 2 - PROFIT ACCUMULATION
# ------------------------------------------------

print("\nPART 2: Profit Accumulation")

total_profit = 0

for i in range(1, len(prices)):

    price_difference = (
        prices[i] - prices[i - 1]
    )

    if price_difference > 0:

        total_profit = (
            total_profit + price_difference
        )

        print(
            "Added Profit:",
            price_difference
        )

print(
    "Total Accumulated Profit:",
    total_profit
)


# ------------------------------------------------
# PART 3 - LEFT TALLEST BARS
# ------------------------------------------------

heights = [
    3, 0, 2, 0, 4, 1, 2, 0, 3
]

n = len(heights)

left_tallest = [0] * n

left_tallest[0] = heights[0]


for i in range(1, n):

    left_tallest[i] = max(
        left_tallest[i - 1],
        heights[i]
    )


print("\nPART 3: Left Tallest Bars")

print(
    "Heights:      ",
    heights
)

print(
    "Left Tallest: ",
    left_tallest
)


# ------------------------------------------------
# PART 4 - RIGHT TALLEST BARS
# ------------------------------------------------

right_tallest = [0] * n

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


print("\nPART 4: Right Tallest Bars")

print(
    "Heights:       ",
    heights
)

print(
    "Right Tallest: ",
    right_tallest
)


# ------------------------------------------------
# PART 5 - RAINWATER TRAPPED
# ------------------------------------------------

water = 0


for i in range(n):

    smaller_bar = min(
        left_tallest[i],
        right_tallest[i]
    )

    trapped = (
        smaller_bar - heights[i]
    )

    water = water + trapped


print("\nPART 5: Rainwater Trapped")

print(
    "Total Rainwater Trapped:",
    water
)


# ------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------

print("\n================================")
print("PROFIT AND WATER SUMMARY")
print("================================")

print(
    "Stock profit is calculated by adding "
    "every positive price increase."
)

print(
    "Left tallest stores the highest bar "
    "seen from the left."
)

print(
    "Right tallest stores the highest bar "
    "seen from the right."
)

print(
    "Trapped water depends on the smaller "
    "of the left and right tallest bars."
)

print("================================")
