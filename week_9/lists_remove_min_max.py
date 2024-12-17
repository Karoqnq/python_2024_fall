def remove_min_max(num_list):

    if len(num_list) <= 1:
        num_list.clear() # Clear the list if it's less than or equal to 1
        return 
    
    # Get the min and max values of
    min_num = min(num_list) 
    max_num = max(num_list)

    # Remove those values
    num_list.remove(min_num)
    num_list.remove(max_num)
    
def main():
    a = [3, 1, 4, 1, 5]
    remove_min_max(a)

    print(a)
if __name__ == "__main__":
    main()
