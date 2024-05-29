rows = 10 
columns = 10

board = [[0 for i in range(columns)]for n in range(rows)]

#get valid user input for coordinates to play, return row and column 
def getInput():
    try:
        row, column = input("Input row and then column: ")
        row = int(row) - 1
        column = ord(column.upper()) - 65
    except:
        print("Invalid input")
        row, column = getInput()
    while row > rows - 1 or row < 0 or column > columns - 1 or column < 0: 
        print("Invalid input")
        try:
            row, column = input("Input row and then column: ")
            row = int(row) - 1
            column = ord(column.upper()) - 65
        except:
            print("Invalid input")
            row, column = getInput()
    return row, column 

def makeMove(row, column):
    board[row][column] = 1

def makeInitialPlacements():
    MakeAnotherMove = 'Y'
    while MakeAnotherMove.upper() == 'Y':
        row, column = getInput()
        makeMove(row, column)
        MakeAnotherMove = input("would you like to make another move? (y/n): ").upper()
        
makeInitialPlacements()