import sys
init_game_board = [['','',''],['','',''],['','','']]
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