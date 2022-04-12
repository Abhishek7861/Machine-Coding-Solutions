from GameBoard import GameBoard
from Player import Player


def playGame():
    count = 0
    while count != size * size:
        player = players.pop(0)
        retval = False

        while not retval:
            temp = input().split()
            if temp[0] == "exit":
                print("Game Over")
                return
            retval = gameBoard.playGame(int(temp[0]) - 1, int(temp[1]) - 1, player.symbol)

        gameBoard.printBoard()
        if gameBoard.checkWinner(int(temp[0]) - 1, int(temp[1]) - 1, player.symbol):
            print(player.name + " won the game")
            return
        players.append(player)

    print("Game Over")


players = []
size = 3

temp = input().split()
player = Player(temp[0], temp[1])
players.append(player)
temp = input().split()
player = Player(temp[0], temp[1])
players.append(player)

gameBoard = GameBoard(size)
gameBoard.initializeBoard()
gameBoard.printBoard()
playGame()

