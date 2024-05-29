def CountingNeighbours(XCoord, YCoord, Board, rows, columns):
    Neighbours = 0
    center = Board[YCoord][XCoord]
    # Checks if the X-bounds of the board are too close and adjusts the start counter and end counter of X accordingly
    if (XCoord > 0) and (XCoord < rows - 1):
        xMin = -1
        xMax = 1
    elif(XCoord > 0) and (not(XCoord < rows - 1)):
        xMin = -1
        xMax = 0
    else:
        xMin = 0
        xMax = 1

    # Checks if the Y-bounds of the board are too close and adjusts the start counter and end counter of Y accordingly
    if (YCoord > 0) and (YCoord < columns - 1):
        yMin = -1
        yMax = 1
    elif (YCoord > 0) and (not(YCoord < columns - 1)):
        yMin = -1
        yMax = 0
    else:
        yMin = 0
        yMax = 1

    x = xMin
    # Actually checks the neighbours of the cell
    while x <= xMax:
        y = yMin
        while y <= yMax:
            Neighbours = Neighbours + Board[YCoord + y][XCoord + x]
            y += 1
        x += 1
    Neighbours -= center # account for the cell itself
    return Neighbours