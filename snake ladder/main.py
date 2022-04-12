from Player import Player
from GameBoard import GameBoard


def start():
    ladders = {}
    snakes = {}
    players = []

    numberOfSnakes = int(input())
    for i in range(numberOfSnakes):
        temp = list(map(int, input().split()))
        snakes[temp[0]] = temp[1]

    numberOfLadders = int(input())
    for i in range(numberOfLadders):
        temp = list(map(int, input().split()))
        ladders[temp[0]] = temp[1]

    numberOfPlayers = int(input())
    for i in range(numberOfPlayers):
        name = input()
        player = Player(i, name)
        players.append(player)

    gameBoard = GameBoard(players, snakes, ladders)
    gameBoard.setUp()
    winner = gameBoard.startGame()
    print(winner.getPlayerName())


start()
