import random
def display(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j])
        print("\n")    

def initialization( board):
    board=np.array([[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]])    
    return(board)    
def checkfill(board):
    for i in board:
        if '-' in i:
            return False
        else:
            return True            
def checkwon(board):
    if board[0][0]==board[1][1]==board[2][2]=="O":
        return("O")
    elif  board[0][0]==board[1][1]==board[2][2]=="X":
        return("X")       
    elif board[0][2]==board[1][1]==board[2][0]=="O":
        return("O")   
    elif board[0][2]==board[1][1]==board[2][0]=="X":
        return("X") 
    else:    
        for i in range(3):
            for j in range(3):
                if board[j][1]==board[j][2]==board[j][3]=='X':
                    return("X")
                elif board[j][1]==board[j][2]==board[j][3]=='O':
                    return("O")
                elif board[1][j]==board[2][j]==board[3][j]=="X":
                    return("X")
                elif board[1][j]==board[2][j]==board[3][j]=="O":
                    return("O")  
    return(-1)                 
    
def start_game ():
    board=[]
    game=0
    print("     Board:    \n")
    board=initialization(board)

    choose=['user','comp']
    turn=random.choice(choose)
#     display(board)      
    while(game!=1):
        display(board)
        if turn=='user':
            print("USER")
            print("Enter the position\n")
            m,n=map(int , input().split())
            board[m][n]="X"
            turn="comp"
        else:
            print("COMPUTER")
            m=random.choice(range(0,3))    
            n=random.choice(range(0,3))
            if board[m][n]=="-":
                board[m][n]="O"
            else:
                while board[m][n]!="-":
                    m=random.choice(range(0,3))    
                    n=random.choice(range(0,3))
                    if board[m][n]=="-":
                        board[m][n]="O"
                        break
            turn="user"
#         display(board)    
        k=checkwon(board)    
        if k=="X":
            print("X won!!!!!")
            display(board) 
            game=1
            break
        elif k=="O":
            print("O won!!!!!")
            display(board) 
            game=1
            break
        elif checkfill==True:
            print("Tie :(")
            display(board) 
            game=1
            break
        else:
            continue
start_game()