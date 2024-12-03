letter_list = ["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]

letter = input("Enter grade letter: ")

percentage = (letter_list.count(letter) / len(letter_list)) * 100

print(f"{percentage:.1f} %")
