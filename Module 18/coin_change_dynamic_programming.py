
# Dynamic Programming: Minimum Coin Change Problem

def find_minimum_coins(coin_denominations, target_amount):

    # Store the minimum coins required for each amount
    minimum_coins = [float('inf')] * (target_amount + 1)

    # Base case: zero coins are needed to make amount zero
    minimum_coins[0] = 0

    # Calculate the minimum coins for each amount
    for current_amount in range(1, target_amount + 1):

        # Try every available coin denomination
        for coin_value in coin_denominations:

            if coin_value <= current_amount:
                minimum_coins[current_amount] = min(
                    minimum_coins[current_amount],
                    1 + minimum_coins[current_amount - coin_value]
                )

    # Return -1 if the target amount cannot be formed
    if minimum_coins[target_amount] == float('inf'):
        return -1

    return minimum_coins[target_amount]


# Example usage
coin_denominations = [1, 2, 5]
target_amount = 11

minimum_coin_count = find_minimum_coins(
    coin_denominations, target_amount
)

print(f"The minimum number of coins needed: {minimum_coin_count}")
