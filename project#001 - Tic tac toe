"""
Project 001
Tic tac toe
Instruction:
    3x3 matrix: [[“_”, “_”, “_”] , [“_”, “_”, “_” ], [“_”, “_”, “_”]]
    Inputs: 0-2 twice (first row, then column), first palyer=X or x, second player=O or o.
    1)In each turn, the player choose row number (0-2), and then column number (0-2)
    2)The program needs to check if the input is valid:
        a)the number is between 0-2.
        b)the square is empty ("_")
    3)Invaild value - the player needs to write again row and column, until he submin a valid input.
    4)After the first player enter a valid location numbers, the "X" needs to be storage in the same location in the matrix, and then print the new matrix.
    5)Now the second player enter his location values, after he finish, again print the new matrix with the O in the location the second player inserted.
    6)If someone win, print a victory to the winning player, and ask if the want a rematch.
    7)If it's a tie, print that it's a draw, and ask for a rematch.
    *8)Add input check if a player type on Enter or a non-valid.
    *9)pc as a player - random.
    *10)pc vs pc
    *11)check if next turn is winning.
    *12)4x4 board.
"""
import random

def board(f3or4):
    """
    define the board size (3x3 or 4x4)
    :param f3or4: 3=3x3 or 4=4x4
    :return:the defined global board
    """
    if f3or4==3:
        global board3
        return board3
    elif f3or4==4:
        global board4
        return board4

def vis_board(f3or4,board):
    """
    print visual board
    :param f3or4: 3x3 or 4x4 board
    :param board: board to print
    :return: None
    """
    if f3or4==3:
        print("",board[0:1][0:3],"\n",board[1:2][0:3],"\n",board[2:3][0:3])
    elif f3or4==4:
        print("",board[0:1][0:4],"\n",board[1:2][0:4],"\n",board[2:3][0:4],"\n",board[3:4][0:4])
    return None

def change_board(f3or4,row,col,x_o):
    """
    this function change the board according to what the user insert
    :param f3or4: understend which board it is.
    :param row: input row from the player
    :param col: input col from the player
    :param x_o: insert x or o
    :return: the changed board
    """
    ch_board=board(f3or4)
    ch_board[row][col]=x_o
    return ch_board

def check_empty(row,col):
    """
    check if the spot is empty or have x or o
    :param row: input row from the player
    :param col: input col from the player
    :return: 1 if the spot is empty, other print to the player if the spot has a x or o, otherwise (not supposed to be) it's not empty
    """
    global f3or4
    if board(f3or4)[row][col]=="_":
        return 1
    elif board(f3or4)[row][col]=="x":
        print("This spot already has an x")
        return -1
    elif board(f3or4)[row][col]=="o":
        print("This spot already has an o")
        return -1
    else:
        print("this spot isn't empty")
        return -1

def input_check(userInput):
    """
    check that the input is valid
    :param userInput: input  from the user
    :return: according to the input, None for return to the main loop
    """
    global f3or4
    global pc
    if userInput==0 or userInput=="0":
        if f3or4==0:
            print("Worng input, please insert a valid option.")
            return None
        else:
            return 0
    elif userInput==1 or userInput=="1":
        if f3or4==0:
            f3or4=3
        return 1
    elif userInput==2 or userInput=="2":
        if f3or4==0:
            f3or4=4
        return 2
    elif userInput==3 or userInput=="3":
        if f3or4==0 or f3or4==3:
            print("Worng input, please insert a valid option.")
            return None
        else:
            return 3
    elif userInput=="3x3" or userInput=="3X3":
        if f3or4==3 or f3or4==4:
            print("Worng input, please insert a valid option.")
            return None
        f3or4=3
        return None
    elif userInput=="4x4" or userInput=="4X4":
        if f3or4==3 or f3or4==4:
            print("Worng input, please insert a valid option.")
            return None
        f3or4=4
        return None
    elif userInput=="q" or userInput=="Q":
        return -1
    else:
        print ("Worng input, please insert a valid option.")
        return None

def row(f3or4):
    """
    get the row input
    :param f3or4: verify if the board is 3x3 or 4x4
    :return: the row value
    """
    while True:
        row=input_check(input("please enter the row number:"))
        if f3or4==3 and row<=2 and row>=0:
            return int(row)
        elif f3or4==4 and row<=3 and row>=0:
            return int(row)
        elif row==-1: #the player write q, which mean worng input and not quit the game
            print("Worng input, please insert a valid option.")
            continue

def col(f3or4):
    """
    get the col input
    :param f3or4: verify if the board is 3x3 or 4x4
    :return: the col value
    """
    while True:
        col=input_check(input("please enter the col number:"))
        if f3or4==3 and col<=2 and col>=0:
            return int(col)
        elif f3or4==4 and col<=3 and col>=0:
            return int(col)
        elif col==-1: #the player write q, which mean worng input and not quit the game
            print("Worng input, please insert a valid option.")
            continue

def input_player01(f3or4,p1):
    """
    input from player 1 - x
    :param f3or4: verify if the board is 3x3 or 4x4
    :return: row and col input
    """
    while True:
        print("-{} your input-".format(p1))
        rowP1=row(f3or4)
        colP1=col(f3or4)
        if check_empty(rowP1,colP1)==1:
            return rowP1,colP1
        else:
            print("please write a now location.")
            continue

def P1(f3or4,p1,board):
    """
    define the "playground" of player 1
    :param f3or4: verify if the board is 3x3 or 4x4
    :param p1: player 1 name - bad name choice, I know...
    :param board: copy board
    :return: 1 if rematch -1 to end the game
    """
    row_col1=input_player01(f3or4,p1) #list of the row and col of player 1
    vis_board(f3or4,change_board(f3or4,row_col1[0],row_col1[1],"x")) #change the board according to the player input, and print the visual board
    if vicCheck(f3or4,board)=="victory": #check victory
        player_win(p1)
        if rematch()==1:
            return 1
        else:
            #game end
            return -1
    elif vicCheck(f3or4,board)=="draw": #check draw
        print("it's a draw")
        if rematch()==1:
            return 1
        else:
            #game end
            return -1

def input_player02(f3or4,p2):
    """
    input from player 2 - o
    :param f3or4: verify if the board is 3x3 or 4x4
    :return: row and col input
    """
    while True:
        print("-{} your input-".format(p2))
        rowP2=row(f3or4)
        colP2=col(f3or4)
        if check_empty(rowP2,colP2)==1:
            return rowP2,colP2
        else:
            print("please write a new location.")
            continue

def P2(f3or4,p2,board):
    """
    define the "playground" of player 2
    :param f3or4: verify if the board is 3x3 or 4x4
    :param p1: player 2 name - bad name choice, I know...
    :param board: copy board
    :return: 1 if rematch -1 to end the game
    """
    row_col2=input_player02(f3or4,p2) #list of the row and col of player 2
    vis_board(f3or4,change_board(f3or4,row_col2[0],row_col2[1],"o")) #change the board according to the player input, and print the visual board
    if vicCheck(f3or4,board)=="victory": #check victory
        player_win(p2)
        if rematch()==1:
            return 1
        else:
            #game end
            return -1
    elif vicCheck(f3or4,board)=="draw": #check draw
        print("it's a draw")
        if rematch()==1:
            return 1
        else:
            #game end
            return -1

def check_empty_pc(row,col):
    """
    check if the spot is empty or have x or o
    :param row: input row from the player
    :param col: input col from the player
    :return: 1 if the spot is empty, other print to the player if the spot has a x or o, otherwise (not supposed to be) it's not empty
    """
    global f3or4
    if board(f3or4)[row][col]=="_":
        return 1
    elif board(f3or4)[row][col]=="x":
        #print("This spot already has an x")
        return -1
    elif board(f3or4)[row][col]=="o":
        #print("This spot already has an o")
        return -1
    else:
        #print("this spot isn't empty")
        return -1

def input_pc(f3or4):
    """
    input from pc - o
    :param f3or4: verify if the board is 3x3 or 4x4
    :return: row and col pc
    """
    while True:
        if f3or4==3:
            rowPC=random.randint(0,2)
            colPC=random.randint(0,2)
        elif f3or4==4:
            rowPC=random.randint(0,3)
            colPC=random.randint(0,3)
        if check_empty_pc(rowPC,colPC)==1:
            return rowPC,colPC
        else:
            continue

def C1(f3or4,p1,board):
    """
    define the "playground" of pc 1
    :param f3or4: verify if the board is 3x3 or 4x4
    :param p1: pc 1 name - bad name choice, I know...
    :param board: copy board
    :return: 1 if rematch -1 to end the game
    """
    row_col1=input_pc(f3or4) #list of the row and col of player 1
    vis_board(f3or4,change_board(f3or4,row_col1[0],row_col1[1],"x")) #change the board according to the player input, and print the visual board
    if vicCheck(f3or4,board)=="victory": #check victory
        player_win(p1)
        if rematch()==1:
            return 1
        else:
            #game end
            return -1
    elif vicCheck(f3or4,board)=="draw": #check draw
        print("it's a draw")
        if rematch()==1:
            return 1
        else:
            #game end
            return -1

def C2(f3or4,p2,board):
    """
    define the "playground" of pc 2
    :param f3or4: verify if the board is 3x3 or 4x4
    :param p1: pc 2 name - bad name choice, I know...
    :param board: copy board
    :return: 1 if rematch -1 to end the game
    """
    row_col2=input_pc(f3or4) #list of the row and col of player 2
    vis_board(f3or4,change_board(f3or4,row_col2[0],row_col2[1],"o")) #change the board according to the player input, and print the visual board
    if vicCheck(f3or4,board)=="victory": #check victory
        player_win(p2)
        if rematch()==1:
            return 1
        else:
            #game end
            return -1
    elif vicCheck(f3or4,board)=="draw": #check draw
        print("it's a draw")
        if rematch()==1:
            return 1
        else:
            #game end
            return -1

def check_pc_input(userInput):
    """
    check that the input is valid - I know i could merge it into input_check(), but I wrote this function too late, and it took me a while to change the input_check(), so I preferred to write another one...
    :param userInput: input from the user
    :return: according to the input, "invalid" for return to the main loop
    """
    if userInput==1 or userInput=="1":
        return 1
    elif userInput==2 or userInput=="2":
        return 2
    elif userInput==3 or userInput=="3":
        return 3
    else:
        print("Worng input, please insert a valid option.")
        return "invalid"

def vicCheck(f3orf4,board):
    """
    check if a player win
    :param board: the board
    :return: victory if win, draw if draw
    """
    c_test=0
    if f3orf4==3:
        if board[0][0]==board[0][1]==board[0][2]=="x" or board[0][0]==board[0][1]==board[0][2]=="o":
            return "victory"
        elif board[1][0]==board[1][1]==board[1][2]=="x" or board[1][0]==board[1][1]==board[1][2]=="o":
            return "victory"
        elif board[2][0]==board[2][1]==board[2][2]=="x" or board[2][0]==board[2][1]==board[2][2]=="o":
            return "victory"
        elif board[0][0]==board[1][0]==board[2][0]=="x" or board[0][0]==board[1][0]==board[2][0]=="o":
            return "victory"
        elif board[0][1]==board[1][1]==board[2][1]=="x" or board[0][1]==board[1][1]==board[2][1]=="o":
            return "victory"
        elif board[0][2]==board[1][2]==board[2][2]=="x" or board[0][2]==board[1][2]==board[2][2]=="o":
            return "victory"
        elif board[0][0]==board[1][1]==board[2][2]=="x" or board[0][0]==board[1][1]==board[2][2]=="o":
            return "victory"
        elif board[0][2]==board[1][1]==board[2][0]=="x" or board[0][2]==board[1][1]==board[2][0]=="o":
            return "victory"
        else:
            for i in board:
                for j in i:
                    if j!="_":
                        c_test+=1
                        if c_test==9:
                            c_test=0
                            return "draw"
            return -1
    if f3orf4==4:

#       ["x","x","x","_"]  ["00","01","02","03"]
#       ["x","x","x","_"]  ["10","11","12","13"]
#       ["x","x","x","_"]  ["20","21","22","23"]
#       ["_","_","_","_"]  ["30","31","32","33"]

        if board[0][0]==board[0][1]==board[0][2]=="x" or board[0][0]==board[0][1]==board[0][2]=="o":
            return "victory"
        elif board[1][0]==board[1][1]==board[1][2]=="x" or board[1][0]==board[1][1]==board[1][2]=="o":
            return "victory"
        elif board[2][0]==board[2][1]==board[2][2]=="x" or board[2][0]==board[2][1]==board[2][2]=="o":
            return "victory"
        elif board[0][0]==board[1][0]==board[2][0]=="x" or board[0][0]==board[1][0]==board[2][0]=="o":
            return "victory"
        elif board[0][1]==board[1][1]==board[2][1]=="x" or board[0][1]==board[1][1]==board[2][1]=="o":
            return "victory"
        elif board[0][2]==board[1][2]==board[2][2]=="x" or board[0][2]==board[1][2]==board[2][2]=="o":
            return "victory"
        elif board[0][0]==board[1][1]==board[2][2]=="x" or board[0][0]==board[1][1] ==board[2][2]=="o":
            return "victory"
        elif board[0][2]==board[1][1]==board[2][0]=="x" or board[0][2]==board[1][1]==board[2][0]=="o":
            return "victory"

#       ["_","x","x","x"]  ["00","01","02","03"]
#       ["_","x","x","x"]  ["10","11","12","13"]
#       ["_","x","x","x"]  ["20","21","22","23"]
#       ["_","_","_","_"]  ["30","31","32","33"]

        elif board[0][1]==board[0][2]==board[0][3]=="x" or board[0][1]==board[0][2]==board[0][3]=="o":
            return "victory"
        elif board[1][1]==board[1][2]==board[1][3]=="x" or board[1][1]==board[1][2]==board[1][3]=="o":
            return "victory"
        elif board[2][1]==board[2][2]==board[2][3]=="x" or board[2][1]==board[2][2]==board[2][3]=="o":
            return "victory"
        elif board[0][1]==board[1][1]==board[2][1]=="x" or board[0][1]==board[1][1]==board[2][1]=="o":
            return "victory"
        elif board[0][2]==board[1][2]==board[2][2]=="x" or board[0][2]==board[1][2]==board[2][2]=="o":
            return "victory"
        elif board[0][3]==board[1][3]==board[2][3]=="x" or board[0][3]==board[1][3]==board[2][3]=="o":
            return "victory"
        elif board[0][1]==board[1][2]==board[2][3]=="x" or board[0][1]==board[1][2]==board[2][3]=="o":
            return "victory"
        elif board[0][3]==board[1][2]==board[2][1]=="x" or board[0][3]==board[1][2]==board[2][1]=="o":
            return "victory"

#       ["_","_","_","_"]  ["00","01","02","03"]
#       ["x","x","x","_"]  ["10","11","12","13"]
#       ["x","x","x","_"]  ["20","21","22","23"]
#       ["x","x","x","_"]  ["30","31","32","33"]

        elif board[1][0]==board[1][1]==board[1][2]=="x" or board[1][0]==board[1][1]==board[1][2]=="o":
            return "victory"
        elif board[2][0]==board[2][1]==board[2][2]=="x" or board[2][0]==board[2][1]==board[2][2]=="o":
            return "victory"
        elif board[3][0]==board[3][1]==board[3][2]=="x" or board[3][0]==board[3][1]==board[3][2]=="o":
            return "victory"
        elif board[1][0]==board[2][0]==board[3][0]=="x" or board[1][0]==board[2][0]==board[3][0]=="o":
            return "victory"
        elif board[1][1]==board[2][1]==board[3][1]=="x" or board[1][1]==board[2][1]==board[3][1]=="o":
            return "victory"
        elif board[1][2]==board[2][2]==board[3][2]=="x" or board[1][2]==board[2][2]==board[3][2]=="o":
            return "victory"
        elif board[1][0]==board[2][1]==board[3][2]=="x" or board[1][0]==board[2][1]==board[3][2]=="o":
            return "victory"
        elif board[1][2]==board[2][1]==board[3][0]=="x" or board[1][2]==board[2][1]==board[3][0]=="o":
            return "victory"

#       ["_","_","_","_"]  ["00","01","02","03"]
#       ["_","x","x","x"]  ["10","11","12","13"]
#       ["_","x","x","x"]  ["20","21","22","23"]
#       ["_","x","x","x"]  ["30","31","32","33"]

        elif board[1][1]==board[1][2]==board[1][3]=="x" or board[1][1]==board[1][2]==board[1][3]=="o":
            return "victory"
        elif board[2][1]==board[2][2]==board[2][3]=="x" or board[2][1]==board[2][2]==board[2][3]=="o":
            return "victory"
        elif board[3][1]==board[3][2]==board[3][3]=="x" or board[3][1]==board[3][2]==board[3][3]=="o":
            return "victory"
        elif board[1][1]==board[2][1]==board[3][1]=="x" or board[1][1]==board[2][1]==board[3][1]=="o":
            return "victory"
        elif board[1][2]==board[2][2]==board[3][2]=="x" or board[1][2]==board[2][2]==board[3][2]=="o":
            return "victory"
        elif board[1][3]==board[2][3]==board[3][3]=="x" or board[1][3]==board[2][3]==board[3][3]=="o":
            return "victory"
        elif board[1][1]==board[2][2]==board[3][3]=="x" or board[1][1]==board[2][2]==board[3][3]=="o":
            return "victory"
        elif board[1][3]==board[2][2]==board[3][1]=="x" or board[1][3]==board[2][2]==board[3][1]=="o":
            return "victory"
        else:
            for i in board:
                for j in i:
                    if j != "_":
                        c_test += 1
                        if c_test == 16:
                            c_test = 0
                            return "draw"
            return -1

def player_win(p):
    """
    print the player who win
    :param p: the winnig player
    :return:
    """
    print("{} win.".format(p))

def rematch():
    """
    rematch the game if the player want to
    :return: 1 for a rematch, 0 if not, otherwise it's not a valid option
    """
    while True:
        rematch=input("Do you want a rematch?\n1)yes\n2)no\nyour choice?")
        if rematch==1 or rematch=="1":
            return 1
        elif rematch==2 or rematch=="2":
            return 0
        elif rematch=="yes" or rematch=="Yes" or rematch=="YES":
            return 1
        elif rematch=="no" or rematch=="No" or rematch=="NO":
            return 0
        else:
            print("Worng input, please insert a valid option.")
            continue


print("-Hi, welcome to a tic-tac-toe game-\n")

while True:
    f3or4=0 #flag#00 - understend if it a 3x3 board or 4x4 board.
    PvP=0 #flag#01 - reset PvP= player vs player
    PvC=0 #flag#02 - reset PvC= player vs computer
    CvC=0 #flag#03 - reset PvP= computer vs computer
    exitt=0 #flag#04 - exit from the game
    #define 3x3 board + reset it
    board3=[["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]]
    # define 4x4 board + reset it
    board4=[["_", "_", "_", "_"],
              ["_", "_", "_", "_"],
              ["_", "_", "_", "_"],
              ["_", "_", "_", "_"]]
    print("please set the board size:")
    print("1)3x3\n"
          "2)4x4\n"
          "if you want to exit the game, please type q")
    userInput=input_check(input("your choice?"))
    if userInput==-1: #if the user want to exit from the game
        exitt=1
    if f3or4==3 or f3or4==4:
        while True:
            print("Please choose how you want to play:")
            print("1)player vs player\n"
                  "2)player vs pc\n"
                  "3)pc vs pc")
            PCinput=check_pc_input(input("your choice?"))
            if PCinput==1: #player vs player
                if f3or4==3 or f3or4==4:
                    p1=input("please write your name player number 1 (x player):") #name of player 1 (x)
                    p2=input("please write your name player number 2 (o player):") #name of player 2 (o)
                    PvP=1 #player vs player
                    PvC=0
                    CvC=0
                    break
            elif PCinput==2: #player vs pc
                if f3or4==3 or f3or4==4:
                    p1=input("please write your name (x player):") #name of player 1 (x)
                    p2="pc"
                    PvP=0
                    PvC=1 #player vs pc
                    CvC=0
                    break
            elif PCinput==3: #PC vs PC
                if f3or4==3 or f3or4==4:
                    p1="pc 1 (x)"
                    p2="pc 2 (o)"
                    PvP=0
                    PvC=0
                    CvC=1 #PC vs PC
                    break
    if PvP==1:
        while True:
    #---------------board 3x3---------------
            if f3or4==3:
                #player 1 turn
                player1=P1(f3or4,p1,board3)
                if player1==1:
                    break #restart the game
                elif player1==-1:
                    exitt=1
                    break #finish the game
                #player 2 turn
                player2=P2(f3or4,p2,board3)
                if player1==1:
                    break #restart the game
                elif player1==-1:
                    exitt=1
                    break #finish the game
    #---------------board 4x4---------------
            elif f3or4==4:
                #player 1 turn
                player1=P1(f3or4,p1,board4)
                if player1==1:
                    break #restart the game
                elif player1==-1:
                    exitt=1
                    break #finish the game
                #player 2 turn
                player2=P2(f3or4,p2,board4)
                if player1==1:
                    break #restart the game
                elif player1==-1:
                    exitt=1
                    break #finish the game
            else:
                break #restart the game
    elif PvC==1:
        while True:
    #---------------board 3x3---------------
            if f3or4==3:
                #player 1 turn
                player1=P1(f3or4,p1,board3)
                print("-------------------")
                if player1==1:
                    break #restart the game
                elif player1==-1:
                    exitt=1
                    break #finish the game
                #PC turn
                player2=C2(f3or4,p2,board3)
                if player2==1:
                    break #restart the game
                elif player2==-1:
                    exitt=1
                    break #finish the game
    #---------------board 4x4---------------
            if f3or4==4:
                #player 1 turn
                player1=P1(f3or4,p1,board4)
                print("------------------------")
                if player1==1:
                    break #restart the game
                elif player1==-1:
                    exitt=1
                    break #finish the game
                #PC turn
                player2=C2(f3or4,p2,board4)
                if player2==1:
                    break #restart the game
                elif player2==-1:
                    exitt=1
                    break #finish the game
    elif CvC==1:
        while True:
    #---------------board 3x3---------------
            if f3or4==3: #board 3x3
                #pc 1 turn
                player1=C1(f3or4,p1,board3)
                print("-------------------")
                if player1==1:
                    break #restart the game
                elif player1==-1:
                    exitt=1
                    break #finish the game
                #PC 2 turn
                player2=C2(f3or4,p2,board3)
                print("-------------------")
                if player2==1:
                    break #restart the game
                elif player2==-1:
                    exitt=1
                    break #finish the game
    #---------------board 4x4---------------
            if f3or4==4: #board 3x3
                #pc 1 turn
                player1=C1(f3or4,p1,board4)
                print("------------------------")
                if player1==1:
                    break #restart the game
                elif player1==-1:
                    exitt=1
                    break #finish the game
                #PC 2 turn
                player2=C2(f3or4,p2,board4)
                print("------------------------")
                if player2==1:
                    break #restart the game
                elif player2==-1:
                    exitt=1
                    break #finish the game
        #---------sub-main loop finish---------------
    if exitt==1:
        exitt=0
        print("You're out of the game, have a nice day!")
        break
        f3or4=0 #reset the board flag for a new board

