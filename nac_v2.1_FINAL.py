#Naughts And Crosses - Version 2.0
#P1 = O, P2 = X

def initSetup():
    global gameOver, playerOneWin, playerTwoWin, rowValid, columnValid, choiceValid, rowNum, colNum, i, grid
    grid = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]] #Printing the empty 3x3 grid
    print(*grid, sep="\n")
    gameOver = False #Initial setup of variables
    playerOneWin = False
    playerTwoWin = False
    rowValid = False
    columnValid = False
    choiceValid = False
    rowNum = -1
    colNum = -1
    i = 1

def emptySpacesExist():
    global grid
    emptySpaces = 0
    for x in range(2):
        for y in range(2):
            if grid[x][y] == "-":
                emptySpaces = emptySpaces + 1
    if emptySpaces == 0:
        return True
    else:
        return False

def checkIfGameOver():
    global gameOver, playerOneWin, playerTwoWin, grid
    gameOver = emptySpacesExist()
    for i in range(3): 
        for j in range(3):
            if (grid[i][j] == "O") and (grid[i][0] == grid[i][1] == grid[i][2]): #Checking rows for a potential win
                gameOver = True
                playerOneWin = True
            elif grid[i][j] == "X" and grid[i][0] == grid[i][1] == grid[i][2]: #It also checks the other way just to be super sure
                gameOver = True
                playerTwoWin = True
            elif (grid[i][j] == "O") and (grid[0][j] == grid[1][j] == grid[2][j]): #Checking columns for a potential win
                gameOver = True
                playerOneWin = True
            elif grid[i][j] == "X" and grid[0][j] == grid[1][j] == grid[2][j]:
                gameOver = True
                playerTwoWin = True
    if (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or (grid[2][2] == "O" and grid [1][1] == "O" and grid[0][0] == "O"): #Checking diagonals
        gameOver = True
        playerOneWin = True
    elif (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or (grid[2][2] == "X" and grid[1][1] == "X" and grid[0][0] == "X"):
        gameOver = True
        playerTwoWin = True
    elif (grid[2][0] == "O" and grid[1][1] == "O" and grid[0][2] == "O") or (grid [0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O"):
        gameOver = True
        playerOneWin = True
    elif (grid[2][0] == "X" and grid[1][1] == "X" and grid[0][2] == "X") or (grid[0][2] == "X" and grid[1][1] == "X" and grid [2][0] == "X"):
        gameOver = True
        playerTwoWin = True

def outputWinner():
    global playerOneWin, playerTwoWin, gameOver
    if playerOneWin == True:
        print("Player 1 wins. Congratulations!")
    elif playerTwoWin == True:
        print("Player 2 wins. Congratulations!")
    elif playerOneWin == True and playerTwoWin == True:
            print("Oh, something went wrong here. Both of you win, I guess?")
    elif gameOver == True and playerOneWin == False and playerTwoWin == False:
            print("It's a draw!")

def turnEnd():
    global rowValid, columnValid, choiceValid, rowNum, colNum
    rowValid = False #I could probably use a subroutine to do all of this, but whatever
    columnValid = False
    choiceValid = False
    rowNum = -1
    colNum = -1
    print(*grid, sep="\n") #Print out the 3x3 grid again
    checkIfGameOver() #Check if the move that was just made won the player the game.
    if gameOver == True: #Double check to see if the gameOver variable is false'
        outputWinner()

def playerTurn(i):
    global choiceValid, rowValid, rowNum, columnValid, colNum, grid
    playerNum = i % 2
    if playerNum == 0:
        player = 2
    else:
        player = 1
    print("Player ", player,"'s turn. Enter a position.")
    while choiceValid == False:
        while rowValid == False: #P1 picks their row
            row = input("(T)op, (M)iddle or (B)ottom?>>: ")
            row = row.upper()
            if row == "T":
                rowValid = True
                rowNum = 0
            elif row == "M":
                rowValid = True
                rowNum = 1
            elif row == "B":
                rowValid = True
                rowNum = 2
            else:
                print("Please enter a valid row (Type T, M or B).")
                
        while columnValid == False: #P1 picks their column
            column = input("(L)eft, (M)iddle or (R)ight? [Type 'cancel' to go back]>>: ")
            column = column.upper()
            if column == "L":
                columnValid = True
                colNum = 0
            elif column == "M":
                columnValid = True
                colNum = 1
            elif column == "R":
                columnValid = True
                colNum = 2
            elif column == "CANCEL":
                rowValid = False
                rowNum = -1
                print("Turn cancelled. Returning to row selection.")
            else:
                print("Please enter a valid column (Type L, M or R).")
        if grid[rowNum][colNum] == "-" and playerNum == 1: #If this is Player 1 (code 1)
            grid[rowNum][colNum] = "O"
            choiceValid = True
        elif grid[rowNum][colNum] == "-" and playerNum == 0: #If this is Player 2 (code 0)
            grid[rowNum][colNum] = "X"
            choiceValid = True
        else: #If there is already an X or an O there...
            print("This space is already taken. Please pick again.") #Don't let them take that space.
    turnEnd()
       
def playGame():
    initSetup()
    global i
    global gameOver
    while gameOver == False:
        playerTurn(i)
        i = i + 1

playGame()
