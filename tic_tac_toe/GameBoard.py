class GameBoard:
    def __init__(self, size):
        self.board = None
        self.size = size

    def initializeBoard(self):
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append("-")
            board.append(row)
        self.board = board

    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end=' ')
            print()

    def playGame(self, row, col, symbol):
        if self.board[row][col] == "-":
            self.board[row][col] = symbol
            return True
        else:
            print("Invalid Move")
            return False

    def checkWinner(self, row, col, symbol):
        winString = symbol * self.size
        rowString = ""
        colString = ""
        diagonalString = ""
        reverseDiagonalString = ""
        for i in range(self.size):
            rowString = rowString + self.board[row][i]
            colString = colString + self.board[i][col]
            if row == col:
                diagonalString = diagonalString + self.board[i][i]
            if row + col == self.size:
                print(i, self.size - i)
                reverseDiagonalString = reverseDiagonalString + self.board[i][self.size-1 - i]

        if winString == reverseDiagonalString or winString == diagonalString or winString == colString or winString == rowString:
            return True
        else:
            return False
