def count_distinct(distinct_list: list):

    return len(set(distinct_list)) # remove all duplicates and count all distinct

def main():

    list = []

    for i in range (5):
        num = int(input("Enter a number: "))
        list.append(num)

    result = count_distinct(list)
    
    print(f"{result}")

if __name__ == "__main__":
 main()
    