import sudoku
import solver

import time
import numpy as np

solution = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],

    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],

    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])


simple = np.array([
    [5, 0, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 0, 2, 5, 6, 7],

    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 0, 5, 3, 7, 9, 0],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],

    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 0, 5, 2, 8, 6, 1, 0, 9]
])


def main():
    # board = sudoku.sample_board
    board = simple

    print("\nINITIAL STATE:")
    sudoku.display(board)

    print("\n\nDEPTH FIRST SEARCH:")
    constrained_start = time.time()
    result = solver.depth_first_search(board)
    print(f"TIME: {round(time.time() - constrained_start, 3)} seconds")

    print("\nBREADTH FIRST SEARCH:")
    normal_start = time.time()
    result = solver.breadth_first_search(board)
    print(f"TIME: {round(time.time() - normal_start, 3)} seconds")

    print("\nITERATIVE DEEPENING DFS:")
    normal_start = time.time()
    result = solver.iterative_dfs(board)
    print(f"TIME: {round(time.time() - normal_start, 3)} seconds")

    print("\nCONSTRAINED DFS:")
    normal_start = time.time()
    result = solver.constrained_dfs(board)
    print(f"TIME: {round(time.time() - normal_start, 3)} seconds")

    print("\nCONSTRAINED BFS:")
    normal_start = time.time()
    result = solver.constrained_bfs(board)
    print(f"TIME: {round(time.time() - normal_start, 3)} seconds")


if __name__ == "__main__":
    main()
