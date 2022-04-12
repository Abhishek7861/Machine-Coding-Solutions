from Dice import Dice


class GameBoard:
    def __init__(self, players, snakes, ladders):
        self.players = players
        self.snakes = snakes
        self.ladders = ladders
        self.dice = Dice(1)
        self.playerPosition = {}
        self.endPosition = 100

    def setUp(self):
        for player in self.players:
            self.playerPosition[player] = 0

    def startGame(self):
        while True:
            player = self.players.pop(0)
            currentPosition = self.playerPosition.get(player)
            oldPosition = currentPosition

            if currentPosition == 100:
                return player

            diceValue = self.dice.roll_dice()
            currentPosition = currentPosition + diceValue

            if currentPosition in self.ladders:
                currentPosition = self.ladders.get(currentPosition) + currentPosition
            elif currentPosition in self.snakes:
                currentPosition = currentPosition - self.snakes.get(currentPosition)

            if currentPosition <= 100:
                self.playerPosition[player] = currentPosition
                print(player.getPlayerName()+" rolled a "+str(diceValue)+" and moved from "+str(oldPosition)+" to "+str(currentPosition))
            self.players.append(player)
