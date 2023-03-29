import numpy as np

# sample starting board from wikipedia - https://www.wikiwand.com/en/Sudoku
sample_board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])


def is_legal(board):
    # check rows
    for row in board:
        if sum(row) != sum(set(row)):
            return False

    # check columns
    cols = np.array(list(zip(*board)))

    for col in cols:
        if sum(col) != sum(set(col)):
            return False

    # check boxes
    for i in range(3):
        for j in range(3):
            box = []
            for k in range(3):
                for l in range(3):
                    box.append(board[i*3+k][j*3+l])
            if sum(box) != sum(set(box)):
                return False

    return True


def is_goal(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                return False

    return is_legal(board)


def display(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                print("  ", end="")
            else:
                print(f"{board[row][col]} ", end="")

            if col % 3 == 2 and col != 8:
                print("| ", end="")

        print()
        if row % 3 == 2 and row != 8:
            print("-"*22)


def move(board, row, col, val):
    temp = np.copy(board)
    temp[row][col] = val
    return temp
