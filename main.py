import random as rd
import os
import time

kostka1 = [' ―――――――― ',
           '│ ●    ● │',
           '│ ●    ● │',
           '│ ●    ● │',
           ' ―――――――― ']

for piece in kostka1:
    print(piece)

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
            #time.sleep(0.05)
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

    def attack(self, playerPos):
        if self.linkA == playerPos:
            return self.linkB
        pass

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
            print("ladder")
            return self.linkB

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

    def update(self):
        Game.gameboard[self.playerPos] = '[' + str(self.id) + ']'

    def roll(self):
        self.oldPos = self.playerPos
        roll = rd.randint(1,6)
        if roll == 6:
            roll += rd.randint(1,6)
        if (self.playerPos + roll > 99): roll = 0
        self.playerPos += roll

        print(self.playerPos)
        if Game.gameboard[self.playerPos] == '[@]' :
            print("Snake!")
            Game.gameboard[self.oldPos] = '[ ]'
            return "snake"
        elif Game.gameboard[self.playerPos] == '[#]':
            print("Ladder!")
            Game.gameboard[self.oldPos] = '[ ]'
            return "ladder"
        
        
        Game.gameboard[self.playerPos] = '[' + str(self.id) + ']'
        Game.gameboard[self.oldPos] = '[ ]'
        pass

    def move(self, possition):
        Game.gameboard[self.playerPos] = '[ ]'
        self.playerPos = possition
        Game.gameboard[self.playerPos] = '[' + str(self.id) + ']'
        
    



        

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




#print(len(GameHandler.gameboard))
#print(GameHandler.gameboard)
def leaderboard():
    playerIndex = 0
    print("\n")
    print("#"*20)
    for player in Players:
        print(f"Player{playerIndex} \t {player.playerPos}")
        playerIndex += 1
    print("#"*20)

while GameON:
    for onplay in range(numberofplayers):
        input()
        for snake in Snakes:
            snake.update()
        for ladder in Ladders:
            ladder.update()

        os.system("clear")
        field = Players[onplay].roll()
        if field == "snake":
            for snake in Snakes:
                if not snake.attack(Players[onplay].playerPos) == None:
                    print(snake.attack(Players[onplay].playerPos))
                    Players[onplay].move(snake.attack(Players[onplay].playerPos))
                
            print("attack")
        elif field == "ladder":
            for ladder in Ladders:
                if not ladder.interact(Players[onplay].playerPos) == None:
                    Players[onplay].move(ladder.interact(Players[onplay].playerPos))

            print("climb")

        for snake in Snakes:
            snake.update()
        for ladder in Ladders:
            ladder.update()
        for player in Players:
            player.update()

        
        GameHandler.drawboard()

        if(Players[onplay].playerPos == 99):
           GameON = False
           break

        leaderboard()
        if not onplay+1 == numberofplayers:
            print(f"Now is playing Player{onplay+1}")
        elif onplay + 1 == numberofplayers:
            print(f"Now is playing Player0")

    
print("GameOver")





