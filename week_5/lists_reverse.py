num_of_int = int(input("How many integers? "))
integers = []

for i in range (num_of_int): 
    new_int = int(input("Enter an integer: "))
    integers.append(new_int)  
      
integers.reverse()
print()
print(*integers, sep=" ")