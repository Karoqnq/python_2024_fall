print("=== Creating a dictionary ===")
dictionary = {}

while True:
    english_word = input("Enter english word (quit ends): ")
    if english_word.lower() == "quit":
        break
    finnish_word = input("Enter finnish word: ")
    dictionary[english_word.lower()] = finnish_word.lower()

print()
print("=== Using a dictionary ===")

while True:
    translate = input("Enter english word (quit ends): ")
    if translate.lower() == "quit":
        break
    if translate.lower() not in dictionary:
        print("Unknown word")
    else:    
        print(dictionary[translate.lower()])