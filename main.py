import sudoku
import solver

import time
import numpy as np

solution = np.array([
        [5,3,4, 6,7,8, 9,1,2],
        [6,7,2, 1,9,5, 3,4,8],
        [1,9,8, 3,4,2, 5,6,7],

        [8,5,9, 7,6,1, 4,2,3],
        [4,2,6, 8,5,3, 7,9,1],
        [7,1,3, 9,2,4, 8,5,6],

        [9,6,1, 5,3,7, 2,8,4],
        [2,8,7, 4,1,9, 6,3,5],
        [3,4,5, 2,8,6, 1,7,9]
        ])


simple = np.array([
        [5,3,4, 6,0,8, 9,1,2],
        [6,0,2, 1,9,5, 3,4,8],
        [1,0,8, 3,0,2, 5,0,7],

        [8,5,9, 7,0,1, 4,2,3],
        [0,0,6, 8,5,3, 7,0,1],
        [7,1,3, 0,2,4, 8,0,6],

        [9,6,1, 5,0,7, 0,8,0],
        [2,8,7, 4,1,9, 6,0,5],
        [3,0,5, 0,8,6, 1,7,0]
        ])

def main():
    board = sudoku.sample_board
    #board = simple


    constrained_start = time.time()
    result = solver.constrained_dfs(board)
    print(f"CONSTRAINED DFS FINISHED IN: {time.time() - constrained_start}")

    sudoku.display(result)
    print()

    normal_start = time.time()
    result = solver.depth_first_search(board)
    print(f"NORMAL DFS FINISHED IN: {time.time() - normal_start}")

    sudoku.display(result)

if __name__ == "__main__":
    main()
