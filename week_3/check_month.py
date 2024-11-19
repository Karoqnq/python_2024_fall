while True:
    user_input = input("Enter a month number: ")

    try:
        month = int(user_input)

        if month > 12 or month < 1:
            print(f"{month} is not a valid month number\n")
        else:
            print("OK")
            break
    
    except ValueError:
        print(f"'{user_input}' is not a valid month number\n")