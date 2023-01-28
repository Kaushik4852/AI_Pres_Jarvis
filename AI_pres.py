import sys
init_game_board = [['','',''],['','',''],['','','']]
ai = 'O'
human = 'X'
tie = 'tie'
values = {'X':1,'O':-1,'tie':0}


# def driver(init):
#     print(game_over(game_board))
    
def if_game_over(game_board):
    #Diagonal values check
    if(game_board[0][0] == game_board[1][1] == game_board[2][2] == human):
        return values[human];
    elif(game_board[0][0] == game_board[1][1] == game_board[2][2] == ai):
        return values[ai];

    #Check horizontally
    for i in range(0,3):
        if(game_board[i][0] == game_board[i][1] == game_board[i][2] == human):
            return values[human];
        elif(game_board[i][0] == game_board[i][1] == game_board[i][2] == ai):
            return values[ai];

    #Check vertically
    for j in range(0,3):
        if(game_board[0][j] == game_board[1][j] == game_board[2][j] == human):
            return values[human];
        elif(game_board[0][j] == game_board[1][j] == game_board[2][j] == ai):
            return values[ai];

    #check for tie
    tie = True
    for i in range(0,3):
        for j in range(0,3):
            if(game_board[i][j]==''):
                tie=False
    
    if(tie):
        return values[tie];
    
def minmax(game_board,isMaximizing,turn):
    if(isMaximizing):
        bestScore = 1-sys.maxsize
        for i in range(0,3):
            for j in range(0,3):
                if(game_board[i][j]==''):
                    game_board[i][j]=turn;
                    score = if_game_over();
                    if(score==values[human] or score==values[ai] or score==values[tie]):
                        return score;
                    return max(bestScore,minmax(game_board,False,ai))
    else:
        bestScore = sys.maxsize
        for i in range(0,3):
            for j in range(0,3):
                if(game_board[i][j]==''):
                    game_board[i][j]=turn;
                    score = if_game_over();
                    if(score==1 or score==-1 or score==0):
                        return score;
                    return min(bestScore,minmax(game_board,False,human))


    

game_board = [['O','O','O'],
              ['X','O','O'],
              ['X','O','X']]
print(if_game_over(game_board))