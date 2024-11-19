try:
    user_input = input("Enter an integer: ")  # Get the user input as a string
    user_num = int(user_input) # Convert it into an integer if possibly

except ValueError:
    print(f"'{user_input}' is not an integer")

else:
    print("OK")