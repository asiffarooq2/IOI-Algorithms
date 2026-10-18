# Class to store the profit and weight of an item
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


# Greedy algorithm to solve the Fractional Knapsack problem
def fractional_knapsack(capacity, items):

    # Sort items by profit-to-weight ratio in descending order
    items.sort(
        key=lambda item: item.profit / item.weight,
        reverse=True
    )

    # Store the total profit earned
    total_profit = 0.0

    # Select items until the knapsack is full
    for item in items:

        # Add the complete item if it fits
        if item.weight <= capacity:
            capacity -= item.weight
            total_profit += item.profit

        # Add a fraction of the item if it doesn't fit completely
        else:
            total_profit += item.profit * capacity / item.weight
            break

    return total_profit


# Main program
if __name__ == "__main__":
    knapsack_capacity = 50

    items = [
        Item(60, 10),
        Item(100, 20),
        Item(120, 30)
    ]

    maximum_profit = fractional_knapsack(knapsack_capacity, items)

    print("Maximum profit:", maximum_profit)
