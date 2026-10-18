maze_size = 4

def is_valid_move(maze_size, maze, row, col, solution):
    if (row >= 0 and col >= 0 and
        row < maze_size and col < maze_size and
        maze[row][col] == 1 and solution[row][col] == 0):
        return True
    return False


def solve_rat_maze(maze_size, maze, row_moves, col_moves,
                   current_row, current_col, solution):

    # Check whether the rat has reached the destination
    if current_row == maze_size - 1 and current_col == maze_size - 1:
        return True

    # Try moving in all four directions
    for direction in range(4):
        next_row = current_row + row_moves[direction]
        next_col = current_col + col_moves[direction]

        # Check whether the next position is valid
        if is_valid_move(maze_size, maze, next_row, next_col, solution):
            solution[next_row][next_col] = 1

            # Recursively explore the next position
            if solve_rat_maze(
                maze_size, maze, row_moves, col_moves,
                next_row, next_col, solution
            ):
                return True

            # Backtrack if the path does not lead to the destination
            solution[next_row][next_col] = 0

    return False


def find_maze_solution(maze):
    maze_size = len(maze)

    solution = [[0 for col in range(maze_size)]
                for row in range(maze_size)]

    solution[0][0] = 1

    # Possible movements: up, down, left, right
    row_moves = [-1, 1, 0, 0]
    col_moves = [0, 0, -1, 1]

    if solve_rat_maze(
        maze_size, maze, row_moves, col_moves, 0, 0, solution
    ):
        print("Solution path:")

        for row in solution:
            for cell in row:
                print(cell, end=" ")
            print()
    else:
        print("Solution does not exist.")


# Main program
if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]

    find_maze_solution(maze)