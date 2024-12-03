def column_ok(grid, column_index):
# 1-9 numbers occur once, 0 is empty
# Check if column is valid

    used = set() # Keep track of the digits that have been used and seen in the row
    for i in range(len(grid)): # Go through the rows of the grid
        num = grid[i][column_index] # Get the element of the column index
        if num != 0: # No need to check 0s as they're empty spaces
                if num in used: # If number is in used set it's a duplicate
                    return False
                used.add(num) # Add the number to the set if it's not

    return True # If not duplicates the column is valid

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

    print(column_ok(sudoku, column_index=0)) # False
    print(column_ok(sudoku, column_index=1)) # True
    print(column_ok(sudoku, column_index=8)) # True


if __name__ == "__main__":
    main() 