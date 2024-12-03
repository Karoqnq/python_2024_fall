string = input("Enter a string: ")

for i in range(len(string)):
    print(string[0:i + 1]) # slicing doesn't include the end character so we need to add 1 so it'll print the whole string