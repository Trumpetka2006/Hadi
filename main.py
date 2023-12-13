import random as rd
import os

class Game():
    gameboard = []
    def __init__(self):
        for i in range(100):
            self.gameboard.append('[ ]')
    def drawboard(self):
        for i in range(10):
            for x in range(10):
                print(self.gameboard[x + (10 * i)], end="")
            print()
    def update(self):
        pass
    pass

class Snake():
    linkA = 0
    linkB = 0
    def __init__(self):
        self.linkA = rd.randint(0,98)
        self.linkB = rd.randint(0,self.linkA)
        


        Game.gameboard[self.linkA] = '[@]'
        Game.gameboard[self.linkB] = '[o]'
    def interact(self, possition):
        if possition == self.linkA:
            print("snake")

    def update(self):
        Game.gameboard[self.linkA] = '[@]'
        Game.gameboard[self.linkB] = '[o]'

class Ladder():
    linkA = 0
    linkB = 0
    def __init__(self):
        self.linkA = rd.randint(5,98)
        self.linkB = rd.randint(self.linkA,97)
        


        Game.gameboard[self.linkA] = '[#]'
        Game.gameboard[self.linkB] = '[_]'
    def interact(self, possition):
        if possition == self.linkA:
            print("snake")

    def update(self):
        Game.gameboard[self.linkA] = '[#]'
        Game.gameboard[self.linkB] = '[_]'

class Player():
    playerPos = 0
    oldPos = 0
    id = 0
    def __init__(self, ID):
        self.id = ID
        Game.gameboard[0] += '[' + str(ID) + ']'
    def roll(self):
        pass
        

numberofsnakes = 5
numberofladders = 5
numberofplayers = 1

Snakes = []
Ladders = []
Players = []

GameON = True

print("LOADING...")
GameHandler = Game()


for snake in range(numberofsnakes):
    Snakes.append(Snake())

for ladder in range(numberofladders):
    Ladders.append(Ladder())

for player in range(numberofplayers):
    Players.append(Player(player))

os.system('clear')

GameHandler.drawboard()

while GameON:
    GameON = False





