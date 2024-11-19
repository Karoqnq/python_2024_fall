try:
    user_input = int(input("Enter a non-negative integer: "))
    
    if user_input < 0:
        print("Please enter a non-negative integer")
    else:
        result = 1
        # If the input is 0, return 1 since 0!! is 1
        if user_input == 0:
            result = 1
        else:
            # Even or odd?
            if user_input % 2 == 0:
                # If even, calculate the product of all even numbers from 2 to n
                for i in range(2, user_input + 1, 2):
                    result = result * i

            else:
                # If odd, calculate the product of all odd numbers from 1 to n
                for i in range(1, user_input + 1, 2):
                    result = result * i    

        print(f"{user_input}!! = {result}")
    
except ValueError:
    print("Please enter a non-negative integer")