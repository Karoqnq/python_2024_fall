#With if and else

user_num = int(input("Enter an integer: "))

if user_num <= 1:  
    print("Nothing to be printed")

else:
    total_sum = 0

    for i in range(user_num, 0, -1):
        print(i, end=" ")
        total_sum += i 

    print() 
    print(f"The sum is {total_sum}")  