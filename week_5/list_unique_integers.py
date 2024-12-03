def unique_integers(num_list: list):

    return sorted(set(num_list)) # remove all duplicates and count all distinct
    
def main():

    num_list = []

    for i in range (5):
        num = int(input("Enter an integer: "))
        num_list.append(num)

    result = unique_integers(num_list)
    sorted_num_list = sorted(num_list)

    print(*result, sep=", ")
    print(*sorted_num_list, sep =", ")

if __name__ == "__main__":
 main()
