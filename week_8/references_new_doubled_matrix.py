from copy import deepcopy
def new_doubled_matrix(matrix):
    # Return a copy of the matrix where each number in the original matrix is multiplied by 2

    doubled_matrix = deepcopy(matrix)

    for row in range(len(doubled_matrix)): # Go through the rows
       for i in range(len(doubled_matrix[i])): # Go through the indexes
          doubled_matrix[i] = doubled_matrix[i] * 2 # double them

    return doubled_matrix
    

def main():
 m1 = [[1, 2, 3], [4, 5, 6]]
 m2 = new_doubled_matrix(m1)
 print(m1)
 print(m2)
 
main()