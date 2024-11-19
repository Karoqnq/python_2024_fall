new_word = input("Enter a word (quit ends): ")
words = []

while new_word != "quit":  
    words.append(new_word)  
    new_word = input("Enter a word (quit ends): ")  

words.sort()  
print("\n".join(words)) # Join converts the list elements into a single string