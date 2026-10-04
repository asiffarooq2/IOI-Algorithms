# Sudoku solver using backtracking


GRID_SIZE = 9
SUBGRID_SIZE = 3


# Display the Sudoku grid
def display_grid(sudoku_grid):

    for row in range(GRID_SIZE):

        for column in range(GRID_SIZE):
            print(sudoku_grid[row][column], end=" ")

        print()


# Find an empty cell in the Sudoku grid
def find_empty_cell(sudoku_grid, empty_position):

    for row in range(GRID_SIZE):

        for column in range(GRID_SIZE):

            if sudoku_grid[row][column] == 0:

                empty_position[0] = row
                empty_position[1] = column

                return True

    return False


# Check whether a number already exists in the row
def is_number_in_row(sudoku_grid, row, number):

    for column in range(GRID_SIZE):

        if sudoku_grid[row][column] == number:
            return True

    return False


# Check whether a number already exists in the column
def is_number_in_column(sudoku_grid, column, number):

    for row in range(GRID_SIZE):

        if sudoku_grid[row][column] == number:
            return True

    return False


# Check whether a number already exists in the 3x3 subgrid
def is_number_in_subgrid(
    sudoku_grid,
    start_row,
    start_column,
    number
):

    for row in range(SUBGRID_SIZE):

        for column in range(SUBGRID_SIZE):

            if (
                sudoku_grid[
                    row + start_row
                ][
                    column + start_column
                ] == number
            ):
                return True

    return False


# Check whether a number can safely be placed
def is_safe_location(
    sudoku_grid,
    row,
    column,
    number
):

    subgrid_start_row = row - row % SUBGRID_SIZE
    subgrid_start_column = column - column % SUBGRID_SIZE

    return (
        not is_number_in_row(
            sudoku_grid,
            row,
            number
        )
        and
        not is_number_in_column(
            sudoku_grid,
            column,
            number
        )
        and
        not is_number_in_subgrid(
            sudoku_grid,
            subgrid_start_row,
            subgrid_start_column,
            number
        )
    )


# Solve the Sudoku using backtracking
def solve_sudoku(sudoku_grid):

    # Store the position of an empty cell
    empty_position = [0, 0]

    # If there are no empty cells, the Sudoku is solved
    if not find_empty_cell(
        sudoku_grid,
        empty_position
    ):
        return True

    row = empty_position[0]
    column = empty_position[1]

    # Try numbers from 1 to 9
    for number in range(1, GRID_SIZE + 1):

        # Check whether the number can be placed safely
        if is_safe_location(
            sudoku_grid,
            row,
            column,
            number
        ):

            # Place the number
            sudoku_grid[row][column] = number

            # Recursively solve the remaining puzzle
            if solve_sudoku(sudoku_grid):
                return True

            # Backtrack
            sudoku_grid[row][column] = 0

    return False


# Driver code
if __name__ == "__main__":

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
    if solve_sudoku(sudoku_grid):
        display_grid(sudoku_grid)
    else:
        print("No solution exists")
