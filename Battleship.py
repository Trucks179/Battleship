
import numpy as np
from random import *

#board = np.zeros((10,10))

#print('')
# print(board)

# for x in range(10):
#     for y in range(10):
#         board[x][y] = randint(1,100)

# print(board)




class Board:
    'Creating a board'
    boardCount = 0 #this variable is shared among all instances of this class

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.alias = []
        for x in range(10):
            self.alias.append([' '])
        for x in range(10):
            for y in range(9):
                self.alias[x].append(' ')
        Board.boardCount += 1
        
    def printBoard(self):
        print('')
        print('   A    B    C    D    E    F    G    H    I    J')
        for x in range(10):
            print(str(x) + str(self.alias[x]))

    def cleanBoard(self):
        for x in range(10):
            for y in range(10):
                self.alias[x][y] = ' '


                
gameBoard = Board(10,10)

gameBoard.printBoard()
gameBoard.cleanBoard()
