
string = input("Enter first string: ").strip()
count = 0

while True:

    if string.lower() == "quit": # Checks for the first input, if its quit it says bye. Lower makes it case insensitive
        print("Bye!")
        break

    if string.lower() == "pearl":
        count += 1

    string = input("Enter next string: ").strip()

    if string.lower() == "quit": # Checks for the following inputs.
        if count >= 0:
            print()
            print(f"{count} pearls")
        print("Bye!")
        break





