integers = []

for i in range (5): 
    new_int = int(input("Enter an integer: "))
    integers.append(new_int) 

print()
integers.sort(reverse=True)
print(*integers)