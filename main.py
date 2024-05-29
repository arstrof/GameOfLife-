from InitialBoardAndInput import makeInitialPlacements
from UpdateBoard import UpdateBoard
from PrintBoard import printBoard
from Globals import board, rows, columns

makeInitialPlacements()

NextTurn = input("if you want to continue press enter, otherwise type n: ")

while NextTurn != "n":
    board = UpdateBoard(board, rows, columns)

    printBoard(board)

    NextTurn = input("if you want to continue press enter, otherwise type n: ")
