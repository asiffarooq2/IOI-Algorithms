# Sudoku solver using backtracking

GRID_SIZE = 9
SUBGRID_SIZE = 3


# Display the Sudoku grid
def display_grid(sudoku_grid):

    for row in range(GRID_SIZE):

        for column in range(GRID_SIZE):
            print(sudoku_grid[row][column], end=" ")

        print()


# Check whether a number can safely be placed
# in the given position
def is_safe(sudoku_grid, row, column, number):

    # Check the current row
    for current_column in range(GRID_SIZE):

        if sudoku_grid[row][current_column] == number:
            return False

    # Check the current column
    for current_row in range(GRID_SIZE):

        if sudoku_grid[current_row][column] == number:
            return False

    # Find the starting position of the 3x3 subgrid
    start_row = row - row % SUBGRID_SIZE
    start_column = column - column % SUBGRID_SIZE

    # Check the 3x3 subgrid
    for current_row in range(SUBGRID_SIZE):

        for current_column in range(SUBGRID_SIZE):

            if (
                sudoku_grid[
                    current_row + start_row
                ][
                    current_column + start_column
                ] == number
            ):
                return False

    return True


# Solve the Sudoku using backtracking
def solve_sudoku(sudoku_grid, row, column):

    # If we have reached the end of the grid,
    # the Sudoku is solved
    if row == GRID_SIZE - 1 and column == GRID_SIZE:
        return True

    # Move to the next row
    if column == GRID_SIZE:
        row += 1
        column = 0

    # If the current cell is already filled,
    # move to the next cell
    if sudoku_grid[row][column] > 0:
        return solve_sudoku(
            sudoku_grid,
            row,
            column + 1
        )

    # Try numbers from 1 to 9
    for number in range(1, GRID_SIZE + 1):

        # Check whether the number is safe
        if is_safe(
            sudoku_grid,
            row,
            column,
            number
        ):

            # Place the number
            sudoku_grid[row][column] = number

            # Recursively solve the remaining cells
            if solve_sudoku(
                sudoku_grid,
                row,
                column + 1
            ):
                return True

            # Backtrack and remove the number
            sudoku_grid[row][column] = 0

    return False


# Sudoku puzzle
sudoku_grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]


# Solve and display the Sudoku
if solve_sudoku(sudoku_grid, 0, 0):
    display_grid(sudoku_grid)
else:
    print("No solution exists.")
