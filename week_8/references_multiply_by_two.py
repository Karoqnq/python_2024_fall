from copy import deepcopy

def multiply_by_two(num_list):
    
    deep_num_list = deepcopy(num_list) # Make a deep copy so the original list doesn't change
    
    for num in range(len(deep_num_list)): # in the range of the list go through all the indexes
        deep_num_list[num] = deep_num_list[num] * 2 # Multiply each index by 2

    print(deep_num_list) # Print the new list

def main():
    numbers = [1, 2, 3, 4, 5, 6]
    more_numbers = [10, 20, 30]

    print(numbers)
    multiply_by_two(numbers)

    print(more_numbers)
    multiply_by_two(more_numbers)

main()