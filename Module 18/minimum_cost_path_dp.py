
# Dynamic Programming: Minimum Cost Path

def find_minimum_cost_path(cost_grid, target_row, target_col):

    # Get the number of rows and columns
    total_rows = len(cost_grid)
    total_columns = len(cost_grid[0])

    # Create a table to store minimum costs
    minimum_cost = [
        [0 for column in range(total_columns)]
        for row in range(total_rows)
    ]

    # Initialize the starting cell
    minimum_cost[0][0] = cost_grid[0][0]

    # Calculate minimum costs for the first column
    for row in range(1, target_row + 1):
        minimum_cost[row][0] = (
            minimum_cost[row - 1][0] + cost_grid[row][0]
        )

    # Calculate minimum costs for the first row
    for column in range(1, target_col + 1):
        minimum_cost[0][column] = (
            minimum_cost[0][column - 1] + cost_grid[0][column]
        )

    # Calculate minimum costs for the remaining cells
    for row in range(1, target_row + 1):
        for column in range(1, target_col + 1):

            minimum_cost[row][column] = (
                min(
                    minimum_cost[row - 1][column - 1],
                    minimum_cost[row - 1][column],
                    minimum_cost[row][column - 1]
                )
                + cost_grid[row][column]
            )

    # Return the minimum cost to reach the destination
    return minimum_cost[target_row][target_col]


# Main program
if __name__ == "__main__":
    cost_grid = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]
    ]

    destination_row = 2
    destination_column = 2

    minimum_cost = find_minimum_cost_path(
        cost_grid, destination_row, destination_column
    )

    print("Minimum cost path:", minimum_cost)
