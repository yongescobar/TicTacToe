'''
Created on Jul 18, 2016

@author: Escobar

24 Jul, 2016
1st version of Tic Tac Toe game 3x3

Future additions:

- Include a computer opponent
- Custom board size beyond 3x3
- Custom win conditions beyond 3 in a row

End-State: Create a (m,n,k) board game, the generalized Tic Tac Toe

'''
from tkinter import *
from tkinter import ttk

import numpy as np

playerTurn = 1
gameBoard = np.array([[0,0,0],[0,0,0],[0,0,0]])

def nextPlayer():
    global playerTurn
    
    playerTurn = 1 if playerTurn == 2 else 2

def winCheck() :
    
    if (gameBoard[0][0] == gameBoard[0][1] == gameBoard[0][2] or gameBoard[0][0] == gameBoard[1][0] == gameBoard[2][0] or gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]) and gameBoard[0][0] in (1, 2) :
        print(playerTurn, " has won the game!")
    
    elif (gameBoard[2][0] == gameBoard[2][1] == gameBoard[2][2] or gameBoard[2][0] == gameBoard[1][1] == gameBoard[0][2]) and gameBoard[2][0] in (1, 2) :
        print(playerTurn, "has won the game!") 
    
    elif (gameBoard[0][2] == gameBoard[1][2] == gameBoard[2][2]) and gameBoard[0][2] in (1,2) :
        print(playerTurn, "has won the game!")
            
    elif (gameBoard[0][1] == gameBoard[1][1] == gameBoard[2][1] or gameBoard[1][0] == gameBoard[1][1] == gameBoard[1][2]) and gameBoard[1][1] in (1,2) :
        print(playerTurn, "has won the game!")

def nextTurn():
    
    winCheck()
    nextPlayer()

def pressed1() :
    
    global playerTurn

    if (playerTurn == 1) :
        b1["text"] = "X"
        gameBoard[0][0] = 1
    else :
        b1["text"] = "O"
        gameBoard[0][0] = 2
        
    nextTurn()

def pressed2() :

    global playerTurn

    if (playerTurn == 1) :
        b2["text"] = "X"
        gameBoard[1][0] = 1
    else :
        b2["text"] = "O"
        gameBoard[1][0] = 2
    
    nextTurn()
    
def pressed3() :

    global playerTurn

    if (playerTurn == 1) :
        b3["text"] = "X"
        gameBoard[2][0] = 1
    else :
        b3["text"] = "O"
        gameBoard[2][0] = 2
    
    nextTurn()
    
def pressed4() :

    global playerTurn

    if (playerTurn == 1) :
        b4["text"] = "X"
        gameBoard[0][1] = 1
    else :
        b4["text"] = "O"
        gameBoard[0][1] = 2
    
    nextTurn()
    
def pressed5() :

    global playerTurn

    if (playerTurn == 1) :
        b5["text"] = "X"
        gameBoard[1][1] = 1
    else :
        b5["text"] = "O"
        gameBoard[1][1] = 2
        
    nextTurn()
    
def pressed6() :

    global playerTurn

    if (playerTurn == 1) :
        b6["text"] = "X"
        gameBoard[2][1] = 1
    else :
        b6["text"] = "O"
        gameBoard[2][1] = 2

    nextTurn()
    
def pressed7() :

    global playerTurn

    if (playerTurn == 1) :
        b7["text"] = "X"
        gameBoard[0][2] = 1
    else :
        b7["text"] = "O"
        gameBoard[0][2] = 2
        
    nextTurn()   
    
def pressed8() :

    global playerTurn

    if (playerTurn == 1) :
        b8["text"] = "X"
        gameBoard[1][2] = 1
    else :
        b8["text"] = "O"
        gameBoard[1][2] = 2
    
    nextTurn()
    
def pressed9() :

    global playerTurn

    if (playerTurn == 1) :
        b9["text"] = "X"
        gameBoard[2][2] = 1
    else :
        b9["text"] = "O"
        gameBoard[2][2] = 2

    nextTurn()
    
root = Tk()
root.title("Tic Tac Toe")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

defH = 5
defW = 10

b1 = Button(mainframe, command = pressed1, height = defH, width = defW)
b1.grid(column=1, row =1)

b2 = Button(mainframe, command = pressed2, height = defH, width = defW)
b2.grid(column=1, row =2)

b3 = Button(mainframe, command = pressed3, height = defH, width = defW)
b3.grid(column=1, row =3)

b4 = Button(mainframe, command = pressed4, height = defH, width = defW)
b4.grid(column=2, row =1)

b5 = Button(mainframe, command = pressed5, height = defH, width = defW)
b5.grid(column=2, row =2)

b6 = Button(mainframe, command = pressed6, height = defH, width = defW)
b6.grid(column=2, row =3)

b7 = Button(mainframe, command = pressed7, height = defH, width = defW)
b7.grid(column=3, row =1)

b8 = Button(mainframe, command = pressed8, height = defH, width = defW)
b8.grid(column=3, row =2)

b9 = Button(mainframe, command = pressed9, height = defH, width = defW)
b9.grid(column=3, row =3)


root.mainloop()