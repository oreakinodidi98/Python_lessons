input_list = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]]

def mines (): 
    # display the input list
    for row in input_list:
        print(row)
    print("\n")
    # create a minesweeper grid
    rows = len(input_list)
    # get the number of columns in the input list
    columns = len(input_list[0])
    # create a 2D list with the same number of rows and columns as the input list
    minesweeper = [[0 for column in range(columns)] for row in range(rows)]
    # iterate over the input list and count the number of mines around each cell
    for row in range(rows):
        # iterate over the columns
        for col in range(columns):
            # check if the cell is a mine
            if input_list[row][col] == "#":
                # if it is a mine, set the cell in the minesweeper grid to "#"
                minesweeper[row][col] = "#"
            else:
                # if it is not a mine, count the number of mines around the cell
                count = 0
                # iterate over the cells around the current cell
                for i in range(-1, 2):
                    # iterate over the columns
                    for j in range(-1, 2):
                        # check if the cell is within the grid
                        if row + i >= 0 and row + i < rows and col + j >= 0 and col + j < columns:
                            # check if the cell is a mine
                            if input_list[row + i][col + j] == "#":
                                # if it is a mine, increment the count
                                count += 1
                                # set the cell in the minesweeper grid to the count
                minesweeper[row][col] = count
                # display the minesweeper grid
    for row in minesweeper:
        # print the row
        print(row)
    return

mines()