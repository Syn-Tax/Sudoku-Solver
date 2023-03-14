class Sudoku:
    def __init__(self):
        # sample starting board from wikipedia - https://www.wikiwand.com/en/Sudoku
        self.board = [
                [5,3,0, 0,7,0, 0,0,0],
                [6,0,0, 1,9,5, 0,0,0],
                [0,9,8, 0,0,0, 0,6,0],

                [8,0,0, 0,6,0, 0,0,3],
                [4,0,0, 8,0,3, 0,0,1],
                [7,0,0, 0,2,0, 0,0,6],
                
                [0,6,0, 0,0,0, 2,8,0],
                [0,0,0, 4,1,9, 0,0,5],
                [0,0,0, 0,8,0, 0,7,9]
                ]

    def is_legal(self):
        # check rows
        for row in self.board:
            # filter empty spaces
            r = list(filter(lambda x: (x!=0), row))
            # check for duplicates
            if len(r) != len(set(r)):
                return False

        # check columns
        cols = [[row[i] for i in range(len(self.board[0]))] for row in self.board]

        for col in cols:
            # filter empty spaces
            c = list(filter(lambda x: (x!=0), col))
            # check for duplicates
            if len(c) != len(set(c)):
                return False

        # check boxes
        for i in range(3):
            for j in range(3):
                box = []
                for k in range(3):
                    for l in range(3):
                        box.append(self.board[i*3+k][j*3+l])

                b = list(filter(lambda x: (x!=0), box))
                if len(b) != len(set(b)):
                    return False

        return True

    def is_goal(self):
        # search for 0's
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    return False

        return self.is_legal()

    def move(self, row, col, val):
        if self.board[row][col] != 0 or val > 9 or val < 0:
            return False

        self.board[row][col] = val
        return self.is_legal()

    def display(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == 0:
                    print("  ", end="")
                else:
                    print(f"{self.board[row][col]} ", end="")

                if col % 3 == 2 and col != 8:
                    print("| ", end="")

            print()
            if row % 3 == 2 and row != 8:
                print("-"*22)

