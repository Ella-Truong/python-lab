# initialize the game
def initialize_game(size=3):
    player1='X'
    player2='O'
    players=[player1,player2]    

    board_list=[]
    for r in range(size):
        board_list.append([])
        for cell in range(size):
            board_list[r].append(' ')
    
    return players,board_list     # return a tuple of players=['X','O'] and board is 2D list



def display_board(board_list):
    size=len(board_list)
    for row in range(size):
        for col in range(size):
            print(board_list[row][col],end='|')
        print()


def update_board(board,player,loc):    #players is list of symbol, loc is a list of x and y location inputted by players
    if board[loc[0]][loc[1]] != ' ':
        print('The position is filled. Choose again.')
        return False
    else:
        board[loc[0]][loc[1]]=player
        return True


def check_win(board,symbol):
    size=len(board)

    #check row
    for row in board:
        if all(cell==symbol for cell in row):
            return True
        
    #check column
    for col in range(size):
        if all(board[row][col]==symbol for row in range(size)):
            return True
    
    #check top-left to bottom-right diagonal
    if all(board[i][i]==symbol for i in range(size)):
        return True
    
    #check top-right to bottom-left diagonal:
    if all(board[i][size-1-i]==symbol for i in range(size)):
        return True
    
    return False


def main():
    players,board=initialize_game()   #return players=['X','O'] and boarr=[[],[],[]]
    size=len(board)        #return a number of rows -> 3
    current_player=0      
    display_board(board)
    while True:
        player=players[current_player]
        while True:
            try:
                x=int(input('Enter a new x: '))
                y=int(input('Enter a new y: '))
                if 0<=x<size and 0<=y<size:
                    loc=(x,y)
                    print(f"Player {current_player+1} is at {loc}")
                    if update_board(board,player,loc):
                        display_board(board)
                        break
                else: 
                    print('Out of board. Choose again.')
            except ValueError:
                print('Invalid input. Please enter an integer')
            
        if check_win(board,player):
            print(f"Congratulations. Player {current_player+1} win.")
            break
        else:
            current_player=1-current_player 
          
if __name__=='__main__':
    main()









   








