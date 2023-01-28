#GUI taken from https://www.codespeedy.com/tic-tac-toe-gui-in-python-using-tkinter/

import sys
game_Board = []
init_game_board = [['','',''],['','',''],['','','']]
game_Board = init_game_board
AI = 'O'
HUMAN = 'X'
TIE = 'tie'
values = {'X':1,'O':-1,'tie':0}

def if_game_over(game_board):
    #Diagonal values check
    if(game_board[0][0] == game_board[1][1] == game_board[2][2] == HUMAN):
        return values[HUMAN]
    elif(game_board[0][0] == game_board[1][1] == game_board[2][2] == AI):
        return values[AI]

    #Check horizontally
    for i in range(0,3):
        if(game_board[i][0] == game_board[i][1] == game_board[i][2] == HUMAN):
            return values[HUMAN]
        elif(game_board[i][0] == game_board[i][1] == game_board[i][2] == AI):
            return values[AI]

    #Check vertically
    for j in range(0,3):
        if(game_board[0][j] == game_board[1][j] == game_board[2][j] == HUMAN):
            return values[HUMAN]
        elif(game_board[0][j] == game_board[1][j] == game_board[2][j] == AI):
            return values[AI]

    #check for tie
    t = True
    for i in range(0,3):
        for j in range(0,3):
            if(game_board[i][j]==''):
                t=False
    
    if(t):
        return values[TIE]
    
def minmax(game_board,isMaximizing,turn):
    if(isMaximizing):
        bestScore = 1-sys.maxsize
        for i in range(0,3):
            for j in range(0,3):
                if(game_board[i][j]==''):
                    game_board[i][j]=turn
                    score = if_game_over(game_board)
                    if(score==values[HUMAN] or score==values[AI] or score==values[TIE]):
                        return score
                    return max(bestScore,minmax(game_board,False,AI))
    else:
        bestScore = sys.maxsize
        for i in range(0,3):
            for j in range(0,3):
                if(game_board[i][j]==''):
                    game_board[i][j]=turn
                    score = if_game_over(game_board)
                    if(score==1 or score==-1 or score==0):
                        return score
                    return min(bestScore,minmax(game_board,False,HUMAN))

print(minmax(init_game_board, False, AI))


#GUI taken from https://www.codespeedy.com/tic-tac-toe-gui-in-python-using-tkinter/
#this code 
from tkinter import *
from tkinter import messagebox
import random as r
def button(frame):          #Function to define a button
    b=Button(frame,padx=1,bg="papaya whip",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b
def change_a():             #Function to change the operand for the next player
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
def reset():                #Resets the game
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
def check():                #Checks for victory or Draw
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Congrats!!","'"+a+"' has won")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' has won")
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","The match ended in a draw")
        reset()
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
        label.config(text=a+"'s Chance")
###############   Main Program #################
root=Tk()                   #Window defined
root.title("Tic-Tac-Toe")   #Title given
a=r.choice(['O','X'])       #Two operators defined
colour={'O':"deep sky blue",'X':"lawn green"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label=Label(text=a+"'s Chance",font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)
root.mainloop()