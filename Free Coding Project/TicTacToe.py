import random
#5 hours 30 minutes worked 11-27-2025
def main():
    #declare variables and print the board
    width = 3
    height = 3
    userMoves = 0
    board = createBoard(width,height)
    displayBoard(board)
    #grab the users piece and grab the opponents piece
    print("Awesome, now it's time to start the game")
    userPiece = input("Enter X or O to select your piece:")
    while userPiece not in ["X","O","x","o"]:
        print("Oops! Your piece is not valid! Please choose a proper piece!")
        userPiece = input("Enter X or O to select your piece:")
    if userPiece == "X":
        opponentPiece = "O"
    else:
        opponentPiece = "X"
    hasWon = False
    #now it's time to play the game, our condition will make it so that we continue playing the game until someone has won
    while not hasWon:
        xMove = int(input("Enter in the x value of where to place your move"))
        while xMove > 2 or xMove < 0:
            print("Oops you, can't enter places off the board!")
            xMove = int(input("Enter in the x value of where to place your move"))
        yMove = int(input("Enter in the y value of where to place your move"))
        while yMove > 2 or yMove < 0:
            print("Oops you, can't enter places off the board!")
            yMove = int(input("Enter in the y value of where to place your move"))
        while board[yMove][xMove] != "#":
            print("Space is taken!")
            xMove = int(input("Enter in the x value of where to place your move"))
            yMove = int(input("Enter in the y value of where to place your move"))
        board = userMove(board,userPiece,xMove,yMove)
        displayBoard(board)
        userMoves += 1
        result = checkWinner(board,userPiece,opponentPiece)
        if result == "User":
            print("You win!")
            hasWon = True
            break
        print("The computer is making their move")
        #Once the user makes two moves, the opponent needs to become smarter
        print(userMoves)
        if userMoves >= 2:
            board = computerSmarterMove(board, userPiece, opponentPiece)
        else:
            compX = random.randint(0,2)
            compY = random.randint(0,2)
            while board[compY][compX] == userPiece or board[compY][compX] == opponentPiece:
                compX = random.randint(0, 2)
                compY = random.randint(0, 2)
            board = opponentMove(board,opponentPiece,compX,compY)
        displayBoard(board)
        result = checkWinner(board,userPiece,opponentPiece)
        if result == "Opponent":
            print("Opponent wins!")
            hasWon = True
        if not hasWon and checkBoard(board):
            print("Tie!")
            break

def createBoard(width, height):
    board = []
    for y in range(height):
        curRow = []
        for x in range(width):
            curRow.append("#")
        board.append(curRow)
    return board
def displayBoard(board):
    for line in board:
        print(line)
def userMove(board,userPiece,x,y):
    board[y][x] = userPiece
    return board
def opponentMove(board,opponentPiece,x,y):
    board[y][x] = opponentPiece
    return board
def checkWinner(board, userPiece, opponentPiece):
    def is_winner(piece):
    #checking across
        for i in range(3):
            if board[i][0] == piece and board[i][1] == piece and board[i][2] == piece:
                return True
        #check down
        for i in range(3):
            if board[0][i] == piece and board[1][i] == piece and board[2][i] == piece:
                return True
            # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] == piece:
                return True
        if board[0][2] == board[1][1] == board[2][0] == piece:
                return True
    if is_winner(userPiece):
        return "User"
    if is_winner(opponentPiece):
        return "Opponent"
def computerSmarterMove(board,userPiece,opponentPiece):
    #checking if the computer can win!
    for i, row in enumerate(board):
        if row.count(opponentPiece) == 2 and row.count("#") == 1:
            board[i][row.index("#")] = opponentPiece
            return board
    for i in range(3):
        col = [board[j][i] for j in range(3)]
        if col.count(opponentPiece) == 2 and col.count("#") == 1:
            board[col.index("#")][i] = opponentPiece
            return board
    diag1 = [board[i][i] for i in range(3)]
    if diag1.count(opponentPiece) == 2 and diag1.count("#") == 1:
        i = diag1.index("#")
        board[i][i] = opponentPiece
        return board
    diag2 = [board[i][2 - i] for i in range(3)]
    if diag2.count(opponentPiece) == 2 and diag2.count("#") == 1:
        i = diag2.index("#")
        board[i][2 - i] = opponentPiece
        return board
    #
    # Block the user from winning
    #
    #blocking across
    for i, row in enumerate(board):
        #we need to find a place to block in the row
        if row.count(userPiece) == 2 and row.count("#") == 1:
            board[i][row.index("#")] = opponentPiece
            return board
    #blocking cloumns
    for i in range(3):
        col = [board[j][i] for j in range(3)]
        if col.count(userPiece) == 2 and col.count("#") == 1:
            board[col.index("#")][i] = opponentPiece
            return board
    #blocking diagonally
    diag1 = [board[i][i] for i in range(3)]
    if diag1.count(userPiece) == 2 and diag1.count("#") == 1:
        i = diag1.index("#")
        board[i][i] = opponentPiece
        return board
    #blocking diagonally again
    diag2 = [board[i][2 - i] for i in range(3)]
    if diag2.count(userPiece) == 2 and diag2.count("#") == 1:
        i = diag2.index("#")
        board[i][2 - i] = opponentPiece
        return board
    #else, let's make a random move
    compX = random.randint(0, 2)
    compY = random.randint(0, 2)
    while board[compY][compX] != "#":
        compX = random.randint(0, 2)
        compY = random.randint(0, 2)
    board = opponentMove(board,opponentPiece,compX,compY)
    return board
def checkBoard(board):
    for row in board:
        if "#" in row:
            return False
    return True
main()