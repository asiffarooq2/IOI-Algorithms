
# Recursive solution to the Coin Change Problem

def count_coin_combinations(coin_denominations, total_coins, target_sum):

    # If the target sum is zero, one valid combination exists
    if target_sum == 0:
        return 1

    # If the target sum becomes negative, no solution exists
    if target_sum < 0:
        return 0

    # If no coins remain and the target is positive, no solution exists
    if total_coins <= 0:
        return 0

    # Count combinations by:
    # 1. Excluding the current coin
    # 2. Including the current coin
    return (
        count_coin_combinations(
            coin_denominations, total_coins - 1, target_sum
        )
        +
        count_coin_combinations(
            coin_denominations,
            total_coins,
            target_sum - coin_denominations[total_coins - 1]
        )
    )


# Main program
coin_denominations = [1, 2, 3]
total_coins = len(coin_denominations)
target_sum = 4

combination_count = count_coin_combinations(
    coin_denominations, total_coins, target_sum
)

print("Number of ways to make the target sum:", combination_count)
