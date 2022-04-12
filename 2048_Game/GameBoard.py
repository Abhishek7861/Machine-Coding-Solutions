import random


class GameBoard:
    def __init__(self, size, winNumber):
        self.size = size
        self.board = None
        self.winNumber = winNumber
        self.tiles = []

    def initialize(self):
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append("-")
            board.append(row)
        self.board = board
        self.addRandomTile()
        self.addRandomTile()

    def addRandomTile(self):
        while True:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if self.board[row][col] == "-":
                self.board[row][col] = 2
                break
            else:
                continue

    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i][j], end=" ")
            print()
        print()
        print()

    def checkGameOver(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == "-":
                    return False
        return True

    def checkGameWon(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == self.winNumber:
                    return True
        return False
