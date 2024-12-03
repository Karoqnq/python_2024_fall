string = input("Enter a string: ")

if len(string) != len(set(string)): # Checks if the length of the normal string and the length of the string which had (if) duplicates removed
    print("Contains duplicate(s)")
else:
    print("No duplicates")