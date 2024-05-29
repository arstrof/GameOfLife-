from Globals import board, columns, rows

print('', end=' ')
for i in range(columns):
    char = chr(65 + i)
    print(char, end=' ')

print('')

for row in range(rows):
    print(row + 1, end=' ')
    for column in range(columns):
        print(board[row][column], end=' ')
    print('',end='\n')