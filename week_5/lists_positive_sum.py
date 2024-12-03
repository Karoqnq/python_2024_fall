def positive_sum(number_list: list):

    total = 0
    for num in number_list:
        if num > 0:
            total += num

    return total


def main():
      
    number_list = []

    for i in range (5):
        number = int(input("Enter an integer: "))
        number_list.append(number)

    total = positive_sum(number_list)
    
    print()
    print(f"{total}")

main()
