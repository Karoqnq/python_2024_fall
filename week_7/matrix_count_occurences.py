def count_occurrences(matrix, num):
    
    count = 0

    for row in matrix: # go through each row
        for element in row: # go through every element in the row
            if element == num: # if element equals the number count +1 
                count += 1
    
    return count

def main():

    num_list = [7, 2, 3] # predefined numbers
    matrix = [[7, 7, 7, 0], [7, 7, 7, 5], [7, 2, 2, 2, 2]] # predefined matrix

    for num in num_list: # go through each number and count the occurrences of the num in the matrix
        count = count_occurrences(matrix, num)
        print(count)

main()