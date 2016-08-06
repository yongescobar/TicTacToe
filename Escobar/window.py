'''
Created on Jul 18, 2016

@author: Escobar

5 Aug, 2016
2nd version of Tic Tac Toe game 3x3

Added computer opponent, replacing 2nd player
Computer is the 2nd player; uses the Minimax algorithm 

Future additions:

- Reduce/Eliminate dependence of global variables
- Add "Game ended in draw" option; currently returns an error
- Custom board size beyond 3x3
- Optimize computer algorithm for a board larger than 3x3
- Custom win conditions beyond 3 in a row

End-State: Create a (m,n,k) board game, the generalized Tic Tac Toe

'''
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from functools import partial
from copy import deepcopy

import numpy as np

playerTurn = 1
gameBoard = np.array([[0,0,0],[0,0,0],[0,0,0]])
possibleSpots = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
buttonList = list()

def runComputer() :
    
    global buttonList
    global playerTurn
    global possibleSpots
    global gameBoard
    
    bestMove = None
    bestValue = float("-inf")
    
    for spot in possibleSpots :
        
        possibleMoves = deepcopy(possibleSpots)
        possibleMoves.remove(spot)
        
        row, col = spot
        
        testBoard = deepcopy(gameBoard)
        testBoard[row][col] = 2
        
        if winCheck(testBoard) :
            bestMove = spot
            break
        else :
            value = miniMax(possibleMoves, testBoard, 1)
            
            if value > bestValue :
                bestValue = value
                bestMove = spot
            
    row, col = bestMove
    
    gameBoard[row][col] = 2
    buttonList[row][col]["text"] = "O"
    possibleSpots.remove(bestMove)
    
    if(winCheck(gameBoard)) :
        winGame()
    else :
        nextPlayer()
        

def miniMax(possibleMoves, board, player) :
        
    if len(possibleMoves) == 1 :
        
        row, col = possibleMoves[0]
        
        testBoard = deepcopy(board)
        
        if player == 1 :
            testBoard[row][col] = 1
        else :
            testBoard[row][col] = 2
        
        if(winCheck(testBoard)) :
            if player == 1 :
                return -1
            else :
                return 1
        else :
            return 0
    
    if player == 1 :
        
        bestValue = float("inf")
        
        for move in possibleMoves :
                        
            row, col = move
            testBoard = deepcopy(board)
            nextMoves = deepcopy(possibleMoves)
            nextMoves.remove(move)
            
            testBoard[row][col] = 1
            
            if winCheck(testBoard) :
                return -1
            else :
                value = miniMax(nextMoves, testBoard, 2)
            
                if value < bestValue :
                    bestValue = value
                         
        return bestValue
    
    if player == 2 :
        
        bestValue = float("-inf")
        
        for move in possibleMoves :
            
            row, col = move
            testBoard = deepcopy(board)
            nextMoves = deepcopy(possibleMoves)
            nextMoves.remove(move)
            
            testBoard[row][col] = 2
            
            if winCheck(testBoard) :
                return 1
            else :
                value = miniMax(nextMoves, testBoard, 1)

                if value > bestValue :
                    bestValue = value
    
        return bestValue
    
def nextPlayer():
    global playerTurn
    
    #If playerTurn == 1, then change to player 2, else change to player 1
    playerTurn = 1 if playerTurn == 2 else 2
    
    if(playerTurn == 2) :
        runComputer()

#Occurs when a player wins the game
#Notify the players
#Give option to restart the game
def winGame() :
    
    global playerTurn
    global gameBoard
    global possibleSpots
    
    if messagebox.askyesno("Winner", "Player " + str(playerTurn) + " has won" + "\n" + "Restart?") :
        playerTurn = 1
        gameBoard = np.array([[0,0,0],[0,0,0],[0,0,0]])
        possibleSpots = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        b1["text"] = ""
        b2["text"] = ""
        b3["text"] = ""
        b4["text"] = ""
        b5["text"] = ""
        b6["text"] = ""
        b7["text"] = ""
        b8["text"] = ""
        b9["text"] = ""

def drawGame() :
    
    global playerTurn
    global gameBoard
    global possibleSpots
    
    if messagebox.askyesno("Draw", "Draw" + "\n" + "Restart?") :
        playerTurn = 1
        gameBoard = np.array([[0,0,0],[0,0,0],[0,0,0]])
        possibleSpots = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        b1["text"] = ""
        b2["text"] = ""
        b3["text"] = ""
        b4["text"] = ""
        b5["text"] = ""
        b6["text"] = ""
        b7["text"] = ""
        b8["text"] = ""
        b9["text"] = ""

#Occurs after a player has marked a position and called by nextTurn()
#Checks if the current player has won, returns true; else False         
def winCheck(board) :
    
    if (board[0][0] == board[0][1] == board[0][2] or board[0][0] == board[1][0] == board[2][0] or board[0][0] == board[1][1] == board[2][2]) and board[0][0] in (1, 2) :
        return True
    
    elif (board[2][0] == board[2][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]) and board[2][0] in (1, 2) :
        return True
    
    elif (board[0][2] == board[1][2] == board[2][2]) and board[0][2] in (1,2) :
        return True
            
    elif (board[0][1] == board[1][1] == board[2][1] or board[1][0] == board[1][1] == board[1][2]) and board[1][1] in (1,2) :
        return True
    
    return False

#Occurs after a player has marked a position
#Calls winCheck to see if the current player has won; else moves onto the next Player
def nextTurn():
    
    global possibleSpots
    #if the current player did not win, then move onto the next player
    if(winCheck(gameBoard)) :
        winGame()
    elif len(possibleSpots) == 0 :
        drawGame()
    else :
        nextPlayer()
    


def pressed(button):
    
    global playerTurn
    
    buttonInfo = button.grid_info()
    
    #the -1 term exists because row/column for buttons start from 1 not 0
    row = int(buttonInfo["row"]) - 1
    column = int(buttonInfo["column"]) - 1
    
    if(playerTurn == 1 ) :
        button["text"] = "X"
        gameBoard[row][column] = 1
    #else :
     #   button["text"] = "O"
     #   gameBoard[row][column] = 2
    
    possibleSpots.remove([row, column])

    nextTurn()
    
    
root = Tk()
root.title("Tic Tac Toe")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

defH = 5
defW = 10


b1 = Button(mainframe, height = defH, width = defW)
b1.grid(row = 1, column = 1)

#Using command = pressed(b1) automatically calls on the command function even though the button was not pressed.
#More info: http://stackoverflow.com/questions/6920302/how-to-pass-arguments-to-a-button-command-in-tkinter
#Alternative: command = lambda : action(argument)
#Alternative leads to potential bugs if buttons are created in a loop with this command function as the argument takes on its previous value before the loop
#Not when the button is created per iteration. 
b1.configure(command = partial(pressed, b1))


b2 = Button(mainframe, height = defH, width = defW)
b2.grid(row = 2, column = 1)
b2.configure(command = partial(pressed, b2))

b3 = Button(mainframe, height = defH, width = defW)
b3.grid(row = 3, column = 1)
b3.configure(command = partial(pressed, b3))

b4 = Button(mainframe, height = defH, width = defW)
b4.grid(row = 1, column = 2)
b4.configure(command = partial(pressed, b4))

b5 = Button(mainframe, height = defH, width = defW)
b5.grid(row = 2, column = 2)
b5.configure(command = partial(pressed, b5))

b6 = Button(mainframe, height = defH, width = defW)
b6.grid(row = 3, column = 2)
b6.configure(command = partial(pressed, b6))

b7 = Button(mainframe, height = defH, width = defW)
b7.grid(row = 1, column = 3)
b7.configure(command = partial(pressed, b7))

b8 = Button(mainframe, height = defH, width = defW)
b8.grid(row = 2, column = 3)
b8.configure(command = partial(pressed, b8))

b9 = Button(mainframe, height = defH, width = defW)
b9.grid(row = 3, column = 3)
b9.configure(command = partial(pressed, b9))

buttonList = [[b1, b4, b7],[b2, b5, b8], [b3, b6, b9]]

root.mainloop()