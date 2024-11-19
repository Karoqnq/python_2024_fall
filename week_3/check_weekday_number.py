try:
    user_input = int(input("Enter a weekday number: "))
        
    if user_input < 1 or user_input > 7:
        print("Please enter an integer between 1 and 7")
    else:
        print("OK")
    
except ValueError:
    print("Please enter an integer between 1 and 7")