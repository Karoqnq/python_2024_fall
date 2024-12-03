string = input("Enter a string: ")

if string[::-1] == string: # Slicing the whole string starting from -1 (the end) to the start gives a reverse copy, then compare it to the starting string
    print("Yes")
else:
    print("No")