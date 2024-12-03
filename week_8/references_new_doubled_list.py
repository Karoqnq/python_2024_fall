from copy import deepcopy
def new_doubled_list(num_list):
# return a copy of the list where each number in the original list is multiplied by two

    second_list = deepcopy(num_list) # Make a deep copy so the original list doesn't change
    
    for i in range(len(second_list)): # in the range of the list go through all the indexes
        second_list[i] = second_list[i] * 2 # Multiply each index by 2

    return second_list

def main():
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = new_doubled_list(first_list)

    print(first_list)
    print(second_list)

main()
    