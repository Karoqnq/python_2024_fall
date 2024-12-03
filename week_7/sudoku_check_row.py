def row_ok(grid, row_index):
# arguments sudoku grid (matrix) and row index (int)
# item on a row represents a number 0 - 9, 0 is an empty square
# function return false if more than one occurrence of a single number other than 0

    used = set() # Keep track of the digits that have been used and seen in the row

    for num in grid[row_index]: # Go through the numbers in the row of the matrix
        if num != 0: # No need to check 0s as they're empty spaces
            if num in used: # If number is in used set it's a duplicate
                return False
            used.add(num) # Add the number to the set if it's not

    return True # If not duplicates the row is valid

def main():
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(row_ok(sudoku, row_index=0)) # True
    print(row_ok(sudoku, row_index=1)) # False
    print(row_ok(sudoku, row_index=8)) # True

if __name__ == "__main__":
    main() 