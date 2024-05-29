from Globals import board, columns, rows

def printBoard(board):

    print('   ', end='')
    for i in range(columns):
        char = chr(65 + i)
        print(char, end=' ')

    print('')

    for row in range(rows):
        numOfSpaces = 3 - len(str(row + 1))
        print(str(row + 1), end='')
        print(' ' * numOfSpaces, end='')
        for column in range(columns):
            print(board[row][column], end=' ')
        print('',end='\n')