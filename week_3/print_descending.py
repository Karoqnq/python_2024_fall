#With exception handling

try:
    user_num = int(input("Enter an integer: "))
    total_sum = 0

   
    for i in range(user_num, 0, -1):
        print(i, end=" ")
        total_sum += i 

    print()
    print(f"The sum is {total_sum}")

except ValueError:
    print("Nothing to be printed.")