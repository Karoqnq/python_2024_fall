surnames_list = []

while True:
    surname = input("Enter a surname (ok ends): ")

    if surname == "ok":
        break
    
    surnames_list.append(surname)

surnames_list = sorted(set(surnames_list))

print()
print(*surnames_list, sep=", ")

