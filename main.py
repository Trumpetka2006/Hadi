import random as rd
import os
import time

class Game():
    gameboard = []
    def __init__(self):
        for i in range(100):
            self.gameboard.append('[ ]')
    def drawboard(self):
        for i in range(10):
            for x in range(10):
                print(self.gameboard[(x + (10 * i))], end="")
            print()
            time.sleep(0.05)
    def update(self):
        pass
    pass


class Snake():
    linkA = 0
    linkB = 0
    def __init__(self):
        self.linkA = rd.randint(0,98)
        self.linkB = rd.randint(0,self.linkA + 1)
        


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
        self.linkB = rd.randint(self.linkA - 1,97)
        


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
        Game.gameboard[0] = '[' + str(ID) + ']'
    def roll(self):
        self.oldPos = self.playerPos
        roll = rd.randint(1,6)
        if roll == 6:
            roll += rd.randint(1,6)
        self.playerPos += roll
        Game.gameboard[self.playerPos] = '[' + str(self.id) + ']'
        Game.gameboard[self.oldPos] = '[ ]'
        pass
        

numberofsnakes = 5
numberofladders = 5
numberofplayers = 3

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

Players[0].roll()
Players[1].roll()
GameHandler.drawboard()

#print(len(GameHandler.gameboard))
#print(GameHandler.gameboard)

for i in range(10):
    input()
    os.system("clear")
    Players[0].roll()
    GameHandler.drawboard()





