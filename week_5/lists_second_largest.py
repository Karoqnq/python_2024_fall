def second_largest(number_list):

    distinct_list = list(set(number_list)) # remove duplicates

    if len(distinct_list) <= 1: # check if it's empty or has only one value
       return None
    
    distinct_list.sort(reverse= True) # sort the distinct list in a descending order

    return distinct_list[1] # return the second index [0,1] as it's the second largest

def main():

    num_list = []
    
    for i in range (5):
        num = int(input("Enter a number: "))
        num_list.append(num)

    result = second_largest(num_list)

    print(f"{result}")

if __name__ == "__main__":
 main()