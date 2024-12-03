how_many = int(input("How many surnames? "))
surname_list = []

for i in range(how_many):
     
     surname = input("Enter a surname: ")
     surname_list.append(surname.capitalize())

final_surnames = sorted(set(surname_list)) # sorted sorts them alphabetically and set removes duplicates

print()
print(*final_surnames, sep=" ")