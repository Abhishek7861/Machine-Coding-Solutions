from GameBoard import GameBoard
from Utility import *


def start():
    gameBoard = GameBoard(4, 2048)
    gameBoard.initialize()
    gameBoard.printBoard()

    while True:
        choice = input()
        if choice == "0":
            gameBoard.board, done = left(gameBoard.board)
            gameBoard.addRandomTile()
            gameBoard.printBoard()
        if choice == "1":
            gameBoard.board, done = right(gameBoard.board)
            gameBoard.addRandomTile()
            gameBoard.printBoard()
        if choice == "2":
            gameBoard.board, done = up(gameBoard.board)
            gameBoard.addRandomTile()
            gameBoard.printBoard()
        if choice == "3":
            gameBoard.board, done = down(gameBoard.board)
            gameBoard.addRandomTile()
            gameBoard.printBoard()
        if gameBoard.checkGameOver():
            print("Game Over")
            return
        if gameBoard.checkGameWon():
            print("Game Won")
            return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
