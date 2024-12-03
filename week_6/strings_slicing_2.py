string = input("Enter a string: ")

if len(string) < 2: # if string shorter than 2 char
    print("Too short string")
else:
    print(string[-2]) # if string longer, print second to last char