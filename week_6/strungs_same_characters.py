string1 = input("Enter first string: ").replace(" ", "") # Replace empty spaces with no space
string2 = input("Enter second string: ").replace(" ", "")

if sorted(string1) == sorted(string2): # Sort the strings in alphabetical order
    print("Same characters")
else:
    print("Different characters")