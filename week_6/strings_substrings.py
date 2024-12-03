string = input("Enter a string: ")
character = input("Enter a character: ")

for i in range(len(string) - 3): # only go up to the length - 3 to make sure that there is always a 4 character substring
    if string[i] == character: # if the letter in the string matches the input character
        substring = string[i:i+4] # print the substring starting from this letter and make it into a 4 letter word ex. 1:1+4 = 1:5 
        print(substring)