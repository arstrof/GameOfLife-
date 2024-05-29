from Test_for_Ars_CountingNeighbours import CountingNeighbours




def UpdateBoard(board, YDimensions, XDimensions): #YDimensions is equivalent to rows, XDimensions is equivalent to cols
    

    NewBoard = [[None for _ in range(XDimensions)] for _ in range(YDimensions)]
    print(NewBoard)

    counter = 0

    for YCoordinate in range(YDimensions):
        for XCoordinate in range(XDimensions):
            
            
            NumOfNeighbours = CountingNeighbours(XCoordinate, YCoordinate, board, rows=YDimensions, cols=XDimensions, counter=counter) #YDimensions is equivalent to rows, XDimensions is equivalent to cols

            print(XCoordinate, YCoordinate)


            if NumOfNeighbours <= 1 or NumOfNeighbours >= 4: #checking the solitude and overpopulation 
                NewBoard[YCoordinate][XCoordinate] = 0

            elif board[YCoordinate][XCoordinate] == 1 and NumOfNeighbours == 2 or NumOfNeighbours == 3: #checking if the cell survives
                NewBoard[YCoordinate][XCoordinate] = 1
            
            elif board[YCoordinate][XCoordinate] == 0 and NumOfNeighbours == 3: #new cell appears 
                NewBoard[YCoordinate][XCoordinate] = 1
            
            else: #the space remanis empty
                NewBoard[YCoordinate][XCoordinate] = 0
            counter += 1
    return NewBoard

board = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]

print(UpdateBoard(board, 3, 3))


    

    