# N-Queens problem:
# Find the total number of solutions
# and display one valid solution.


def display_board(chess_board):
    """Display the chess board."""

    for board_row in chess_board:
        print(" ".join(board_row))


def solve_n_queens(board_size):

    # Create an empty chess board
    chess_board = [
        ["." for _ in range(board_size)]
        for _ in range(board_size)
    ]

    # Keep track of occupied columns
    occupied_columns = set()

    # Keep track of occupied diagonals
    # Main diagonal: row - column
    occupied_diagonal_1 = set()

    # Other diagonal: row + column
    occupied_diagonal_2 = set()

    # Store all valid solutions
    all_solutions = []

    def backtrack(current_row):

        # All queens have been placed
        if current_row == board_size:

            all_solutions.append(
                [row[:] for row in chess_board]
            )

            return

        # Try placing a queen in every column
        for current_column in range(board_size):

            # Check whether the position is safe
            if (
                current_column in occupied_columns
                or (current_row - current_column)
                in occupied_diagonal_1
                or (current_row + current_column)
                in occupied_diagonal_2
            ):
                continue

            # Place the queen
            chess_board[current_row][current_column] = "Q"

            # Mark the column and diagonals as occupied
            occupied_columns.add(current_column)
            occupied_diagonal_1.add(
                current_row - current_column
            )
            occupied_diagonal_2.add(
                current_row + current_column
            )

            # Move to the next row
            backtrack(current_row + 1)

            # Backtrack: remove the queen
            chess_board[current_row][current_column] = "."

            occupied_columns.remove(current_column)
            occupied_diagonal_1.remove(
                current_row - current_column
            )
            occupied_diagonal_2.remove(
                current_row + current_column
            )

    # Start placing queens from the first row
    backtrack(0)

    return all_solutions


# Driver code
board_size = 4

solutions = solve_n_queens(board_size)

print("Total solutions:", len(solutions))

print(
    f"Out of {len(solutions)} solutions, "
    "one solution is:"
)

display_board(solutions[0])
